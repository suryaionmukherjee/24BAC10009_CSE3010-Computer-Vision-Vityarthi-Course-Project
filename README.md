Suryaion Mukherjee
Reg No: 24BAC10009

### Project title
VisionCLI: A Terminal-Based Computer Vision Toolkit

### Overview of the project
VisionCLI is a lightweight, terminal-native computer vision toolkit implemented entirely in Python and built on OpenCV. The application processes local image files entirely through a command-line interface and writes the results directly to the disk. It operates without calling graphical backends (like `cv2.imshow`), ensuring fully headless execution that is ideal for remote servers, continuous integration environments, and automated evaluations.

### Features
* **Histogram Equalization:** Enhances image contrast by equalizing the luminance channel for color images or the standard grayscale channel.
* **Canny Edge Detection:** Extracts structural edges using Gaussian blur and hysteresis thresholding, with configurable high and low thresholds.
* **Haar Cascade Face Detection:** Utilizes OpenCV's pre-trained frontal face cascade classifier to detect faces and annotate them with bounding boxes.

### Technologies/tools used
* Python 3
* OpenCV (`opencv-python==4.14.0.94`)
* NumPy
* Standard Python Libraries (`os`, `sys`, `pathlib`, `datetime`)

### Steps to install & run the project
1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt in the root directory of the project.
3. Install the required dependencies by running:
   `pip install -r requirements.txt`
4. Run the application by executing:
   `python main.py`

*(Note: This application runs entirely in the terminal without any GUI-based setup or external window displays).*

### Instructions for testing
1. Ensure you have a folder named `input` in the root directory (the script resolves paths relative to this folder).
2. Place a sample raster image (e.g., `test_image.jpg`) into the `input/` folder.
3. Run `python main.py` in your terminal.
4. When prompted by the menu, enter `1`, `2`, or `3` to select a processing module.
5. Type the exact filename of your test image (e.g., `test_image.jpg`) and press Enter.
6. The terminal will print a confirmation message. Navigate to the newly generated `outputs/` folder to view the processed image.
