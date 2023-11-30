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

    def _mouse_down_(self,canvas_obj):
        # Internal method for handling mouse down
        self.previous_pos = pygame.mouse.get_pos()
        self.drawing = True

    def _mouse_up_(self,canvas_obj):
        # Internal method for handling mouse up
        self.previous_pos = pygame.mouse.get_pos()
        self.drawing = False

    def _mouse_scroll_(self, canvas_obj, dir):
        # internal method for handling the mouse scrolling upwards
        pass

    def _tick_(self, canvas_obj, color):
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
            
            pygame.draw.line(canvas_obj.surface, color, new_current_pos, new_prev)
            self.previous_pos = current_pos
            pygame.display.flip()


# class Eraser():
#     def __init__(self) -> None:
#         self.pencil = Pencil()
    
#     def _mouse_down_(self):
#         self.pencil._mouse_down_()
    
#     def _mouse_up_(self):
#         self.pencil._mouse_up_()

#     def _tick_(self, canvas_obj, color):
#         self.pencil._tick_(canvas_obj,(255,255,255))


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
    
    def _tick_(self, canvas_obj,color):
        # Internal method for updating the panning tool
    
        if self.panning:
            
            current_pos = pygame.mouse.get_pos()
            
            canvas_obj.offset = (
                self.previous_offset[0] + current_pos[0] - self.previous_pos[0],
                self.previous_offset[1] + current_pos[1] - self.previous_pos[1]
            )



class Tool():
    pencil_object = Pencil()
    # eraser_object = Eraser()
    # fill_object = Fill()
    panning_object = Panning()
    # brush_object = Brush()
    # eyedropper_object = Eyedropper()

    tool_dictionary = {
        "pencil": pencil_object,
        # "eraser": eraser_object,
        # "fill": fill_object,
        "panning": panning_object,
        # "brush": brush_object,
        # "eyedropper": eyedropper_object,
    }

    def __init__(self):
        self.current_tool = None
    
    def __update_Tool__(self, selected_tool):
        self.current_tool = Tool.tool_dictionary[selected_tool]

    def _mouse_down_(self,canvas_obj):
        self.current_tool._mouse_down_(canvas_obj)


    def _mouse_up_(self,canvas_obj):
        self.current_tool._mouse_up_(canvas_obj)

    def _tick_(self, canvas_obj, color):
        self.current_tool._tick_(canvas_obj, color)
  
    def _mouse_scroll_(self, canvas_obj, dir):
        self.current_tool._mouse_scroll_(canvas_obj,dir)

