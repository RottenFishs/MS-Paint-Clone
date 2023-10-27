import pygame


class GUI:
    """A class representing the graphical user interface for the MS Paint Clone.

    This class provides tools and buttons for interacting with the canvas and selecting colors.

    Attributes:
        eraser (ToolButton): The eraser tool button.
        fill (ToolButton): The fill tool button.
        panning (ToolButton): The panning tool button.
        pencil (ToolButton): The pencil tool button.
        brush (ToolButton): The brush tool button.
        eyedropper (ToolButton): The eyedropper tool button.
        red (ColorButton): The red color button.
        green (ColorButton): The green color button.
        blue (ColorButton): The blue color button.
        black (ColorButton): The black color button.
        selected_color (ColorButton): The currently selected color button.

    """

    class ToolButton:
        """A class representing a tool button in the GUI.

        Attributes:
            STATIC_SELECTED (str): The currently selected tool.
            state (bool): Flag indicating if the button is in an active state.
            clicked (bool): Flag indicating if the button has been clicked.
            activeImage (pygame.Surface): The active image for the button.
            inactiveImage (pygame.Surface): The inactive image for the button.
            screen (pygame.Surface): The Pygame screen surface.
            mouse_was_pressed (bool): Flag indicating if the mouse button was pressed.
            image (pygame.Surface): The current image of the button.
            name (str): The name of the tool.
            rect (pygame.Rect): The rectangle representing the button's position and size.
            x (int): The X-coordinate of the button.
            y (int): The Y-coordinate of the button.
        """

        STATIC_SELECTED = "pencil"

        def __init__(self, x, y, inactive, active, screen, name):
            self.state = False
            self.clicked = False
            self.active_image = active
            self.inactive_image = inactive
            self.screen = screen
            self.mouse_was_pressed = False
            self.image = self.inactive_image
            self.name = name

            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.topleft = (x, y)

        # Internal method for drawing ToolButtons on the screen
        def _draw_(self):
            position = pygame.mouse.get_pos()
            mouse_is_pressed = pygame.mouse.get_pressed()[0] == 1
            if self.rect.collidepoint(position):
                if (
                    mouse_is_pressed
                    and self.clicked == False
                    and not self.mouse_was_pressed
                ):
                    self.clicked = True
                    self.state = True
                    GUI.ToolButton.STATIC_SELECTED = self.name

            if GUI.ToolButton.STATIC_SELECTED != self.name:
                self.state = False

            if not mouse_is_pressed:
                self.clicked = False

            if not self.state:
                self.image = self.inactive_image
            else:
                self.image = self.active_image

            self.screen.blit(self.image, (self.rect.x, self.rect.y))
            pygame.display.flip
            self.mouse_was_pressed = mouse_is_pressed

        def _set_active_(self, is_active):
            # Internal method to change the state of a ToolButton
            if is_active:
                self.state = True
            else:
                self.state = False

    class ColorButton:
        STATIC_SELECTED = (0, 0, 0)

    class ColorButton():
        """A class representing a color button in the GUI.

        This class defines a button for selecting colors.

        Attributes:
        STATIC_SELECTED (tuple): The currently selected color as an RGB tuple.
        state (bool): Flag indicating if the button is in an active state.
        screen (pygame.Surface): The Pygame screen surface.
        mouse_was_pressed (bool): Flag indicating if the mouse button was pressed.
        color (tuple): The color associated with the button.
        rect (pygame.Rect): The rectangle representing the button's position and size.

        """
        STATIC_SELECTED = (0,0,0)
        def __init__(self, x, y, color, screen,length, width):
            self.state = False
            self.screen = screen
            self.mouse_was_pressed = False
            self.color = color
            self.screen = screen
            self.rect = pygame.Rect(x, y, length, width)

        def _draw_(self):
            # Internal method to draw color buttons on the GUI
            position = pygame.mouse.get_pos()
            mouse_is_pressed = pygame.mouse.get_pressed()[0] == 1
            if self.rect.collidepoint(position):
                if (
                    mouse_is_pressed
                    and self.clicked == False
                    and not self.mouse_was_pressed
                ):
                    self.clicked = True
                    self.state = True
                    GUI.ColorButton.STATIC_SELECTED = self.color

            if GUI.ColorButton.STATIC_SELECTED != self.color:
                self.state = False

            if not mouse_is_pressed:
                self.clicked = False

            pygame.draw.rect(self.screen, self.color, self.rect)
            pygame.display.flip
            self.mouse_was_pressed = mouse_is_pressed

        def _set_color_to_selected_(self):
            # Internal method to change the color to the selected color
            self.color = GUI.ColorButton.STATIC_SELECTED

    def __init__(self, screen):
        self.screen = screen

        # Pencil tool
        pencil_inactive_image = pygame.image.load("Images/pencil_inactive.png")
        pencil_active_image = pygame.image.load("Images/pencil_active.png")
        pencil = GUI.ToolButton(
            20, 20, pencil_inactive_image, pencil_active_image, self.screen, "pencil"
        )
        pencil._draw_()
        pencil._set_active_(True)

        # Eraser tool
        eraser_inactive_image = pygame.image.load("Images/eraser_inactive.png")
        eraser_active_image = pygame.image.load("Images/eraser_active.png")
        eraser = GUI.ToolButton(
            50, 20, eraser_inactive_image, eraser_active_image, self.screen, "eraser"
        )
        eraser._draw_()

        # Fill tool
        fill_inactive_image = pygame.image.load("Images/fill_inactive.png")
        fill_active_image = pygame.image.load("Images/fill_active.png")
        fill = GUI.ToolButton(
            80, 20, fill_inactive_image, fill_active_image, self.screen, "fill"
        )
        fill._draw_()

        # Panning tool
        panning_inactive_image = pygame.image.load("Images/panning_inactive.png")
        panning_active_image = pygame.image.load("Images/panning_active.png")
        panning = GUI.ToolButton(
            110,
            20,
            panning_inactive_image,
            panning_active_image,
            self.screen,
            "panning",
        )
        panning._draw_()

        # Brush tool
        brush_inactive_image = pygame.image.load("Images/brush_inactive.png")
        brush_active_image = pygame.image.load("Images/brush_active.png")
        brush = GUI.ToolButton(
            140, 20, brush_inactive_image, brush_active_image, self.screen, "brush"
        )
        brush._draw_()

        # Eyedropper tool
        eyedropper_inactive_image = pygame.image.load("Images/eyedropper_inactive.png")
        eyedropper_active_image = pygame.image.load("Images/eyedropper_active.png")
        eyedropper = GUI.ToolButton(
            170,
            20,
            eyedropper_inactive_image,
            eyedropper_active_image,
            self.screen,
            "eyedropper",
        )
        eyedropper._draw_()

        self.eraser = eraser
        self.fill = fill
        self.panning = panning
        self.pencil = pencil
        self.brush = brush
        self.eyedroppper = eyedropper

        red = GUI.ColorButton(330, 20, (255, 0, 0), self.screen, 18, 18)
        green = GUI.ColorButton(370, 20, (0, 255, 0), self.screen, 18, 18)
        blue = GUI.ColorButton(410, 20, (0, 0, 255), self.screen, 18, 18)
        black = GUI.ColorButton(450, 20, (0, 0, 0), self.screen, 18, 18)
        selected_color = GUI.ColorButton(
            240, 13, GUI.ColorButton.STATIC_SELECTED, self.screen, 30, 30
        )

        self.red = red
        self.green = green
        self.blue = blue
        self.black = black
        self.selected_color = selected_color
        pygame.display.flip

    def __draw__(self):
        # Grey Bar on top
        pygame.draw.rect(self.screen, (187, 192, 199), pygame.Rect(0, 0, 512, 50))
        pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(0, 0, 512, 8))
        self.brush._draw_()
        self.eraser._draw_()
        self.fill._draw_()
        self.panning._draw_()
        self.pencil._draw_()
        self.eyedroppper._draw_()

        self.red._draw_()
        self.green._draw_()
        self.blue._draw_()
        self.black._draw_()
        self.selected_color._set_color_to_selected_()
        self.selected_color._draw_()

        pygame.display.flip

    def __get_selected_tool__(self):
        return GUI.ToolButton.STATIC_SELECTED

    def __get_selected_color__(self):
        return GUI.ColorButton.STATIC_SELECTED
