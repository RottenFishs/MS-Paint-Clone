import pygame
import random
import GUI

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

r_range = random.randrange(255)
g_range = random.randrange(255)
b_range = random.randrange(255)

fill_color = (255, 255, 255)

pygame.draw.rect(screen, fill_color, pygame.Rect(0, 0, 512, 512))

pygame.display.flip()


class Pencil:
    """A class representing a pencil tool for drawing on the canvas.

    Attributes:
        active (bool): Flag indicating if the tool is currently selected.
        drawing (bool): Flag indicating if the tool is drawing pixels on the canvas.
        previous_pos (tuple): The previous mouse cursor position.
    """

    def __init__(self) -> None:
        # This tool is currently selected
        self.active = True

        # Should currently be drawing pixels onto canvas
        self.drawing = False

        # Some previous coords so the mouse actually draws lines
        self.previous_pos = (0, 0)

    def _mouse_down_(self):
        # Internal method for handling mouse down
        self.previous_pos = pygame.mouse.get_pos()
        self.drawing = True

    def _mouse_up_(self):
        # Internal method for handling mouse up
        self.previous_pos = pygame.mouse.get_pos()
        self.drawing = False

    def _tick_(self, canvas_obj):
        # Internal method for updating the pencil tool
        if self.drawing:
            current_pos = pygame.mouse.get_pos()
            color = main_gui.__get_selected_color__()
            pygame.draw.line(canvas_obj.surface, color, current_pos, self.previous_pos)
            self.previous_pos = current_pos
            pygame.display.flip()


pencil_tool = Pencil()


while run_program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run_program = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            pencil_tool._mouse_down_()
        if event.type == pygame.MOUSEBUTTONUP:
            pencil_tool._mouse_up_()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.image.save(screen, "test_file.png")
            if event.key == pygame.K_o:
                loaded_image = pygame.image.load("test_file.png")
                screen.fill((255, 255, 255))
                myCanvas.surface.blit(loaded_image, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run_program = False
                break

    if not run_program:
        break

    pencil_tool._tick_(myCanvas)

    myCanvas._draw_(screen)

    main_gui.__draw__()

    pass

    pygame.display.flip()
