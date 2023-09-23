#!/usr/bin/python3
""" unittests for the sqaure class """


from models.square import Square
from models.base import Base
import unittest
import json
import sys
import io
import os


class TestSquareInitialization(unittest.TestCase):
    def test_square_to_dictionary(self):
        obj = Square(10, 1, 9, 100)

        expected_output = {'x': 1, 'y': 9, 'id': 100, 'size': 10}
        self.assertEqual(obj.to_dictionary(), expected_output)

    def test_update(self):
        dummy = Square(1, 1, 1, 99)

        #  Test when no arguments updated
        dummy.update()
        self.assertEqual("[Square] (99) 1/1 - 1", str(dummy))

        #  Test with one argument updated
        dummy.update(2)
        self.assertEqual("[Square] (2) 1/1 - 1", str(dummy))

        #  Test with two arguments updated
        dummy.update(2, 2)
        self.assertEqual("[Square] (2) 1/1 - 2", str(dummy))

        #  Test with three arguments updated
        dummy.update(2, 2, 2)
        self.assertEqual("[Square] (2) 2/1 - 2", str(dummy))

        #  Test with four arguments updated
        dummy.update(2, 2, 2, 2)
        self.assertEqual("[Square] (2) 2/2 - 2", str(dummy))

        #  Test with kwargs: id
        dummy.update(id=99)
        self.assertEqual("[Square] (99) 2/2 - 2", str(dummy))

        #  Test with kwargs: id, size
        dummy.update(id=99, size=1)
        self.assertEqual("[Square] (99) 2/2 - 1", str(dummy))

        #  Test with kwargs: id, size, x
        dummy.update(id=99, size=1, x=1)
        self.assertEqual("[Square] (99) 1/2 - 1", str(dummy))

        #  Test with kwargs: id, size, x, y
        dummy.update(id=99, size=1, x=1, y=1)
        self.assertEqual("[Square] (99) 1/1 - 1", str(dummy))

    def test_create(self):
        #  Test with kwargs: id
        try:
            obj = Square.create(id=89)
            self.assertEqual(obj.id, 89)
        except TypeError:
            self.fail("TypeError should not be raised")

        #  Test with kwargs: id, size
        try:
            obj = Square.create(id=89, size=1)
            self.assertEqual(obj.size, 1)
        except TypeError:
            self.assertEqual("TypeError should not be raised")

        #  Test with kwargs: id, size, x
        obj = Square.create(id=89, size=1, x=3)
        self.assertEqual(obj.x, 3)

        #  Test with kwargs: id, size, x, y
        obj = Square.create(id=89, size=1, x=3, y=4)
        self.assertEqual(obj.y, 4)

    def test_square_save_to_file(self):
        # Test when the list is None
        Square.save_to_file(None)
        expected_output = "[]"

        with open("Square.json", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_output)

        #  Test when list is []
        Square.save_to_file([])
        expected_output = "[]"

        with open("Square.json", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_output)

        #  Test when the list is not empty
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        expected_output = json.dumps([s1.to_dictionary(), s2.to_dictionary()])

        with open("Square.json", "r") as f:
            data = f.read()
        self.assertEqual(data, expected_output)

    def test_load_from_file(self):
        #  Test loading from a non-existing file
        path = "Square.json"
        if os.path.isfile(path):
            os.remove(path)

        instances = Square.load_from_file()
        self.assertEqual(instances, [])

        #  Test loading from the existing file
        test_data = [Square(1, 2).to_dictionary()]
        with open(path, 'w') as f:
            f.write(json.dumps(test_data))

        instances = Square.load_from_file()
        self.assertEqual(len(instances), len(test_data))
