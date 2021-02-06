import itertools
import math


class Vector:

    def __init__(self, n=1, coordinates=None):
        if coordinates is None:
            self.vector = [0] * n
        else:
            self.vector = []
            for c in coordinates:
                self.vector.append(c)
        self.dimension = n
        v_length = len(self.vector)
        if v_length < self.dimension:
            delta = self.dimension - v_length
            self.vector.extend([0] * delta)

    def to_string(self):
        return str(self.vector)

    def sum(self, v):
        a = self.vector
        b = v.vector
        res = [x + y for x, y in itertools.zip_longest(a, b, fillvalue=0)]
        return Vector(self.dimension, res)

    def sub(self, v):
        a = self.vector
        b = v.vector
        res = [x - y for x, y in itertools.zip_longest(a, b, fillvalue=0)]
        return Vector(self.dimension, res)

    def constant_product(self, const):
        res = []
        for c in self.vector:
            res.append(c * const)
        return Vector(self.dimension, res)

    def scalar_product(self, v):
        a = self.vector
        b = v.vector
        return sum([x * y for x, y in itertools.zip_longest(a, b, fillvalue=0)])

    def equals_to(self, v):
        a = self.vector
        b = v.vector
        return all(c_1 == c_2 for c_1, c_2 in itertools.zip_longest(a, b))

    def get_length(self):
        s = sum(x ** 2 for x in self.vector)
        return math.sqrt(s)

    def get_coordinate(self, n):
        return self.vector[n]
