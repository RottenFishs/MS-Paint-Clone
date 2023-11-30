import pygame

class Pencil():
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

    def _tick_(self, canvas_obj, color):
        # Internal method for updating the pencil tool
        if self.drawing:
            current_pos = pygame.mouse.get_pos()
            pygame.draw.line(canvas_obj.surface, color, current_pos, self.previous_pos)
            self.previous_pos = current_pos
            pygame.display.flip()

class Eraser():
    def __init__(self) -> None:
        self.pencil = Pencil()
    
    def _mouse_down_(self):
        self.pencil._mouse_down_()
    
    def _mouse_up_(self):
        self.pencil._mouse_up_()

    def _tick_(self, canvas_obj, color):
        self.pencil._tick_(canvas_obj,(255,255,255))


class Tool():
    pencil_object = Pencil()
    eraser_object = Eraser()
    # fill_object = Fill()
    # panning_object = Panning()
    # brush_object = Brush()
    # eyedropper_object = Eyedropper()

    tool_dictionary = {
        "pencil": pencil_object,
        "eraser": eraser_object,
        # "fill": fill_object,
        # "panning": panning_object,
        # "brush": brush_object,
        # "eyedropper": eyedropper_object,
    }

    def __init__(self):
        self.current_tool = None
    
    def __update_Tool__(self, selected_tool):
        self.current_tool = Tool.tool_dictionary[selected_tool]

    def _mouse_down_(self):
        self.current_tool._mouse_down_()


    def _mouse_up_(self):
        self.current_tool._mouse_up_()

    def _tick_(self, canvas_obj, color):
        self.current_tool._tick_(canvas_obj, color)
  

