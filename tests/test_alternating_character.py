from coe_number.alternating_character import alternatingCharacters
import unittest


class TestAlternatingCharacters(unittest.TestCase):
    def test_alternatingCharacters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)
        self.assertEqual(alternatingCharacters(""), "Out of Range")
        self.assertEqual(alternatingCharacters("A" * 100001), "Out of Range")
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("B"), 0)
        self.assertEqual(alternatingCharacters("ABABABABA"), 0)
        self.assertEqual(alternatingCharacters("ABABABABB"), 1)

    def test_alternatingCharacters_invalid_input(self):
        self.assertEqual(alternatingCharacters(123), "Not String")
        self.assertEqual(alternatingCharacters(None), "Not String")
        self.assertEqual(alternatingCharacters([]), "Not String")
        self.assertEqual(alternatingCharacters({}), "Not String")
        self.assertEqual(alternatingCharacters("A1B2C3"), "Invalid Input")
        self.assertEqual(alternatingCharacters("ABABABAB1"), "Invalid Input")
        self.assertEqual(alternatingCharacters("ABABABAB!"), "Invalid Input")
        self.assertEqual(alternatingCharacters("ABABABAB@"), "Invalid Input")
        self.assertEqual(alternatingCharacters("abababab#"), "Invalid Input")
