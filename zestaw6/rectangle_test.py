import unittest
from points import Point
from rectangle import Rectangle

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(0, 0, 0, 0)
        self.rect2 = Rectangle(1, 2, 3, 4)
        self.rect3 = Rectangle(4, 3, 2, 1)
        self.rect4 = Rectangle(2, 2, 0, 0)
        self.rect5 = Rectangle(-2, -2, 2, 2)
        self.rect6 = Rectangle(-3, 1, 1, -3)

    def test_str(self):
        self.assertEqual(str(self.rect1), "[(0, 0), (0, 0)]")
        self.assertEqual(str(self.rect2), "[(1, 2), (3, 4)]")
        self.assertEqual(str(self.rect3), "[(4, 3), (2, 1)]")

    def test_repr(self):
        self.assertEqual(repr(self.rect4), "Rectangle(2, 2, 0, 0)")
        self.assertEqual(repr(self.rect5), "Rectangle(-2, -2, 2, 2)")
        self.assertEqual(repr(self.rect6), "Rectangle(-3, 1, 1, -3)")

    def test_eq(self):
        self.assertTrue(self.rect2 == Rectangle(1, 2, 3, 4))
        self.assertFalse(self.rect2 == self.rect3)
        self.assertTrue(self.rect4 == Rectangle(2, 2, 0, 0))

    def test_ne(self):
        self.assertTrue(self.rect1 != self.rect2)
        self.assertFalse(self.rect3 != Rectangle(4, 3, 2, 1))
        self.assertTrue(self.rect5 != self.rect6)

    def test_center(self):
        self.assertEqual(self.rect2.center(), Point(2, 3))
        self.assertEqual(self.rect5.center(), Point(0, 0))
        self.assertEqual(self.rect6.center(), Point(-1, -1))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 0)
        self.assertEqual(self.rect2.area(), 4)
        self.assertEqual(self.rect5.area(), 16)

    def test_move(self):
        self.rect2.move(1, 1)
        self.assertEqual(self.rect2, Rectangle(2, 3, 4, 5))

        self.rect5.move(-1, -1)
        self.assertEqual(self.rect5, Rectangle(-3, -3, 1, 1))

        self.rect6.move(10, -5)
        self.assertEqual(self.rect6, Rectangle(7, -4, 11, -8))

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
