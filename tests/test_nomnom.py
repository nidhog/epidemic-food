"""This file contains the basic tests for the nomnom module
"""
import unittest
# adding nomnom path to PYTHONPATH
import sys, os
nomnom_path = os.path.dirname(os.getcwd())
sys.path.append(nomnom_path)
from nomnom import foodstore


class BasicTest(unittest.TestCase):
    def test_instantiation(self):
        fs = foodstore.FoodStore()


if __name__ == '__main__':
    unittest.main()


