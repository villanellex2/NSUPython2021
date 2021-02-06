import unittest
from Vector import Vector


class TestVector(unittest.TestCase):

    def test_init(self):
        vector = Vector(3, [4.5, 10])
        vector1 = Vector(4, [4])
        self.assertEqual(vector.vector, [4.5, 10, 0])
        self.assertEqual(vector1.vector, [4, 0, 0, 0])

    def test_sum(self):
        vector = Vector(3, [4.5, 10, 56])
        vector1 = Vector(3, [4, 11.3, -50.4])
        self.assertEqual(vector.sum(vector1).vector, [8.5, 21.3, 5.600000000000001])

        vector = Vector(3, [-3, 10, 506])
        vector1 = Vector(3, [4, -11, 50])
        self.assertEqual(vector.sum(vector1).vector, [1, -1, 556])

        vector = Vector(3, [4, 10, 50])
        vector1 = Vector(3, [4, 10, 50])
        self.assertEqual(vector.sum(vector1).vector, [8, 20, 100])

        vector = Vector(3, [4.5, 10])
        vector1 = Vector(4, [4])

        self.assertEqual(vector.sum(vector1).vector, [8.5, 10, 0, 0])

    def test_sub(self):
        vector = Vector(3, [4, 10, 56])
        vector1 = Vector(3, [4, 11, 50])
        self.assertEqual(vector.sub(vector1).vector, [0, -1, 6])

        vector = Vector(3, [4, 10, 50])
        vector1 = Vector(3, [4, 10, 50])
        self.assertEqual(vector.sub(vector1).vector, [0, 0, 0])

        vector = Vector(3, [-3, 10, 506])
        vector1 = Vector(3, [4, -11, 50])

        self.assertEqual(vector.sub(vector1).vector, [-7, 21, 456])

    def test_constant_product(self):
        vector = Vector(3, [4, 10, 56])
        self.assertEqual(vector.constant_product(5).vector, [20, 50, 280])

        vector = Vector(3, [-3, 10, 506])
        self.assertEqual(vector.constant_product(5).vector, [-15, 50, 2530])

        vector = Vector(3, [4, 10, 50])
        self.assertEqual(vector.constant_product(5).vector, [20, 50, 250])

        vector = Vector(3)
        self.assertEqual(vector.constant_product(5).vector, [0, 0, 0])

    def test_scalar_product(self):
        vector = Vector(3, [4, 10, 56])
        vector1 = Vector(3, [4, 11, 50])
        self.assertEqual(vector.scalar_product(vector1), 2926)

        vector = Vector(3, [4, 10, 50])
        vector1 = Vector(3, [4, 10, 50])
        self.assertEqual(vector.scalar_product(vector1), 2616)

        vector = Vector(3, [-3, 10, 506])
        vector1 = Vector(3, [4, -11, 50])
        self.assertEqual(vector.scalar_product(vector1), 25178)

    def test_equals(self):
        vector = Vector(3, [4, 10, 56])
        vector1 = Vector(3, [4, 11, 50])
        self.assertEqual(vector.equals_to(vector1), False)

        vector = Vector(3, [4, 10, 50])
        vector1 = Vector(3, [4, 10, 50])
        self.assertEqual(vector.equals_to(vector1), True)

        vector = Vector(3, [-3, 10, 506])
        vector1 = Vector(3, [4, -11, 50])
        self.assertEqual(vector.equals_to(vector1), False)

    def test_get_length(self):
        vector = Vector(3, [4, 10, 56])
        self.assertEqual(vector.get_length(), 57.02630971753301)

        vector = Vector(3, [-3, 10, 506])
        self.assertEqual(vector.get_length(), 506.10769604897337)

        vector = Vector(3, [4, 10, 50])
        self.assertEqual(vector.get_length(), 51.146847410177685)

    def test_get_coordinate(self):
        vector = Vector(3, [4, 10, 56])
        self.assertEqual(vector.get_coordinate(1), 10)

        vector = Vector(3, [-3, 10, 506])
        self.assertEqual(vector.get_coordinate(0), -3)

        vector = Vector(3, [4, 10, 50])
        self.assertEqual(vector.get_coordinate(2), 50)


if __name__ == "__main__":
    unittest.main()