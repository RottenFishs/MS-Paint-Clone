import pygame
import random
import GUI
import sys
import tkinter as tk
from tkinter import filedialog
import Tools

# Initialize the Pygame window
screen = pygame.display.set_mode((512, 512), pygame.RESIZABLE)
pygame.display.set_caption("MS Paint Clone")
run_program = True
dim0_size = 512
dim1_size = 512


class Canvas:
    """A class representing a drawing canvas

    Attributes:
        width (int): The width of the canvas.
        height (int): The height of the canvas.
        surface (pygame.Surface): The drawing surface.
        x_offset (int): The X-axis offset for the canvas.
        y_offset (int): The Y-axis offset for the canvas.
        undrawn (bool): A flag indicating if the canvas needs to be redrawn.
        scale (float): The scaling factor for the canvas.
    """

    def __init__(self, width=512, height=512) -> None:
        """
        Initialize a new Canvas.

        Args:
            width (int): The width of the canvas.
            height (int): The height of the canvas.
        """

        self.width = width
        self.height = height

        self.surface = pygame.Surface((width, height))
        self.surface.fill((255, 255, 255))  # test function

        self.x_offset = 0
        self.y_offset = 0

        # if this is true, then the canvas and thus the display needs to be redrawn
        self.undrawn = False

        self.scale = 1

    def _draw_(self, window_screen):
        # Internal method for drawing the canvas
        surf_display = pygame.transform.scale(
            self.surface, (self.width * self.scale, self.height * self.scale)
        )
        pygame.Surface.blit(window_screen, surf_display, (self.x_offset, self.y_offset))

    def _tick_(self):
        # Internal method for updating the canvas
        self.scale *= 0.95


myCanvas = Canvas()

main_gui = GUI.GUI(screen)

fill_color = (255, 255, 255)

pygame.draw.rect(screen, fill_color, pygame.Rect(0, 0, 512, 512))

pygame.display.flip()


tool = Tools.Tool()
tool.__update_Tool__(main_gui.__get_selected_tool__())

while run_program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run_program = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            # pencil_tool._mouse_down_()
            tool._mouse_down_()
        if event.type == pygame.MOUSEBUTTONUP:
            # pencil_tool._mouse_up_()
            tool._mouse_up_()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                root = tk.Tk()
                # Hide the main window
                root.withdraw()
                # Open save file dialog with limited file types
                file_path = filedialog.asksaveasfilename(
                    filetypes=[("PNG File", "*.png"), ("JPEG File", "*.jpg")]
                )
                # Save screenshot to the selected file
                pygame.image.save(pygame.display.get_surface(), file_path)
            if event.key == pygame.K_o:
                root = tk.Tk()
                # Hide the main window
                root.withdraw()
                # Open file explorer
                file_path = filedialog.askopenfilename()
                # Load and display the selected image
                image = pygame.image.load(file_path)
                myCanvas.surface.blit(image, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run_program = False
                break

    if not run_program:
        break

    # pencil_tool._tick_(myCanvas)
    tool._tick_(myCanvas,main_gui.__get_selected_color__())

    myCanvas._draw_(screen)

    main_gui.__draw__()
    tool.__update_Tool__(main_gui.__get_selected_tool__())
    pass

    pygame.display.flip()
