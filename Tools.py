import pygame
import math


class Tool:
    """
    A class that represents a collection of drawing tools for a canvas.

    This class contains several nested classes, each representing a different drawing tool.
    The class establishes instances of each tool so it can swtich and use a selected tools methods.
    Attributes:
        pencil_object (Pencil): An instance of the Pencil tool.
        eraser_object (Eraser): An instance of the Eraser tool.
        fill_object (Fill): An instance of the Fill tool.
        panning_object (Panning): An instance of the Panning tool.
        brush_object (Brush): An instance of the Brush tool.
        eyedropper_object (Eyedropper): An instance of the Eyedropper tool.
        tool_dictionary (dict): A dictionary mapping tool names to their corresponding instances.
        current_tool (Tool): The currently selected tool.
    """

    class Pencil:
        """A class representing a pencil tool for drawing on the canvas.

        A tool used to draw onto the canvas with thin lines

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

        def _tick_(self, canvas_obj, color, ___):
            # Internal method for updating the pencil tool
            if self.drawing:

                current_pos = pygame.mouse.get_pos()

                # the current pos needs to be adjusted based on the canvas'
                # size.
                new_current_pos = (
                    (current_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale,
                    (current_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale,
                )

                # as well as the previous pos. But we don't want to actually
                # edit it.
                new_prev = (
                    (self.previous_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale,
                    (self.previous_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale,
                )

                pygame.draw.line(canvas_obj.surface, color, new_current_pos, new_prev)
                self.previous_pos = current_pos
                pygame.display.flip()

    class Brush:
        """A class representing a brush tool for drawing on the canvas.

        A tool used to draw onto the canvas with a size that is adjustable via the scroll wheel

        Attributes:
            active (bool): Flag indicating if the tool is currently selected.
            drawing (bool): Flag indicating if the tool is drawing pixels on the canvas.
            size (int): Number that represents the size of the brush
            previous_pos (tuple): The previous mouse cursor position.
        """

        def __init__(self) -> None:
            # This tool is currently selected
            self.active = True

            # Should currently be drawing pixels onto canvas
            self.drawing = False

            # represents how large the brush should draw
            self.size = 2

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
            # internal method for handling the mouse scrolling

            if dir == 1:
                if self.size < 16:
                    self.size += 1
            elif dir == -1:
                if self.size > 3:
                    self.size -= 1

        def _tick_(self, canvas_obj, color, ___):
            # Internal method for updating the pencil tool
            if self.drawing:

                current_pos = pygame.mouse.get_pos()

                # the current pos needs to be adjusted based on the canvas'
                # size.
                new_current_pos = (
                    (current_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale,
                    (current_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale,
                )

                # as well as the previous pos. But we don't want to actually
                # edit it.
                new_prev = (
                    (self.previous_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale,
                    (self.previous_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale,
                )

                line_length = math.dist(new_prev, new_current_pos)

                # pygame.draw.circle(canvas_obj.surface, color, new_current_pos, self.size)

                # draw_coords = (
                #         ((new_prev[0] * 1) + (new_current_pos[0] * 1))/2,
                #         ((new_prev[1] * 1) + (new_current_pos[1] * 1)/2),
                #     )

                # pygame.draw.circle(canvas_obj.surface, color, draw_coords, self.size)

                if line_length > 0:

                    steps = math.ceil(line_length)

                    for i in range(steps):

                        prev_multi = i
                        current_multi = steps - i

                        draw_coords = (
                            (
                                (new_prev[0] * prev_multi)
                                + (new_current_pos[0] * current_multi)
                            )
                            / steps,
                            (
                                (new_prev[1] * prev_multi)
                                + (new_current_pos[1] * current_multi)
                            )
                            / steps,
                        )

                        pygame.draw.circle(
                            canvas_obj.surface, color, draw_coords, self.size
                        )

                self.previous_pos = current_pos
                pygame.display.flip()

    class Eraser:
        """A class representing an eraser tool for erasing on the canvas.

        The eraser allows users to erase parts of their drawing on the canvas.
        Basically does it by drawing onto the canvas in white.

        Attributes:
            active (bool): Flag indicating if the tool is currently selected.
            drawing (bool): Flag indicating if the tool is erasing pixels on the canvas.
            size (int): Number that represents the size of the eraser.
            previous_pos (tuple): The previous mouse cursor position.
            color (tuple): The color of the eraser, always set to white (255, 255, 255).

        """

        def __init__(self) -> None:
            # This tool is currently selected
            self.active = True

            # Should currently be drawing pixels onto canvas
            self.drawing = False

            # represents how large the brush should draw
            self.size = 2

            # Some previous coords so the mouse actually draws lines
            self.previous_pos = (0, 0)

            # Color is always white
            self.color = (255, 255, 255)

        def _mouse_down_(self, canvas_obj):
            # Internal method for handling mouse down
            self.previous_pos = pygame.mouse.get_pos()
            self.drawing = True

        def _mouse_up_(self, canvas_obj):
            # Internal method for handling mouse up
            self.previous_pos = pygame.mouse.get_pos()
            self.drawing = False

        def _mouse_scroll_(self, canvas_obj, dir):
            # internal method for handling the mouse scrolling

            if dir == 1:
                if self.size < 16:
                    self.size += 1
            elif dir == -1:
                if self.size > 1:
                    self.size -= 1

        def _tick_(self, canvas_obj, __, ___):
            # Internal method for updating the pencil tool
            if self.drawing:

                current_pos = pygame.mouse.get_pos()

                # the current pos needs to be adjusted based on the canvas'
                # size.
                new_current_pos = (
                    (current_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale,
                    (current_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale,
                )

                # as well as the previous pos. But we don't want to actually
                # edit it.
                new_prev = (
                    (self.previous_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale,
                    (self.previous_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale,
                )

                line_length = math.dist(new_prev, new_current_pos)

                # pygame.draw.circle(canvas_obj.surface, color, new_current_pos, self.size)

                # draw_coords = (
                #         ((new_prev[0] * 1) + (new_current_pos[0] * 1))/2,
                #         ((new_prev[1] * 1) + (new_current_pos[1] * 1)/2),
                #     )

                # pygame.draw.circle(canvas_obj.surface, color, draw_coords, self.size)

                if line_length > 0:

                    steps = math.ceil(line_length)

                    for i in range(steps):

                        prev_multi = i
                        current_multi = steps - i

                        draw_coords = (
                            (
                                (new_prev[0] * prev_multi)
                                + (new_current_pos[0] * current_multi)
                            )
                            / steps,
                            (
                                (new_prev[1] * prev_multi)
                                + (new_current_pos[1] * current_multi)
                            )
                            / steps,
                        )

                        pygame.draw.circle(
                            canvas_obj.surface, self.color, draw_coords, self.size
                        )

                self.previous_pos = current_pos
                pygame.display.flip()

    class Fill:
        """
        A class representing a fill tool that colors closed shapes on the canvas.

        The fill tool allows the user to fill a closed area on the canvas with a specific color.

        Attributes:
            fill (bool): Flag indicating if the fill operation is currently active.
            visited_pixels (set): A set storing the pixels that have been visited during the fill operation.
        """

        def __init__(self) -> None:

            self.fill = False
            self.visited_pixels = set()

            pass

        def _mouse_down_(self, canvas_obj):

            if pygame.mouse.get_pos()[1] > 50:
                self.fill = True

            pass

        def _mouse_up_(self, canvas_obj):

            self.fill = False
            self.visited_pixels.clear()

            pass

        def _mouse_scroll_(self, canvas_obj, dir):
            pass

        def _tick_(self, canvas_obj, color, ___):

            if self.fill:
                current_pos = pygame.mouse.get_pos()

                # the current pos needs to be adjusted based on the canvas'
                # size.
                new_current_pos = (
                    math.floor(
                        (current_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale
                    ),
                    math.floor(
                        (current_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale
                    ),
                )

                self.fill_pixel(new_current_pos, canvas_obj, color)

            pass

        # Private function to check and recursively fill in pixels.
        def fill_pixel(self, current_position, canvas_obj, color):

            if (
                current_position[0] >= 0
                and current_position[0] <= canvas_obj.width - 1
                and current_position[1] >= 0
                and current_position[1] <= canvas_obj.height - 1
            ):

                old_color = canvas_obj.surface.get_at(current_position)
                if old_color == color:
                    return

                stack = [current_position]

                while stack:

                    x, y = stack.pop()

                    if canvas_obj.surface.get_at((x, y)) == old_color:
                        canvas_obj.surface.set_at((x, y), color)

                        # Add left pixel if valid index
                        if x > 0:
                            stack.append((x - 1, y))

                        # Add right pixel if valid index
                        if x < canvas_obj.width - 1:
                            stack.append((x + 1, y))

                        # Add bottom pixel if valid index
                        if y > 0:
                            stack.append((x, y - 1))

                        # Add top pixel if valid index
                        if y < canvas_obj.height - 1:
                            stack.append((x, y + 1))

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

            # Some previous coords so the tool knows the difference, and thus
            # where to pan to
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
            if dir == 1 and canvas_obj.scale < 5:
                canvas_obj.scale *= 1.1
            elif dir == -1 and canvas_obj.scale > 0.2:
                canvas_obj.scale *= 0.9

        def _tick_(self, canvas_obj, color, ___):
            # Internal method for updating the panning tool

            if self.panning:

                current_pos = pygame.mouse.get_pos()

                canvas_obj.offset = (
                    self.previous_offset[0] + current_pos[0] - self.previous_pos[0],
                    self.previous_offset[1] + current_pos[1] - self.previous_pos[1],
                )

    class Eyedropper:
        """
        A class representing an eyedropper tool for selecting colors on the canvas.

        The eyedropper tool allows the user to select a color from the canvas.
        The selected color can then be used by other tools.

        Attributes:
            eyedropper (bool): Flag indicating if the eyedropper operation is currently active.
            color (tuple): The color selected by the eyedropper tool.
        """

        def __init__(self) -> None:
            self.eyedropper = False
            self.color = None

        def _mouse_down_(self, canvas_obj):
            # Internal method for handling mouse down

            if pygame.mouse.get_pos()[1] > 50:
                self.eyedropper = True

        def _mouse_up_(self, canvas_obj):
            # Internal method for handling mouse up
            self.eyedropper = False
            pass

        def _mouse_scroll_(self, canvas_obj, dir):
            # internal method for handling the mouse scrolling upwards
            pass

        def _tick_(self, canvas_obj, ___, GUI_obj):
            # Internal method for updating the eyedropper tool
            if self.eyedropper:

                current_pos = pygame.mouse.get_pos()

                # the current pos needs to be adjusted based on the canvas'
                # size.
                new_current_pos = (
                    math.floor(
                        (current_pos[0] - canvas_obj.offset[0]) / canvas_obj.scale
                    ),
                    math.floor(
                        (current_pos[1] - canvas_obj.offset[1]) / canvas_obj.scale
                    ),
                )

                self.color = canvas_obj.surface.get_at(new_current_pos)
                GUI_obj.change_selected_color(self.color)

            pass

    pencil_object = Pencil()
    eraser_object = Eraser()
    fill_object = Fill()
    panning_object = Panning()
    brush_object = Brush()
    eyedropper_object = Eyedropper()

    tool_dictionary = {
        "pencil": pencil_object,
        "eraser": eraser_object,
        "fill": fill_object,
        "panning": panning_object,
        "brush": brush_object,
        "eyedropper": eyedropper_object,
    }

    def __init__(self):
        self.current_tool = None

    def __update_Tool__(self, selected_tool):
        """
        Updates the current tool based on the selected tool name.

        Args:
            selected_tool (str): The name of the selected tool.
        """
        self.current_tool = Tool.tool_dictionary[selected_tool]

    def _mouse_down_(self, canvas_obj):
        """
        Calls the _mouse_down_ method of the current tool.

        Args:
            canvas_obj (Canvas): The canvas object that the Tool class is tracking.
        """
        self.current_tool._mouse_down_(canvas_obj)

    def _mouse_up_(self, canvas_obj):
        """
        Calls the _mouse_up_ method of the current tool.

        Args:
            canvas_obj (Canvas): The canvas object that the Tool class is tracking.
        """
        self.current_tool._mouse_up_(canvas_obj)

    def _tick_(self, canvas_obj, color, GUI_obj):
        """
        Calls the _tick_ method of the current tool.

        Args:
            canvas_obj (Canvas): The canvas object that the Tool class is tracking.
            color (tuple): The currently selected color.
            GUI_obj (GUI): The GUI object that the Tool class is tracking.
        """
        self.current_tool._tick_(canvas_obj, color, GUI_obj)

    def _mouse_scroll_(self, canvas_obj, dir):
        """
        Calls the _mouse_scroll_ method of the current tool.

        Args:
            canvas_obj (Canvas): The canvas object that the Tool class is tracking.
            dir (int): The direction of the mouse scroll, 1 for up and -1 for down.
        """
        self.current_tool._mouse_scroll_(canvas_obj, dir)
