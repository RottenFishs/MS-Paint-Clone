import pygame
import tkinter as tk
from tkinter import filedialog


class ImageHandler:
   def __init__(self, canvas):
       self.canvas = canvas

   def load_image(self):
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
       root = tk.Tk()
       # Hide the main window
       root.withdraw()
       # Open save file dialog with limited file types
       file_path = filedialog.asksaveasfilename(
           filetypes = [("PNG File", "*.png"), ("JPEG File", "*.jpg")],
           defaultextension = ''
       )
       # Save screenshot if a file/filepath is selected
       if file_path:
            try:
                pygame.image.save_extended(self.canvas.surface, file_path)
            except pygame.error as e:
                print(f"Failed to save image: {e}")
