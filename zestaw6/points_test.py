from points import Point
import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.point1 = Point(0, 0)
        self.point2 = Point(1, 2)
        self.point3 = Point(-3, 4)
        self.point4 = Point(12, -2)
        self.point5 = Point(-3, -3)
        self.point6 = Point(5, 1)

    def test_str(self):
        self.assertEqual(str(self.point1), "(0, 0)")
        self.assertEqual(str(self.point2), "(1, 2)")
        self.assertEqual(str(self.point3), "(-3, 4)")

    def test_repr(self):
        self.assertEqual(repr(self.point4), "Point(12, -2)")
        self.assertEqual(repr(self.point5), "Point(-3, -3)")
        self.assertEqual(repr(self.point6), "Point(5, 1)")

    def test_eq(self):
        self.assertTrue(self.point1 == Point(0, 0))
        self.assertFalse(self.point2 == self.point3)
        self.assertFalse(self.point4 == self.point5)

    def test_ne(self):
        self.assertTrue(self.point2 != self.point3)
        self.assertTrue(self.point3 != self.point4)
        self.assertFalse(self.point5 != Point(-3, -3))

    def test_add(self):
        self.assertEqual(self.point1 + self.point2, Point(1, 2))
        self.assertEqual(self.point3 + self.point4, Point(9, 2))
        self.assertEqual(self.point5 + self.point6, Point(2, -2))

    def test_sub(self):
        self.assertEqual(self.point3 - self.point2, Point(-4, 2))
        self.assertEqual(self.point1 - self.point4, Point(-12, 2))
        self.assertEqual(self.point6 - self.point5, Point(8, 4))

    def test_mul(self):
        self.assertEqual(self.point3 * self.point2, 5)
        self.assertEqual(self.point1 * self.point4, 0)
        self.assertEqual(self.point6 * self.point5, -18)

    def test_cross(self):
        self.assertEqual(self.point1.cross(self.point2), 0)
        self.assertEqual(self.point3.cross(self.point4), -42)
        self.assertEqual(self.point5.cross(self.point6), 12)

    def test_length(self):
        self.assertEqual(self.point1.length(), 0)
        self.assertAlmostEqual(self.point2.length(), 2.236068, places=6)
        self.assertEqual(self.point3.length(), 5.0)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
