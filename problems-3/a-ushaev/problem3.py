#!/usr/bin/env python3

class Vector():
    def __init__(self, *args):
        if len(args) > 0:
            if isinstance(args[0], (tuple, list)):
                self._components = list(args[0])
            else:
                self._components = list(args)
        else:
            self._components = [0,0]

    def __str__(self):
        return str(self._components)

    def __repr__(self):
        return str(self._components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        return self._components[key]

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_vec = [el + other for el in self._components]
        else:
            new_vec = [el + other_el for el, other_el in zip(self._components, other)]
        return Vector(new_vec)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            new_vec = [el - other for el in self._components]
        else:
            new_vec = [el - other_el for el, other_el in zip(self._components, other)]
        return Vector(new_vec)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_vec = [el * other for el in self._components]
            return Vector(new_vec)
        else:
            dot_prod = sum(el * other_el for el, other_el in zip(self._components, other))
            return dot_prod

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self._components == other._components
    
if __name__ == '__main__':
    x = Vector(2,5,7)
    y = Vector([10,3,5])
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'x + y = {x + y}')
    print(f'x - y = {x - y}')
    print(f'x * 4 = {x * 4}')
    print(f'x * y = {x * y}')
    print(f'length of x is {len(x)}')
    print(f'x[2] = {x[2]}')