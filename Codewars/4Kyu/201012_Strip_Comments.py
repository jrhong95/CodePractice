import re
import unittest


def strip_comments(string,markers):
    if markers == []:
        return string
    return "\n".join(re.split("|".join("\\" + m for m in markers), line)[0].rstrip() for line in string.split('\n'))


class Test_Strip_Comments(unittest.TestCase):
    def test_strip_comments_with_regular_string(self):
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
    def test_strip_comments_with_no_markers(self):
        self.assertEqual(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", []), "apples, pears # and bananas\ngrapes\nbananas !apples")


if __name__ == '__main__':
    unittest.main()
    