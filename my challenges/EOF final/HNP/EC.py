from __future__ import division
from Crypto.Util.number import inverse

class EC(object):

    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def __eq__(self, other):

        if isinstance(other, EC):
            return(
                self.p == other.p
                and self.a == other.a
                and self.b == other.b
            )
        return NotImplemented
    
    def contains_point(self, x, y):
        return (y * y - ((x * x + self.a) * x + self.b)) % self.p == 0


class Point(object):

    def __init__(self, curve, x, y, order=None):

        self.curve = curve
        self.x = x
        self.y = y
        self.order = order

        if self.curve:
            assert self.curve.contains_point(x, y)

        if curve and order:
            assert self * order == INFINITY

    def __eq__(self, other):

        if isinstance(other, Point):
            return (
                self.curve == other.curve
                and self.x == other.x
                and self.y == other.y
            )
        return NotImplemented
    
    def __add__(self, other):

        if not isinstance(other, Point):
            return NotImplemented
        if other == INFINITY:
            return self
        if self == INFINITY:
            return other
        assert self.curve == other.curve
        if self.x == other.x:
            if (self.y + other.y) % self.curve.p == 0:
                return INFINITY
            else:
                return self.double()

        p = self.curve.p
        l = ((other.y - self.y) * inverse(other.x - self.x, p)) % p
        x3 = (l * l - self.x - other.x) % p
        y3 = (l * (self.x - x3) - self.y) % p

        return Point(self.curve, x3, y3)

    def __neg__(self):

        return Point(self.curve, self.x, self.curve.p - self.y)

    def __mul__(self, other):

        def leftmost_bit(x):
            assert x > 0
            result = 1
            while result <= x:
                result = 2 * result
            return result //2

        e = other
        if e == 0 or (self.order and e % self.order == 0):
            return INFINITY
        if self == INFINITY:
            return INFINITY
        if e < 0:
            return (-self) * (-e)

        e3 = 3 * e
        negative_self = Point(self.curve, self.x, -self.y, self.order)
        i = leftmost_bit(e3) // 2
        result = self
        while i > 1:
            result = result.double()
            if (e3 & i) != 0 and (e & i) == 0:
                result = result + self
            if (e3 & i) == 0 and (e & i) != 0:
                result = result + negative_self
            i = i // 2

        return result

    def __rmul__(self, other):
            
        return self * other

    def double(self):

        if self == INFINITY:
            return INFINITY

        p = self.curve.p
        a = self.curve.a
        l = ((3 * self.x * self.x + a) * inverse(2 * self.y, p)) % p
        x3 = (l * l - 2 * self.x) % p
        y3 = (l * (self.x - x3) - self.y) % p

        return Point(self.curve, x3, y3)

INFINITY = Point(None, None, None)
