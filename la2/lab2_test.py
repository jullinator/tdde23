import unittest
from la2 import check_pnr

personal_id_ok = [7, 4, 0, 2, 1, 7, 4, 8, 2, 0]
personal_id_fail = [7, 4, 0, 2, 1, 7, 4, 8, 2, 1]

class TestLab1 (unittest.TestCase):
    def test_check_pnr (self):
        self.assertEqual(True, check_pnr(personal_id_ok))
        self.assertEqual(False, check_pnr(personal_id_fail))




if __name__ == '__main__':
    unittest.main()