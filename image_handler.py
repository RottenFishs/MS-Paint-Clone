import pygame
import tkinter as tk
from tkinter import filedialog


class ImageHandler:
    """
    A class that handles loading and saving images for the canvas.

    This class provides methods to load an image from a file and draw it onto the canvas, and to save the current state of the canvas to an image file.

    Attributes:
        canvas (Canvas): The canvas object that the ImageHandler will be working with.
    """

    def __init__(self, canvas):
        """
        Initialize the ImageHandler class.

        This method sets up the ImageHandler class by storing a reference to the canvas that it will be working with.

        Args:
            canvas (Canvas): The canvas object that the ImageHandler will be working with.
        """
        self.canvas = canvas

    def load_image(self):
        """
        Loads an image from a file and draws it onto the canvas.

        This method opens a file dialog for the user to select an image file. If a file is selected, it loads the image and draws it onto the canvas.

        Args:
            None

        Returns:
            None
        """
        root = tk.Tk()
        # Hide the main window
        root.withdraw()
        # Open file explorer
        file_path = filedialog.askopenfilename(
            filetypes=[("PNG File", "*.png"), ("JPEG File", "*.jpg")]
        )
        # Check if a file was selected
        if file_path:
            # Load and display the selected image
            image = pygame.image.load(file_path)
            self.canvas.surface.blit(image, (0, 0))
            pygame.display.flip()
        else:
            print("No file selected.")

    def save_image(self):
        """
        Saves the current state of the canvas to an image file.

        This method opens a file dialog for the user to select a location and file name to save the current state of the canvas as an image file.

        Args:
            None

        Returns:
            None
        """
        root = tk.Tk()
        # Hide the main window
        root.withdraw()
        # Open save file dialog with limited file types
        file_path = filedialog.asksaveasfilename(
            filetypes=[("PNG File", "*.png"), ("JPEG File", "*.jpg")],
            defaultextension="",
        )
        # Save screenshot if a file/filepath is selected
        if file_path:
            try:
                pygame.image.save_extended(self.canvas.surface, file_path)
            except pygame.error as e:
                print(f"Failed to save image: {e}")
