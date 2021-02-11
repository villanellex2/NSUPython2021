import itertools
import math


class Vector:

    def __init__(self, n=1, coordinates=None):
        self.dimension = n
        if coordinates is None:
            self.vector = [0] * n
        else:
            self.vector = []
            cord_len = len(coordinates)
            if self.dimension > cord_len:
                for c in coordinates:
                    self.vector.append(c)
                delta = self.dimension - cord_len
                self.vector.extend([0] * delta)
            else:
                for i in range(0, self.dimension):
                    self.vector.append(coordinates[i])

    def to_string(self):
        return str(self.vector)

    def sum(self, v):
        a = self.vector
        b = v.vector
        res = [x + y for x, y in itertools.zip_longest(a, b, fillvalue=0)]
        return Vector(len(res), res)

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
