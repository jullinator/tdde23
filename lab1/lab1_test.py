import unittest
from lab1 import divide_by_three, max_of_three, max3

class TestLab1 (unittest.TestCase):
    def test_divide_by_three (self):
        self.assertEqual(False, divide_by_three(5))
        self.assertEqual(True, divide_by_three(6))

    def test_max_of_three(self):
        self.assertEqual(10, max_of_three(10, 5, 3))
        self.assertEqual(4, max_of_three(1, 2, 4))

    def test_max3 (self):
        self.assertEqual(10, max3(10, 5, 3))
        self.assertEqual(4, max3(1, 2, 4))

if __name__ == '__main__':
    unittest.main()