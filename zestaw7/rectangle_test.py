import unittest
from rectangle import Rectangle
from zestaw7.points import Point

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(0, 0, 4, 4)
        self.rect2 = Rectangle(1, 1, 5, 5)
        self.rect3 = Rectangle(3, 3, 2, 2)

    def test_str(self):
        self.assertEqual(str(self.rect1), "[(0, 0), (4, 4)]")
        self.assertEqual(str(self.rect2), "[(1, 1), (5, 5)]")
        self.assertEqual(str(self.rect3), "[(2, 2), (3, 3)]")

    def test_repr(self):
        self.assertEqual(repr(self.rect1), "Rectangle(0, 0, 4, 4)")
        self.assertEqual(repr(self.rect2), "Rectangle(1, 1, 5, 5)")
        self.assertEqual(repr(self.rect3), "Rectangle(2, 2, 3, 3)")

    def test_eq(self):
        self.assertTrue(self.rect1 == Rectangle(0, 0, 4, 4))
        self.assertFalse(self.rect1 == self.rect2)
        self.assertFalse(self.rect2 == self.rect3)

    def test_ne(self):
        self.assertTrue(self.rect1 != self.rect2)
        self.assertFalse(self.rect1 != Rectangle(0, 0, 4, 4))
        self.assertTrue(self.rect2 != self.rect3)

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2, 2))
        self.assertEqual(self.rect2.center(), Point(3, 3))
        self.assertEqual(self.rect3.center(), Point(2.5, 2.5))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 16)
        self.assertEqual(self.rect2.area(), 16)
        self.assertEqual(self.rect3.area(), 1)

    def test_move(self):
        self.rect1.move(1, 1)
        self.assertEqual(self.rect1, Rectangle(1, 1, 5, 5))
        self.rect2.move(-1, -1)
        self.assertEqual(self.rect2, Rectangle(0, 0, 4, 4))
        self.rect3.move(2, 2)
        self.assertEqual(self.rect3, Rectangle(4, 4, 5, 5))

    def test_intersection(self):
        self.assertEqual(self.rect1.intersection(self.rect2), Rectangle(1, 1, 4, 4))
        self.assertIsNone(self.rect1.intersection(Rectangle(5, 5, 6, 6)))
        self.assertEqual(self.rect2.intersection(self.rect3), Rectangle(2, 2, 3, 3))

    def test_cover(self):
        self.assertEqual(self.rect1.cover(self.rect2), Rectangle(0, 0, 5, 5))
        self.assertEqual(self.rect1.cover(self.rect3), Rectangle(0, 0, 4, 4))
        self.assertEqual(self.rect2.cover(self.rect3), Rectangle(1, 1, 5, 5))

    def test_make4(self):
        rects1 = self.rect1.make4()
        self.assertEqual(rects1[0], Rectangle(0, 0, 2, 2))
        self.assertEqual(rects1[1], Rectangle(2, 0, 4, 2))
        self.assertEqual(rects1[2], Rectangle(0, 2, 2, 4))
        self.assertEqual(rects1[3], Rectangle(2, 2, 4, 4))

        rects2 = self.rect2.make4()
        self.assertEqual(rects2[0], Rectangle(1, 1, 3, 3))
        self.assertEqual(rects2[1], Rectangle(3, 1, 5, 3))
        self.assertEqual(rects2[2], Rectangle(1, 3, 3, 5))
        self.assertEqual(rects2[3], Rectangle(3, 3, 5, 5))

        rects3 = self.rect3.make4()
        self.assertEqual(rects3[0], Rectangle(2, 2, 2.5, 2.5))
        self.assertEqual(rects3[1], Rectangle(2.5, 2, 3, 2.5))
        self.assertEqual(rects3[2], Rectangle(2, 2.5, 2.5, 3))
        self.assertEqual(rects3[3], Rectangle(2.5, 2.5, 3, 3))

if __name__ == '__main__':
    unittest.main()
