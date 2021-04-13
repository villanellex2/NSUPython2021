import problem2 as p2
import unittest


class TestCalculator(unittest.TestCase):
    def test_1(self):
        f = open("res/en_dictionary.txt", 'r')
        result = p2.createDictionary(f.read())
        actual = "baca - fruit\n" + \
                 "bacca - fruit\n" + \
                 "malum - apple, punishment\n" + \
                 "multa - punishment\n" + \
                 "pomum - apple\n" + \
                 "popula - apple\n" + \
                 "popum - fruit\n"
        self.assertEqual(result, actual)
        f.close()

    def test_2(self):
        f = open("res/en_dictionary2.txt", 'r')
        result = p2.createDictionary(f.read())
        actual = "bow - luk, bant, duga\n" + \
                 "knot - bant\n" + \
                 "onion - luk, lukovica\n"
        self.assertEqual(result, actual)
        f.close()


if __name__ == "__main__":
    unittest.main()
