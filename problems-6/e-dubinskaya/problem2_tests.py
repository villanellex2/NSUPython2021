import problem2 as p2
import unittest


class TestCalculator(unittest.TestCase):
    def test_1(self):
        baseball = "Traditionally, the pitcher also bats." + \
                   "Starting in 1973 with the https://en.wikipedia.org/wiki/American_League and spreading to further" \
                   " leagues throughout the 1980s and 1990s, the hitting duties of the pitcher have " \
                   "generally been given over to the position of https://en.wikipedia.org/wiki/Designated_hitter a cause of some" \
                   " controversy. https://en.wikipedia.org/wiki/National_League in https://en.wikipedia.org/wiki/Major_League_Baseball" \
                   " although it was adopted " \
                   "for the 2020 season, and the Japanese Central League are among the remaining leagues " \
                   "that have not adopted the designated hitter position."
        self.assertEqual(p2.find_all_link(baseball),
                         ["https://en.wikipedia.org/wiki/American_League",
                          "https://en.wikipedia.org/wiki/Designated_hitter",
                          "https://en.wikipedia.org/wiki/National_League",
                          "https://en.wikipedia.org/wiki/Major_League_Baseball"])

    def test_2(self):
        wifi = "Видеонаблюдение 24*7 из любой точки мира! http://www.enforta.ru или это было www.enforta.ru ?" \
               "или httpt://www.enforta.ru/ ? Ну ладно, не будем отвлакаться на глупости и вернемся к бейсболу: " \
               "https://en.wikipedia.org/wiki/Division_Series"
        self.assertEqual(p2.find_all_link(wifi),
                         ["http://www.enforta.ru",
                          "www.enforta.ru",
                          "https://en.wikipedia.org/wiki/Division_Series"])

    def test_3(self):
        lalala = "https://www.youtube.com/watch?v=d35pHYwgVpg http://www.youtube.com/watch?v=d35pHYwgVpg " \
                 "htt://www.youtube.com/watch?v=d35pHYwgVpg https://www.youtube.com\watch?v=d35pHYwgVpg " \
                 "https://www.youtube.com{}watch?v=d35pHYwgVpg https://www.youtube.com/watch?v=d35pHYwgVpg♀# " \
                 "www.youtube.com"
        self.assertEqual(p2.find_all_link(lalala),
                         ["https://www.youtube.com/watch?v=d35pHYwgVpg",
                          "http://www.youtube.com/watch?v=d35pHYwgVpg",
                          "www.youtube.com"])


if __name__ == "__main__":
    unittest.main()
