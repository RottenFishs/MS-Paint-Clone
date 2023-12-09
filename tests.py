import unittest
import main

class TestMainMethods(unittest.TestCase):

    def test_check_canvas_size(self):
        # Test method to check if canvas is 512x512
        self.assertEqual(main.Canvas().height, 512)
        self.assertEqual(main.Canvas().width, 512)

    def test_check_default_tool(self):
        # Test method to check if default tool is pencil
        self.assertEqual(main.main_gui.get_selected_tool(), "pencil")

    def test_check_default_color(self):
        # Test method to check if the default color is black
        self.assertEqual(main.main_gui.get_selected_color(),(0,0,0))


if __name__ == '__main__':
    unittest.main()