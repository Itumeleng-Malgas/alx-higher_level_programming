#!/usr/bin/python3
""" unittests for the rectangle class """


from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangleInitialization(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(Rectangle(1, 2, 0, 0, 99).id, 99)
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_args(self):
        with self.assertRaises(TypeError):
            Rectangle()  # No args

        with self.assertRaises(TypeError):
            Rectangle(12)  # One arg

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)  # Morethan 5 args

    def test_private_args(self):
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
