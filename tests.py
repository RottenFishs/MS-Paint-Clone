import unittest
import main

class TestMainMethods(unittest.TestCase):

    def check_canvas_size(self):
        # Test method to check if canvas is 512x512
        self.assertEqual(main.Canvas().height, 512)
        self.assertEqual(main.Canvas().width, 512)

    def check_default_tool(self):
        # Test method to check if default tool is pencil
        self.assertEqual(main.main_gui.get_selected_tool(), "pencil")

    def check_default_color(self):
        # Test method to check if the default color is black
        self.assertEqual(main.main_gui.get_selected_colorm,(0,0,0))

    def check_color_change(self):
        # Test method to check if a change in the color is detected
        main.main_gui.change_selected_color(12,12,12)
        self.assertEqual(main.main_gui.get_selected_color,(12,12,12))


if __name__ == '__main__':
    unittest.main()