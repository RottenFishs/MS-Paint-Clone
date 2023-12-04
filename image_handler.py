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
       # Load and display the selected image
       image = pygame.image.load(file_path)
       self.canvas.surface.blit(image, (0, 0))
       pygame.display.flip()

   def save_image(self):
       root = tk.Tk()
       # Hide the main window
       root.withdraw()
       # Open save file dialog with limited file types
       file_path = filedialog.asksaveasfilename(
           filetypes=[("PNG File", "*.png"), ("JPEG File", "*.jpg")]
       )
       # Save screenshot if a file/filepath is selected
       if file_path:
            try:
                pygame.image.save(self.canvas.surface, file_path)
            except pygame.error as e:
                print(f"Failed to save image: {e}")
