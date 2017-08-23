# coding=utf-8
import unittest
from kombinatorik import fakultet, permutationer, kombinationer

class TestKombinatorik(unittest.TestCase):
    def test_fakultet(self):
        self.assertEqual(fakultet(0), 1)
        self.assertEqual(fakultet(1), 1)
        self.assertEqual(fakultet(3), 6)
        self.assertEqual(fakultet(4), 24)

    def test_permutationer(self):
        self.assertEqual(permutationer(2, 2), 2)
        self.assertEqual(permutationer(4, 2), 12)

    def test_kombinationer(self):
        self.assertEqual(kombinationer(5,3), kombinationer(5,2))
        self.assertEqual(kombinationer(5, 2), 10)

    def test_u54(self):
        """På hur många sätt kan A,B,C,D,E,F permuteras?"""
        string = "ABCDEF"
        a = fakultet(len(string))
        b = fakultet(len(string)-1)
        self.assertEqual(a, fakultet(6))
        self.assertEqual(b, fakultet(5))


if __name__ == '__main__':
    unittest.main()