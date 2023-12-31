#!/usr/bin/python3


import unittest
import sys

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_' + sys.argv[1] + '.py')
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
