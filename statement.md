### Problem statement
Contemporary computer vision tutorials and student projects frequently assume an interactive desktop environment, relying on graphical event loops or web front ends. This creates a gap for deployments in headless environments, laboratory SSH sessions, or automated evaluation systems. There is a strict need for a lightweight, terminal-executable computer vision tool that processes images without heavy UI dependencies.

### Scope of the project
The system follows a three-tier local architecture confined to the file system, a CLI menu, and an in-process OpenCV processing engine. It handles local image I/O, applies selected algorithms, and writes outputs securely back to the disk without remote services or databases.

### Target users
Students, researchers, and developers who require reproducible, batch-friendly, or CLI-based image processing pipelines that bypass desktop environment assumptions.

### High-level features
* Menu-driven interface that gracefully handles invalid inputs without exiting.
* Robust file handling that automatically generates timestamped outputs and required output directories.
* Three core vision modules: Histogram Equalization, Canny Edge Detection, and Haar Cascade Face Detection.