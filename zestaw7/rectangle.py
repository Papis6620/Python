from zestaw7.points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 > x2 or y1 > y2: raise ValueError("Metoda wymaga dwóch punktów(lewy dolny i prawy górny)")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):              # "[(x1, y1), (x2, y2)]"
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
        return  f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):        # obsługa rect1 == rect2
        return {self.pt1, self.pt2} == {other.pt1, other.pt2}

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):               # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):                 # pole powierzchni
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y)

    def move(self, x, y):           # przesunięcie o (x, y)
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)

    def intersection(self, other):  # część wspólna prostokątów
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        else:
            return None

    def cover(self, other):         # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):                # zwraca krotkę czterech mniejszych
        center = self.center()

        rect1 = Rectangle(self.pt1.x, self.pt1.y, center.x, center. y)
        rect2 = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
        rect3 = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        rect4 = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)

        return rect1, rect2, rect3, rect4
