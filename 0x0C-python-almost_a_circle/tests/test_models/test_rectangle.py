#!/usr/bin/python3
""" unittests for the rectangle class """


from models.rectangle import Rectangle
from models.base import Base
import unittest


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


if __name__ == '__main__':
    unittest.main()
