import cv2
import os
import sys
from pathlib import Path
from datetime import datetime

INPUT_DIR = "input"
OUTPUT_DIR = "outputs"
DEFAULT_LOW_THRESHOLD = 100
DEFAULT_HIGH_THRESHOLD = 200
DEFAULT_SCALE_FACTOR = 1.1
DEFAULT_MIN_NEIGHBORS = 5


def ensure_output_dir():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


def timestamped_name(prefix, filename):
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{stem}_{ts}{suffix}"


def resolve_input_path(filename):
    path = Path.cwd() / INPUT_DIR / filename
    return str(path)


def equalize_histogram(input_path, output_path):
    img = cv2.imread(input_path)

    if img is None:
        print(f"Error: Could not read image at {input_path}", file=sys.stderr)
        return None

    if len(img.shape) == 2:
        equalized = cv2.equalizeHist(img)
    else:
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        y, cr, cb = cv2.split(ycrcb)
        y_eq = cv2.equalizeHist(y)
        merged = cv2.merge((y_eq, cr, cb))
        equalized = cv2.cvtColor(merged, cv2.COLOR_YCrCb2BGR)

    cv2.imwrite(output_path, equalized)
    print(f"Histogram equalized. Contrast improved. Saved to {output_path}")
    return output_path


def canny_edge_detection(input_path, output_path, low_threshold, high_threshold):
    img = cv2.imread(input_path)

    if img is None:
        print(f"Error: Could not read image at {input_path}", file=sys.stderr)
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, low_threshold, high_threshold)

    cv2.imwrite(output_path, edges)
    print(f"Canny edges (thresholds {low_threshold}/{high_threshold}, kernel 5x5). Saved to {output_path}")
    return output_path


def detect_faces(input_path, output_path):
    img = cv2.imread(input_path)

    if img is None:
        print(f"Error: Could not read image at {input_path}", file=sys.stderr)
        return None

    cascade_path = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")

    if not os.path.exists(cascade_path):
        print(f"Error: Haar cascade file not found at {cascade_path}", file=sys.stderr)
        return None

    face_cascade = cv2.CascadeClassifier(cascade_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=DEFAULT_SCALE_FACTOR, minNeighbors=DEFAULT_MIN_NEIGHBORS
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "face", (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imwrite(output_path, img)
    print(f"Detected {len(faces)} face(s). Saved to {output_path}")
    return output_path


def prompt_int(prompt_text, default_value):
    raw = input(f"{prompt_text} [{default_value}]: ").strip()
    if raw == "":
        return default_value
    try:
        return int(raw)
    except ValueError:
        print(f"Invalid number, using default {default_value}")
        return default_value


def run_menu():
    ensure_output_dir()

    while True:
        print("\nVisionCLI - Computer Vision Toolkit")
        print("1. Histogram Equalization")
        print("2. Canny Edge Detection")
        print("3. Haar Cascade Face Detection")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "4":
            print("Exiting VisionCLI.")
            sys.exit(0)

        if choice not in ("1", "2", "3"):
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        filename = input("Enter the image filename (must be inside the input/ folder): ").strip()
        input_path = resolve_input_path(filename)

        if not os.path.isfile(input_path):
            print(f"Error: {input_path} is not a valid file.", file=sys.stderr)
            continue

        if choice == "1":
            output_name = timestamped_name("equalized", filename)
            output_path = os.path.join(OUTPUT_DIR, output_name)
            equalize_histogram(input_path, output_path)

        elif choice == "2":
            low = prompt_int("Low threshold", DEFAULT_LOW_THRESHOLD)
            high = prompt_int("High threshold", DEFAULT_HIGH_THRESHOLD)
            output_name = timestamped_name("edges", filename)
            output_path = os.path.join(OUTPUT_DIR, output_name)
            canny_edge_detection(input_path, output_path, low, high)

        elif choice == "3":
            output_name = timestamped_name("faces", filename)
            output_path = os.path.join(OUTPUT_DIR, output_name)
            detect_faces(input_path, output_path)


if __name__ == "__main__":
    run_menu()