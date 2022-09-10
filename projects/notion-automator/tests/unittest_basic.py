import unittest
from tkinter.messagebox import NO


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector<x={self.x}, y={self.y}>"

    def __add__(self, other: "Vector"):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector"):
        return Vector(self.x - other.x, self.y - other.y)

    @property
    def props(self):
        return self.x, self.y

    def distance(self, other: "Vector"):
        result = (other.x**2 - self.x**2) + (other.y**2 - self.y**2)
        return abs(result)


class TestVector(unittest.TestCase):

    vec_a = None
    vec_b = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.vec_a = Vector(x=2, y=5)
        cls.vec_b = Vector(x=-1, y=2)

    def test_props(self):
        vector = Vector(1, 2)
        self.assertEqual(vector.props, (1, 2))

    def test_add(self):
        result = self.vec_a + self.vec_b
        self.assertTupleEqual(result.props, (1, 7))

    def test_sub(self):
        result = self.vec_a - self.vec_b
        self.assertTupleEqual(result.props, (3, 3))

    def test_distance(self):
        result = self.vec_a.distance(self.vec_b)
        self.assertEqual(result, 24)


if __name__ == '__main__':
    unittest.main(verbosity=2)
