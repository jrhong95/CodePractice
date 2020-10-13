import unittest


def who_is_next(names, r):
    r -= 1
    name_len = len(names)
    while r >= name_len:
        r = (r - name_len) // 2
    return names[r]


name = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

class TestWhoIsNext(unittest.TestCase):
    def test_who_is_next_with_small_int(self):
        self.assertEqual(who_is_next(name, 1), "Sheldon")
    def test_who_is_next_with_big_int(self):
        self.assertEqual(who_is_next(name, 7230702951), "Leonard")


if __name__ == '__main__':
    unittest.main()
    