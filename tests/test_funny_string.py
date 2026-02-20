from coe_number.funny_string import funnyString
import unittest


class TestFunnyString(unittest.TestCase):
    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        self.assertEqual(funnyString("abc"), "Funny")
        self.assertEqual(funnyString("abcd"), "Funny")
        self.assertEqual(funnyString("lmnop"), "Funny")
        self.assertEqual(funnyString(""), "Out of Range")
        self.assertEqual(funnyString("a"), "Out of Range")
        self.assertEqual(funnyString("ab"), "Funny")
        self.assertEqual(funnyString("za"), "Funny")
        self.assertEqual(funnyString("aaaaa"), "Funny")
        self.assertEqual(funnyString("racecar"), "Funny")
        self.assertEqual(funnyString("abcdefghijklmnopqrstuvwxyz"), "Funny")
        self.assertEqual(funnyString("abcdefghijklmnopqrstuvwxyza"), "Not Funny")
        self.assertEqual(funnyString("abde"), "Funny")
        self.assertEqual(funnyString("abgij"), "Not Funny")
        self.assertEqual(funnyString("acdxz"), "Not Funny")

    def test_funny_string_special_characters(self):
        self.assertEqual(funnyString("a!b@c"), "Not Funny")
        self.assertEqual(funnyString("!@#"), "Not Funny")
        self.assertEqual(funnyString("@!@"), "Funny")
        self.assertEqual(funnyString("a$c"), "Not Funny")

    def test_funny_string_non_string_input(self):
        self.assertEqual(funnyString(123), "Not String")
        self.assertEqual(funnyString(None), "Not String")
        self.assertEqual(funnyString(3.14), "Not String")
        self.assertEqual(funnyString([]), "Not String")
        self.assertEqual(funnyString({}), "Not String")
        self.assertEqual(funnyString(()), "Not String")
        self.assertEqual(funnyString(True), "Not String")
