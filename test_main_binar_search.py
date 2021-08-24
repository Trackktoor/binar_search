import unittest
from main_binar_search import binar_search


class TestBinarySearch(unittest.TestCase):
    def test_value(self):
        self.assertEqual(binar_search(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(binar_search(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
        self.assertEqual(binar_search(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(binar_search(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)

    def test_types(self):
        self.assertRaises(TypeError, binar_search, 'str')
        self.assertRaises(ValueError, binar_search, 10, [[]])

if __name__ == '__main__':
    unittest.main()