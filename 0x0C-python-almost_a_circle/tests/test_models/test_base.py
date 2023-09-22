#!/usr/bin/python3
""" unittests for the base class """

from models.base import Base
import unittest
import json


class TestBase(unittest.TestCase):
    def test_init(self):
        obj0 = Base()
        obj1 = Base(10)
        obj2 = Base()

        self.assertEqual(obj0.id, 1)
        self.assertEqual(obj1.id, 10)
        self.assertEqual(obj2.id, 2)

    def test_integer_validator(self):
        base_instance = Base()

        with self.assertRaisesRegex(TypeError, "attr must be an integer"):
            base_instance.integer_validator("attr", 12.5)

        with self.assertRaisesRegex(ValueError, "attr must be > 0"):
            base_instance.integer_validator("attr", 0)

        with self.assertRaisesRegex(TypeError, "attr must be an integer"):
            base_instance.integer_validator("attr", "2", True)

        with self.assertRaisesRegex(ValueError, "attr must be >= 0"):
            base_instance.integer_validator("attr", -1, True)

    def test_to_json_string(self):
        #  Test when list in not empty
        input_list = [{"key": "value"}]
        expected_output = json.dumps(input_list)
        self.assertEquals(Base.to_json_string(input_list), expected_output)

        #  Test when list is empty
        input_list = []
        expected_output = "[]"
        self.assertEquals(Base.to_json_string(input_list), expected_output)

        #  Test when list in None
        self.assertIsNotNone(Base.to_json_string(None))

    def test_from_json_string(self):
        #  Test when JSON string is not empty
        input_json = '[{"key": "value"}]'
        expected_output = [{"key": "value"}]
        self.assertEquals(Base.from_json_string(input_json), expected_output)

        #  Test when JSON string is empty
        input_json = "[]"
        expected_output = []
        self.assertEquals(Base.from_json_string(input_json), expected_output)

        #  Test when JSON string is None
        self.assertIsNotNone(Base.from_json_string(None))


if __name__ == '__main__':
    unittest.main()
