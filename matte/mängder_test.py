# coding=utf-8
import unittest
from mängder import union

class TestKombinatorik(unittest.TestCase):
    def test_union(self):

        self.assertEqual([[1,4,5],[1,2,3,4]], [1,2,3,4,5])



if __name__ == '__main__':
    unittest.main()