import pygame
import GUI
import Tools
import undo_redo
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


        self.offset = (0, 0)

        # if this is true, then the canvas and thus the display needs to be redrawn
        self.undrawn = False
        
        self.scale = 1

    def draw(self, window_screen):
        """
        Draws the canvas on the provided screen.

        This method first fills the entire screen with a gray color. Then, it scales the surface of the canvas 
        according to the current scale factor and blits it onto the provided screen at the current offset.

        Args:
            window_screen (pygame.Surface): The Pygame screen surface on which the canvas will be drawn.
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

main_gui = GUI.GUI(screen)

fill_color = (255, 255, 255)

pygame.draw.rect(screen, fill_color, pygame.Rect(0, 0, 512, 512))

pygame.display.flip()


tool = Tools.Tool()
tool.__update_Tool__(main_gui.get_selected_tool())

shortcut = undo_redo.shortcut(myCanvas)

image_handler = ImageHandler(myCanvas)

while run_program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            shortcut.clearTemp()
            run_program = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            tool._mouse_down_(myCanvas)
            shortcut.check_if_viable(main_gui.get_selected_tool())

        elif event.type == pygame.MOUSEBUTTONUP:
            tool._mouse_up_(myCanvas)
            shortcut.save(myCanvas)

        elif event.type == pygame.MOUSEWHEEL:
            tool._mouse_scroll_(myCanvas,event.y)

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
                run_program = False
                break

    if not run_program:
        break

    tool._tick_(myCanvas,main_gui.get_selected_color(),main_gui)

    myCanvas.draw(screen)

    main_gui.draw()

    tool.__update_Tool__(main_gui.get_selected_tool())
    pass

    pygame.display.flip()
