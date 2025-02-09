# image-sorter
Image Sorter GUI is a Python-based tool designed to help users efficiently sort images into labeled subfolders using a simple and intuitive graphical interface. Perfect for organizing large collections of images, this tool allows you to assign labels to images with just a click or a keypress.

# Image Sorter GUI

A Python-based graphical user interface (GUI) tool for sorting images into labeled subfolders. This program allows users to view images one by one, assign labels to them, and move the images into corresponding folders based on the selected labels.

## Features

- **Full-Screen Mode**: The application opens in full-screen mode for an immersive experience.
- **Image Display**:
  - Images are displayed in their original size if they fit within the window.
  - If more than 10% of the image would be cropped, it is automatically scaled down while maintaining aspect ratio.
  - Images are always centered in the window, with unused space filled with a black background.
- **Label Buttons**: Labels are displayed as buttons on the right side of the screen for easy selection.
- **Keyboard Shortcuts**:
  - Press `Esc` to exit the application.
  - Use number keys (`1`, `2`, etc.) to select labels quickly.
- **File Management**: Images are moved to subfolders named after the selected labels.

## Installation

### Prerequisites

- Python 3.7 or higher
- Required Python packages:
  - `Pillow` (for image processing)
  - `tkinter` (for the GUI)

Install the required dependencies using `pip`:

```bash
pip install pillow
