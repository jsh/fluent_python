#!/usr/bin/env python
"""Demo infix operators, bool, abs, repr."""

from math import hypot


class Vector:
    """Vectors."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def magnitude(self):
        """Length of the vector.
        :returns: length
        :rtype: float
        """
        return abs(self)


def main():
    """Everything interesting."""
    v_00 = Vector(0, 0)
    v_23 = Vector(2, 3)
    v_45 = Vector(4, 5)
    print(v_23)
    print("[2, 3] is ", bool(v_23))
    print("[0, 0] is ", bool(v_00))
    print("[2, 3] + [4, 5] = ", v_23 + v_45)
    print("[2, 3] * 10 = ", v_23 * 10)
    print("magnitude of Vector(3,4) is ", Vector(3, 4).magnitude())


if __name__ == "__main__":
    main()
