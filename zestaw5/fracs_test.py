from fracs import *
import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.frac1 = [2, 1]
        self.frac2 = [1, 3]
        self.frac3 = [4, 5]
        self.frac4 = [-1, 2]
        self.frac5 = [1, -2]
        self.frac6 = [5, -6]
        self.frac7 = [3, -1]
    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac(self.zero, self.frac1), [2, 1])
        self.assertEqual(add_frac(self.frac2, self.frac4), [-1, 6])


    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.frac3, self.frac2), [7, 15])
        self.assertEqual(sub_frac(self.frac5, self.frac4), [0, 1])
        self.assertEqual(sub_frac(self.frac1, self.zero), [2, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.frac1, self.frac2), [2, 3])
        self.assertEqual(mul_frac(self.frac4, self.frac3), [-2, 5])
        self.assertEqual(mul_frac(self.frac5, self.frac7), [3, 2])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.frac1, self.frac2), [6, 1])
        self.assertEqual(div_frac(self.frac3, self.frac4), [-8, 5])
        self.assertEqual(div_frac(self.frac5, self.frac6), [3, 5])

    def test_is_positive(self):
        self.assertTrue(is_positive(self.frac1))
        self.assertFalse(is_positive(self.frac4))
        self.assertFalse(is_positive(self.frac5))
        self.assertTrue(is_positive(self.frac3))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero(self.frac1))
        self.assertFalse(is_zero(self.frac2))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.frac1, self.frac2), 1)
        self.assertEqual(cmp_frac(self.frac4, self.frac5), 0)
        self.assertEqual(cmp_frac(self.frac3, self.frac1), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float(self.frac1), 2.0)
        self.assertAlmostEqual(frac2float(self.frac3), 0.8)
        self.assertAlmostEqual(frac2float(self.frac4), -0.5)
        self.assertAlmostEqual(frac2float(self.frac7), -3)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy


