#!/usr/bin/python3
""" unittests for the base class """


from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def test_init(self):
        obj0 = Base()
        obj1 = Base(10)
        obj2 = Base()

        self.assertEqual(obj0.id, 1)
        self.assertEqual(obj1.id, 10)
        self.assertEqual(obj2.id, 2)

    def test_integer_validator(self):
        obj0 = Base()

        with self.assertRaisesRegex(TypeError, "attr must be an integer"):
            obj0.integer_validator("attr", 12.5)

        with self.assertRaisesRegex(ValueError, "attr must be > 0"):
            obj0.integer_validator("attr", 0)

        with self.assertRaisesRegex(TypeError, "attr must be an integer"):
            obj0.integer_validator("attr", "2", True)

        with self.assertRaisesRegex(ValueError, "attr must be >= 0"):
            obj0.integer_validator("attr", -1, True)
