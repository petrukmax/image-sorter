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
```

Вот текст, который вы можете скопировать и вставить напрямую в файл `README.md` для GitHub. Он уже содержит правильную разметку Markdown и включает все предоставленные вами данные:

```markdown
# Image Sorter GUI
```
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
```

## Running the Program

1. Clone this repository or download the script.
2. Run the script from the command line with the following arguments:

```bash
python sort_folder.py --folder <INPUT-FOLDER> --labels <LABEL1> <LABEL2> ...
```

#### Example:

```bash
python sort_folder.py --folder ./images --labels cat dog other
```

This will:
- Load all `.tif`, `.tiff`, `.jpg`, and `.png` files from the `./images` folder.
- Create subfolders named `cat`, `dog`, and `other` inside the `./images` folder.
- Allow you to sort images into these subfolders by clicking the corresponding buttons.

## Usage

1. Launch the program with the appropriate arguments.
2. The first image will be displayed in full-screen mode.
3. Click on one of the label buttons on the right side of the screen to assign a label to the current image.
4. The image will be moved to the corresponding subfolder, and the next image will be displayed.
5. Repeat until all images are sorted.
6. Press `Esc` to exit the program at any time.

## Customization

- **Labels**: Specify any number of labels when launching the program. These labels will determine the names of the subfolders.
- **Image Formats**: The program supports `.tif`, `.tiff`, `.jpg`, and `.png` formats. You can modify the code to include additional formats if needed.

## Notes

- If an image exceeds the screen size by more than 10%, it will be scaled down to fit within the window while preserving its aspect ratio.
- The program creates subfolders for each label if they do not already exist.
- If no valid images are found in the specified folder, the program will exit with an error message.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [Apache License Version 2.0](LICENSE).

---

### Acknowledgments

This project was inspired by and adapted from the following repositories:
- [baumgach/image-sorter](https://github.com/baumgach/image-sorter)
- [Nestak2/image-sorter2](https://github.com/Nestak2/image-sorter2)
```
