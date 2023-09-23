#!/usr/bin/python3
""" unittests for the rectangle class """


from models.rectangle import Rectangle
from models.base import Base
import unittest
import json
import sys
import io
import os


class TestRectangleInitialization(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(Rectangle(1, 2, 0, 0, 99).id, 99)
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_num_args(self):
        with self.assertRaises(TypeError):  # No args
            Rectangle()

        with self.assertRaises(TypeError):  # One arg
            Rectangle(1)

        try:
            Rectangle(1, 2)  # Two args
        except TypeError:
            self.fail("TypeError should not be raised")

        try:
            Rectangle(1, 2, 3)  # Three args
        except TypeError:
            self.fail("TypeError should not be raised")

        try:
            Rectangle(1, 2, 3, 4)  # Four args
        except TypeError:
            self.fail("TypeError should not be raised")

    def test_incorrect_types(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_negative_args(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_zero_value_args(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_privacy_of_attr(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 1, 0, 0).__width

        with self.assertRaises(AttributeError):
            Rectangle(1, 1, 0, 0).__height

        with self.assertRaises(AttributeError):
            Rectangle(1, 1, 0, 0).__x

        with self.assertRaises(AttributeError):
            Rectangle(1, 1, 0, 0).__y

    def test_getters_and_setters(self):
        obj = Rectangle(1, 1, 0, 0, 100)

        # width setter and getter
        obj.width = 4
        self.assertEqual(4, obj.width)

        # height setter and getter
        obj.height = 4
        self.assertEqual(4, obj.height)

        # x setter and getter
        obj.x = 4
        self.assertEqual(4, obj.x)

        # y setter and getter
        obj.y = 4
        self.assertEqual(4, obj.y)

    def test_rectangle_area(self):
        self.assertEquals(Rectangle(1, 2).area(), 2)

    def test_to_str(self):
        #  Test __str__ method
        obj = Rectangle(4, 6, 2, 1, 12)

        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        actual_output = obj.__str__()
        self.assertEquals(actual_output, expected_output)

    def test_display(self):
        #  Test output without x & y
        obj = Rectangle(2, 1)

        #  Redirect stdout to capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        obj.display()

        sys.stdout = sys.__stdout__  #  Reset stdout

        actual_output = captured_output.getvalue()
        expected_output = "##\n"
        self.assertEquals(actual_output, expected_output)

        #  Test output without y
        obj = Rectangle(2, 1, 2)

        #  Redirect stdout to capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        obj.display()

        sys.stdout = sys.__stdout__

        actual_output = captured_output.getvalue()
        expected_output = "  ##\n"
        self.assertEqual(actual_output, expected_output)

        #  Test output with both x & y are not zero
        obj = Rectangle(2, 1, 2, 2)

        #  Redirect stdout to capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        obj.display()

        sys.stdout = sys.__stdout__

        actual_output = captured_output.getvalue()
        expected_output = "\n\n  ##\n"
        self.assertEqual(actual_output, expected_output)

    def test_to_dictionary(self):
        obj = Rectangle(10, 2, 1, 9, 100)

        expected_output = {'x': 1, 'y': 9, 'id': 100, 'height': 2, 'width': 10}
        self.assertEqual(obj.to_dictionary(), expected_output)

    def test_update(self):
        dummy = Rectangle(1, 1, 1, 1, 99)

        #  Test when no arguments updated
        dummy.update()
        self.assertEqual("[Rectangle] (99) 1/1 - 1/1", str(dummy))

        #  Test with one argument updated
        dummy.update(2)
        self.assertEqual("[Rectangle] (2) 1/1 - 1/1", str(dummy))

        #  Test with two arguments updated
        dummy.update(2, 2)
        self.assertEqual("[Rectangle] (2) 1/1 - 2/1", str(dummy))

        #  Test with three arguments updated
        dummy.update(2, 2, 2)
        self.assertEqual("[Rectangle] (2) 1/1 - 2/2", str(dummy))

        #  Test with four arguments updated
        dummy.update(2, 2, 2, 2)
        self.assertEqual("[Rectangle] (2) 2/1 - 2/2", str(dummy))

        #  Test with all five arguments updated
        dummy.update(2, 2, 2, 2, 2)
        self.assertEqual("[Rectangle] (2) 2/2 - 2/2", str(dummy))

        #  Test with kwargs: id
        dummy.update(id=99)
        self.assertEqual("[Rectangle] (99) 2/2 - 2/2", str(dummy))

        #  Test with kwargs: id, width
        dummy.update(id=99, width=1)
        self.assertEqual("[Rectangle] (99) 2/2 - 1/2", str(dummy))

        #  Test with kwargs: id, width, height
        dummy.update(id=99, width=1, height=1)
        self.assertEqual("[Rectangle] (99) 2/2 - 1/1", str(dummy))

        #  Test with kwargs: id, width, height, x
        dummy.update(id=99, width=1, height=1, x=1)
        self.assertEqual("[Rectangle] (99) 1/2 - 1/1", str(dummy))

        #  Test with kwargs: id, width, height, x, y
        dummy.update(id=99, width=1, height=1, x=1, y=1)
        self.assertEqual("[Rectangle] (99) 1/1 - 1/1", str(dummy))

    def test_create(self):
        #  Test with kwargs: id
        try:
            obj = Rectangle.create(id=89)
            self.assertEqual(obj.id, 89)
        except TypeError:
            self.fail("TypeError should not be raised")

        #  Test with kwargs: id, width
        try:
            obj = Rectangle.create(id=89, width=1)
            self.assertEqual(obj.width, 1)
        except TypeError:
            self.assertEqual("TypeError should not be raised")

        #  Test with kwargs: id, width, height
        obj = Rectangle.create(id=89, width=1, height=2)
        self.assertEqual(obj.height, 2)

        #  Test with kwargs: id, width, height, x
        obj = Rectangle.create(id=89, width=1, height=2, x=3)
        self.assertEqual(obj.x, 3)

        #  Test with kwargs: id, width, height, x, y
        obj = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(obj.y, 4)

    def test_rectangle_save_to_file(self):
        # Test when the list is None
        Rectangle.save_to_file(None)
        expected_output = "[]"

        with open("Rectangle.json", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_output)

        #  Test when list is []
        Rectangle.save_to_file([])
        expected_output = "[]"

        with open("Rectangle.json", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_output)

        #  Test when the list is not empty
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        expected_output = json.dumps([r1.to_dictionary(), r2.to_dictionary()])

        with open("Rectangle.json", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_output)

    def test_load_from_file(self):
        #  Test loading from a non-existing file
        path = "Rectangle.json"
        if os.path.isfile(path):
            os.remove(path)

        instances = Rectangle.load_from_file()
        self.assertEqual(instances, [])

        #  Test loading from the existing file
        test_data = [Rectangle(1, 2).to_dictionary()]
        with open(path, 'w') as f:
            f.write(json.dumps(test_data))

        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), len(test_data))




if __name__ == '__main__':
    unittest.main()
