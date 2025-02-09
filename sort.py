import argparse
import tkinter as tk
import os
from shutil import move
from PIL import ImageTk, Image

class ImageGui:
    """
    GUI for iFind1 image sorting. This draws the GUI and handles all the events.
    Useful, for sorting views into sub views or for removing outliers from the data.
    """
    def __init__(self, master, labels, paths):
        """
        Initialise GUI
        :param master: The parent window
        :param labels: A list of labels that are associated with the images
        :param paths: A list of file paths to images
        """
        self.master = master
        self.master.overrideredirect(True)  # Убираем синюю строку с кнопками
        self.master.configure(bg="black")  # Устанавливаем фон окна чёрным

        # Получаем размеры экрана
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Устанавливаем размер окна на весь экран
        self.master.geometry(f"{screen_width}x{screen_height}+0+0")

        self.master.bind("<Escape>", self.close_window)  # Закрыть окно по нажатию Esc
        self.master.bind("<Configure>", self.on_resize)  # Обработка изменения размера окна

        # Основной фрейм
        frame = tk.Frame(master, bg="black")
        frame.pack(fill="both", expand=True)

        # Правая панель для кнопок меток
        button_frame = tk.Frame(frame, bg="black")
        button_frame.pack(side="right", fill="y", padx=10, pady=10)

        # Кнопки меток
        for i, label in enumerate(labels):
            button = tk.Button(
                button_frame,
                text=label,
                command=lambda l=label: self.vote(l),
                bg="gray",
                fg="white",
                width=15,
                height=2
            )
            button.pack(pady=5, fill="x")

        # Левая панель для изображения
        image_frame = tk.Frame(frame, bg="black")
        image_frame.pack(side="left", fill="both", expand=True)

        # Start at the first file name
        self.index = 0
        self.paths = paths
        self.labels = labels
        self.n_labels = len(labels)
        self.n_paths = len(paths)

        # Set empty image container
        self.image_raw = None
        self.image = None
        self.image_panel = tk.Canvas(image_frame, bg="black", highlightthickness=0)  # Используем Canvas для центрирования
        self.image_panel.pack(fill="both", expand=True)

        # Отложенная загрузка первого изображения
        self.master.after(100, lambda: self.set_image(paths[self.index]))

    def set_image(self, path):
        """
        Helper function which sets a new image in the image view
        :param path: path to that image
        """
        try:
            self.image_raw = Image.open(path)
            self.display_image()
        except Exception as e:
            print(f"Error loading image: {e}")

    def display_image(self):
        """
        Display the image, scaling it if more than 10% is cropped.
        """
        # Get current window size
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()

        # Check if window size is valid
        if window_width <= 0 or window_height <= 0:
            return  # Skip displaying if window size is invalid

        # Original image dimensions
        img_width, img_height = self.image_raw.size

        # Calculate cropping percentage
        crop_x = max(0, (img_width - window_width) / img_width)
        crop_y = max(0, (img_height - window_height) / img_height)
        total_crop = max(crop_x, crop_y)

        # If more than 10% of the image is cropped, scale it down
        if total_crop > 0.1:
            scale_x = window_width / img_width
            scale_y = window_height / img_height
            scale = min(scale_x, scale_y)
            new_width = int(img_width * scale)
            new_height = int(img_height * scale)
            resized_image = self.image_raw.resize((new_width, new_height), Image.Resampling.LANCZOS)
            img_width, img_height = new_width, new_height
        else:
            resized_image = self.image_raw

        # Calculate position to center the image
        x_offset = max((window_width - img_width) // 2, 0)
        y_offset = max((window_height - img_height) // 2, 0)

        # Clear previous image
        self.image_panel.delete("all")

        # Convert to PhotoImage and display on the canvas
        self.image = ImageTk.PhotoImage(resized_image)
        self.image_panel.create_image(x_offset, y_offset, anchor="nw", image=self.image)

    def on_resize(self, event):
        """
        Handle window resize events
        """
        if event.widget == self.master:
            self.display_image()

    def show_next_image(self):
        """
        Displays the next image in the paths list
        """
        self.index += 1
        if self.index < self.n_paths:
            self.set_image(self.paths[self.index])
        else:
            self.master.quit()

    def vote(self, label):
        """
        Processes a vote for a label: Initiates the file moving and shows the next image
        :param label: The label that the user voted for
        """
        input_path = self.paths[self.index]
        self._move_image(input_path, label)
        self.show_next_image()

    @staticmethod
    def _move_image(input_path, label):
        """
        Moves a file to a new label folder using the shutil library.
        :param input_path: Path of the original image
        :param label: The label
        """
        root, file_name = os.path.split(input_path)
        output_path = os.path.join(root, label, file_name)
        print(" %s --> %s" % (file_name, label))
        move(input_path, output_path)

    def close_window(self, event=None):
        """
        Close the application
        """
        self.master.quit()

def make_folder(directory):
    """
    Make folder if it doesn't already exist
    :param directory: The folder destination path
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

# The main bit of the script only gets executed if it is directly called
if __name__ == "__main__":
    # Make input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', help='Input folder where the *tif images should be', required=True)
    parser.add_argument('-l', '--labels', nargs='+', help='Possible labels in the images', required=True)
    args = parser.parse_args()
    input_folder = args.folder
    labels = args.labels

    for label in labels:
        make_folder(os.path.join(input_folder, label))

    paths = []
    for file in os.listdir(input_folder):
        if file.lower().endswith((".tif", ".tiff", ".jpg", ".png")):
            path = os.path.join(input_folder, file)
            paths.append(path)

    if not paths:
        print("No .tif or .tiff or .jpg or .png files found in the specified folder.")
        exit(1)

    # Start the GUI
    root = tk.Tk()
    app = ImageGui(root, labels, paths)
    root.mainloop()
