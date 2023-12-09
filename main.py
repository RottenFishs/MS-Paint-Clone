"""Module that runs the whole program"""
import pygame # pylint: disable=import-error
import GUI
import Tools
import undo_redo
from image_handler import ImageHandler

# Initialize the Pygame window
screen = pygame.display.set_mode((512, 512), pygame.RESIZABLE)
"""The main window for the program"""

pygame.display.set_caption("MS Paint Clone")

RUN_PROGRAM = True
"""A flag to indicate whether the program should be ran"""

DIM0_SIZE = 512
"""Variable that holds window dimension"""
DIM1_SIZE = 512

"""Variable that holds window dimension"""


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

        self.offset = (0, 0)

        # if this is true, then the canvas and thus the display needs to be
        # redrawn
        self.undrawn = False

        self.scale = 1

    def draw(self, window_screen):
        """
        Draws the canvas on the provided screen.

        This method first fills the entire screen with a gray color. Then,
        it scales the surface of the canvasaccording to the current scale
        factor and blits it onto the provided screen at the current offset.

        Args:
            window_screen (pygame.Surface): The Pygame screen
            surface on which the canvas will be drawn.
        """

        fill_color = (127, 127, 127)
        pygame.draw.rect(screen, fill_color, pygame.Rect(0, 0, 512, 512))

        surf_display = pygame.transform.scale(
            self.surface, (self.width * self.scale, self.height * self.scale)
        )
        pygame.Surface.blit(window_screen, surf_display, self.offset)

    # def _tick_(self):
    #     # Internal method for updating the canvas
    #     # self.scale *= 0.95
    #     pass


myCanvas = Canvas()
"""Variable for main.py's canvas"""

main_gui = GUI.GUI(screen)
"""Variable for main.py's GUI object"""

fill_color = (255, 255, 255)
"""Variable used to color the screen white"""
pygame.draw.rect(screen, fill_color, pygame.Rect(0, 0, 512, 512))

pygame.display.flip()


tool = Tools.Tool()
"""Variable to run functions from the Tool object"""
tool.__update_Tool__(main_gui.get_selected_tool())

shortcut = undo_redo.shortcut(myCanvas)
"""Variable to run functions from the Shortcut object"""

image_handler = ImageHandler(myCanvas)
"""Variable to run functions from the ImageHandler object"""
while RUN_PROGRAM:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            shortcut.clearTemp()
            RUN_PROGRAM = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            tool._mouse_down_(myCanvas)
            shortcut.check_if_viable(main_gui.get_selected_tool())

        elif event.type == pygame.MOUSEBUTTONUP:
            tool._mouse_up_(myCanvas)
            shortcut.save(myCanvas)

        elif event.type == pygame.MOUSEWHEEL:
            tool._mouse_scroll_(myCanvas, event.y)

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:
                image_handler.save_image()

            if event.key == pygame.K_o:
                image_handler.load_image()

            if event.key == pygame.K_z and (pygame.key.get_mods() & pygame.KMOD_LCTRL):
                shortcut.undo(myCanvas)
            if event.key == pygame.K_y and (pygame.key.get_mods() & pygame.KMOD_LCTRL):
                shortcut.redo(myCanvas)

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                shortcut.clearTemp()
                RUN_PROGRAM = False
                break

    if not RUN_PROGRAM:
        break

    tool._tick_(myCanvas, main_gui.get_selected_color(), main_gui)

    myCanvas.draw(screen)

    main_gui.draw()

    tool.__update_Tool__(main_gui.get_selected_tool())

    pygame.display.flip()
