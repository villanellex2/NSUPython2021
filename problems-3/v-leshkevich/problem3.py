class Vector:
    def __init__(self, *args):
        if len(args) == 0:
            self.values = (0, 0)
        elif isinstance(args[0], (list, tuple)):
            self.values = args[0]
        else:
            self.values = args

    def __add__(self, other):
        if isinstance(other, Vector):
            result = tuple(x + y for x, y in zip(self.values, other.values))
        elif isinstance(other, (int, float)):
            result = tuple(x + other for x in self.values)
        else:
            raise ValueError("Can not add with type {}".format(type(other)))
        return self.__class__(*result)

    def __radd__(self, other):
        return self.__class__(other)

    def __iadd__(self, other):
        return self.__class__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            result = tuple(x - y for x, y in zip(self.values, other.values))
        elif isinstance(other, (int, float)):
            result = tuple(x - other for x in self.values)
        else:
            raise ValueError("Can not subtract with type {}".format(type(other)))
        return self.__class__(*result)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum(x * y for x, y in zip(self.values, other.values))
        elif isinstance(other, (int, float)):
            result = tuple(x * other for x in self.values)
            return self.__class__(*result)
        else:
            raise ValueError("Can not multiply with type {}".format(type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.values == other.values

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return 'Vector({args})'.format(args=self.values)

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)
