from buckets import Buckets
from fixed_buckets import FixedBuckets
import unittest


class TestBuckets(unittest.TestCase):
    def test_init(self):
        b = Buckets(5, 2)
        self.assertEqual(b.buckets, [2, 2, 2, 2, 2])

        a = Buckets(5, [])
        self.assertEqual(a.buckets, [[], [], [], [], []])

    def test_add(self):
        a = Buckets(5, [])
        self.assertEqual(a.buckets, [[], [], [], [], []])
        a.add(1, 1)
        self.assertNotEqual(a.buckets, [[], [1], [], [], []])  # ERROR, при передачи default == [], и повторении
        # списка ([value] * N) все получившиеся списки связаны - при добавлении в один из списков, происходит
        # добавление во все

        a.add(1, 2)
        self.assertEqual(a.buckets, [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]])

    def test_find(self):
        a = Buckets(5, [])
        a.add(1, 1)
        a.add(1, 2)
        self.assertNotEqual(a.find(0, 1), False)
        self.assertNotEqual(a.find(0, 2), False)
        self.assertNotEqual(a.find(3, 2), False)

    def test_clear(self):
        a = Buckets(5, [])
        a.add(1, 1)
        a.add(1, 2)
        a.clear(0)
        self.assertNotEqual(a.buckets, [[], [1, 2], [1, 2], [1, 2], [1, 2]])  # ERROR, default значение изменяется при
        # изменении корзин + присваивается ссылка на default, а не значение default - при добавление в очищенную
        # корзину элемента, он добавиться во все очищенные корзины
        a.add(0, 3)
        a.clear(2)
        self.assertEqual(a.buckets, [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])

    def test_fixed_buckets(self):
        c = FixedBuckets(5, 2)
        self.assertEqual(c.buckets, [2, 2, 2, 2, 2])


        c = FixedBuckets(5, [])

        self.assertEqual(c.buckets, [[], [], [], [], []])

        c.add(0, 1)
        self.assertEqual(c.buckets, [[1], [], [], [], []])
        c.add(1, 14)
        self.assertEqual(c.buckets, [[1], [14], [], [], []])
        c.add(4, 28)
        self.assertEqual(c.buckets, [[1], [14], [], [], [28]])
        c.clear(1)
        c.clear(4)
        self.assertEqual(c.buckets, [[1], [], [], [], []])
        #
        c.add(3, 16)
        self.assertEqual(c.buckets, [[1], [], [], [16], []])
        #
        c.add(2, 7)
        c.add(1, 6)
        self.assertEqual(c.buckets, [[1], [6], [7], [16], []])

        c = FixedBuckets(5, [1, 2, 3])
        self.assertEqual(c.buckets, [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
        c.add(0, 1)
        self.assertEqual(c.buckets, [[1, 2, 3, 1], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
        c.add(1, 14)
        self.assertEqual(c.buckets, [[1, 2, 3, 1], [1, 2, 3, 14], [1, 2, 3], [1, 2, 3], [1, 2, 3]])
        c.add(4, 28)
        self.assertEqual(c.buckets, [[1, 2, 3, 1], [1, 2, 3, 14], [1, 2, 3], [1, 2, 3], [1, 2, 3, 28]])
        c.clear(1)
        c.clear(4)
        self.assertEqual(c.buckets, [[1, 2, 3, 1], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])

        c.add(3, 16)
        self.assertEqual(c.buckets, [[1, 2, 3, 1], [1, 2, 3], [1, 2, 3], [1, 2, 3, 16], [1, 2, 3]])
        c.add(2, 7)
        c.add(1, 6)
        self.assertEqual(c.buckets, [[1, 2, 3, 1], [1, 2, 3, 6], [1, 2, 3, 7], [1, 2, 3, 16], [1, 2, 3]])

        self.assertEqual(c.find(2, 1), True)
        self.assertEqual(c.find(4, 666), False)

        l = [6, 6, 6]
        c.add(4, l)
        self.assertEqual(c.buckets, [[1, 2, 3, 1], [1, 2, 3, 6], [1, 2, 3, 7], [1, 2, 3, 16], [1, 2, 3, [6, 6, 6]]])

        l.append(7)
        self.assertEqual(c.buckets, [[1, 2, 3, 1], [1, 2, 3, 6], [1, 2, 3, 7], [1, 2, 3, 16], [1, 2, 3, [6, 6, 6, 7]]])


unittest.main()
