import pygame
import random
import GUI
from image_handler import ImageHandler

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

        self.offset = (0, 50)

        # if this is true, then the canvas and thus the display needs to be redrawn
        self.undrawn = False

        self.scale = 1

    def _draw_(self, window_screen):
        # Internal method for drawing the canvas
        
        fill_color = (127, 127, 127)
        pygame.draw.rect(screen, fill_color, pygame.Rect(0, 0, 512, 512))
        
        surf_display = pygame.transform.scale(
            self.surface, (self.width * self.scale, self.height * self.scale)
        )
        pygame.Surface.blit(window_screen, surf_display, self.offset)

    def _tick_(self):
        # Internal method for updating the canvas
        # self.scale *= 0.95
        pass


myCanvas = Canvas()

main_gui = GUI.GUI(screen)

r_range = random.randrange(255)
g_range = random.randrange(255)
b_range = random.randrange(255)

fill_color = (255, 255, 255)

pygame.draw.rect(screen, fill_color, pygame.Rect(0, 0, 512, 512))

pygame.display.flip()


class Panning:
    """A class that represents the Panning tool, for panning around the canvas.
    
    Attributes:
        active (bool): Flag indicating if the tool is currently selected.
        drawing (bool): Flag indicating if the tool is currently panning around.
        previous_pos (tuple): The previous mouse cursor position.
        previous_offset (tuple): The previous canvas offset.
    """

    def __init__(self) -> None:
        # This tool is currently selected
        self.active = True
        
        # Should currently be panning around the canvas
        self.panning = False
        
        # Some previous coords so the tool knows the difference, and thus where to pan to
        self.previous_pos = (0, 0)
        
        # The previous canvas offset for doing calculations for the panning
        self.previous_offset = (0, 0)

    def _mouse_down_(self, canvas_obj):
        # Internal method for handling mouse down
        self.previous_pos = pygame.mouse.get_pos()
        self.previous_offset = canvas_obj.offset
        self.panning = True

    def _mouse_up_(self, canvas_obj):
        # Internal method for handling mouse up
        self.panning = False

    def _mouse_scroll_(self, canvas_obj, dir):
        # internal method for handling the mouse scrolling upwards
        if dir == 1:
            canvas_obj.scale *= 1.1
        elif dir == -1:
            canvas_obj.scale *= 0.9
    
    def _tick_(self, canvas_obj):
        # Internal method for updating the panning tool
    
        if self.panning:
            
            current_pos = pygame.mouse.get_pos()
            
            canvas_obj.offset = (
                self.previous_offset[0] + current_pos[0] - self.previous_pos[0],
                self.previous_offset[1] + current_pos[1] - self.previous_pos[1]
            )
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

    def _mouse_down_(self, canvas_obj):
        # Internal method for handling mouse down
        self.previous_pos = pygame.mouse.get_pos()
        self.drawing = True

    def _mouse_up_(self, canvas_obj):
        # Internal method for handling mouse up
        self.previous_pos = pygame.mouse.get_pos()
        self.drawing = False

    def _mouse_scroll_(self, canvas_obj, dir):
        # internal method for handling the mouse scrolling upwards
        pass

    def _tick_(self, canvas_obj):
        # Internal method for updating the pencil tool
        if self.drawing:
            
            current_pos = pygame.mouse.get_pos()
            
            # the current pos needs to be adjusted based on the canvas' size.
            new_current_pos = (
                    (current_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale,
                    (current_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale
                    )
            
            # as well as the previous pos. But we don't want to actually edit it.
            new_prev = (
                    (self.previous_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale,
                    (self.previous_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale
                    )
            
            color = main_gui.__get_selected_color__()
            pygame.draw.line(canvas_obj.surface, color, new_current_pos, new_prev)
            self.previous_pos = current_pos
            pygame.display.flip()


# current_tool = Pencil()
current_tool = Panning()
image_handler = ImageHandler(myCanvas)

while run_program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run_program = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            current_tool._mouse_down_(myCanvas)
        elif event.type == pygame.MOUSEBUTTONUP:
            current_tool._mouse_up_(myCanvas)
        elif event.type == pygame.MOUSEWHEEL:
            current_tool._mouse_scroll_(myCanvas, event.y)

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_s:
                 image_handler.save_image()
                 
            if event.key == pygame.K_o:
                image_handler.load_image()
                
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run_program = False
                break

    if not run_program:
        break

    current_tool._tick_(myCanvas)

    myCanvas._draw_(screen)

    main_gui.__draw__()

    pass

    pygame.display.flip()
