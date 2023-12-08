"""Module that adds functionality to undo /redo"""
import os
import glob
import pygame # pylint: disable=import-error


class shortcut:
    """
    A class that handles undo and redo operations for the canvas.

    This class keeps track of all changes made to the canvas within the
    canvas_stack directory and allows the user to undo or redo these changes.

    Attributes:
        counter (int): A counter that keeps track of the current image displayed
        size (int): The total number of saved images in canvas_stack directory
        check (bool): A flag indicating whether the current tool can make
        changes that should be tracked.
    """

    def __init__(self, canvas_obj) -> None:
        """
        Initialize the shortcut class.

        This method sets up the shortcut class by saving the initial default state of the canvas.

        Args:
            canvas_obj (Canvas): The canvas object that the shortcut class will be tracking.
        """
        self.counter = 0
        self.size = 1

        self.check = False
        blank_file = "canvas_stack/temp_image{}.png".format(0)

        if not os.path.exists("canvas_stack"):
            os.makedirs("canvas_stack")

        pygame.image.save(canvas_obj.surface, blank_file)

        pass

    def check_if_viable(self, current_tool):
        """
        Checks if the current tool can make changes that should be saved.

        This method checks if the current tool is appropriate tool is selected
        (pencil,brush,eraser,fill),
        if the mouse isn't on the GUI, and if the left mouse button was pressed.

        If all the above is true, self.check is set to true, otherwise it is false
        Args:
            current_tool (str): The name of the current tool.

        Returns:
            None
        """
        left_click = pygame.mouse.get_pressed()
        viable_tools = ["pencil", "brush", "eraser", "fill"]
        if (
            current_tool in viable_tools
            and pygame.mouse.get_pos()[1] > 50
            and left_click[0]
        ):
            self.check = True
        else:
            self.check = False

    def save(self, canvas_obj):
        """
        Saves the current state of the canvas into canvas_stack directory.

        This method saves the current state of the canvas into canvas_stack directory.
        If a change has been made that should be tracked/self.check is true.

        It also deletes all images ahead of it, in the case of a user undoing and saving

        Args:
            canvas_obj (Canvas): The canvas object that the shortcut class is tracking.

        Returns:
            None
        """
        if self.check:
            self.counter += 1
            image_file = "canvas_stack/temp_image{}.png".format(self.counter)
            for i in range(self.counter + 1, self.size):
                delete_file = "canvas_stack/temp_image{}.png".format(i)
                if os.path.exists(delete_file):
                    os.remove(delete_file)

            self.size = self.counter + 1
            pygame.image.save(canvas_obj.surface, image_file)

    def undo(self, canvas_obj):
        """
        Undoes the last change made to the canvas.

        This method undoes the last change made to the canvas, if there is a change to undo.
        It does this by loading the last image within the canvas_stack folder

        Args:
            canvas_obj (Canvas): The canvas object that the shortcut class is tracking.

        Returns:
            None
        """
        if self.counter > 0:
            self.counter -= 1
            image_file = "canvas_stack/temp_image{}.png".format(self.counter)
            undo_image = pygame.image.load(image_file)
            canvas_obj.surface.blit(undo_image, (0, 0))
            pygame.display.flip()

    def redo(self, canvas_obj):
        """
        Redoes the last change that was undone.

        This method redoes the last change that was undone, if there is a change to redo.
        It does this by iterating counter by 1 to get the next image in the stack

        Args:
            canvas_obj (Canvas): The canvas object that the shortcut class is tracking.

        Returns:
            None
        """
        if self.counter < self.size - 1:
            self.counter += 1
            image_file = "canvas_stack/temp_image{}.png".format(self.counter)
            undo_image = pygame.image.load(image_file)
            canvas_obj.surface.blit(undo_image, (0, 0))
            pygame.display.flip()

    def clearTemp(self):
        """
        Clears all temporary images.

        This method deletes all temporary images that were saved for undo/redo operations
        wihtin the canvas_stack directory.

        Returns:
            None
        """
        temp = glob.glob("canvas_stack/temp_image*.png")
        for file in temp:
            os.remove(file)
