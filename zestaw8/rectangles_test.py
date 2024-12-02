import pytest
from points import Point
from rectangles import Rectangle

def test_rectangle_creation():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.pt1 == Point(1, 2)
    assert rect.pt2 == Point(3, 4)

def test_rectangle_invalid_creation():
    with pytest.raises(ValueError):
        Rectangle(3, 4, 1, 2)

def test_rectangle_str():
    rect = Rectangle(1, 2, 3, 4)
    assert str(rect) == "[(1, 2), (3, 4)]"

def test_rectangle_repr():
    rect = Rectangle(1, 2, 3, 4)
    assert repr(rect) == "Rectangle(1, 2, 3, 4)"

def test_rectangle_equality():
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(1, 2, 3, 4)
    rect3 = Rectangle(0, 0, 1, 1)
    assert rect1 == rect2
    assert rect1 != rect3

def test_rectangle_from_points():
    rect = Rectangle.from_points([(1, 2), (3, 4)])
    assert rect == Rectangle(1, 2, 3, 4)

    rect = Rectangle.from_points([Point(1, 2), Point(3, 4)])
    assert rect == Rectangle(1, 2, 3, 4)

    with pytest.raises(ValueError):
        Rectangle.from_points([(1, 2)])

    with pytest.raises(TypeError):
        Rectangle.from_points([(1, 2), ('a', 'b')])

def test_rectangle_properties():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.center == Point(2, 3)
    assert rect.width == 2
    assert rect.height == 2
    assert rect.top == 4
    assert rect.bottom == 2
    assert rect.left == 1
    assert rect.right == 3
    assert rect.topleft == Point(1, 4)
    assert rect.topright == Point(3, 4)
    assert rect.bottomleft == Point(1, 2)
    assert rect.bottomright == Point(3, 2)

def test_rectangle_area():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.area() == 4

def test_rectangle_move():
    rect = Rectangle(1, 2, 3, 4)
    rect.move(1, 1)
    assert rect == Rectangle(2, 3, 4, 5)

def test_rectangle_intersection():
    rect1 = Rectangle(1, 1, 4, 4)
    rect2 = Rectangle(2, 2, 5, 5)
    intersection = rect1.intersection(rect2)
    assert intersection == Rectangle(2, 2, 4, 4)

    rect3 = Rectangle(5, 5, 6, 6)
    assert rect1.intersection(rect3) is None

def test_rectangle_cover():
    rect1 = Rectangle(1, 1, 4, 4)
    rect2 = Rectangle(2, 2, 5, 5)
    cover = rect1.cover(rect2)
    assert cover == Rectangle(1, 1, 5, 5)

def test_rectangle_make4():
    rect = Rectangle(0, 0, 4, 4)
    rects = rect.make4()
    assert rects[0] == Rectangle(0, 0, 2, 2)
    assert rects[1] == Rectangle(2, 0, 4, 2)
    assert rects[2] == Rectangle(0, 2, 2, 4)
    assert rects[3] == Rectangle(2, 2, 4, 4)