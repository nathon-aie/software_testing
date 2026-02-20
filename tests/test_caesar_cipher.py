from coe_number.caesar_cipher import caesarCipher
import unittest


class TestcaesarCipher(unittest.TestCase):
    def test_caesarCipher(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")
        self.assertEqual(
            caesarCipher("abcdefghijklmnopqrstuvwxyz", 3), "defghijklmnopqrstuvwxyzabc"
        )
        self.assertEqual(
            caesarCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2), "CDEFGHIJKLMNOPQRSTUVWXYZAB"
        )
        self.assertEqual(caesarCipher("a", 1), "b")
        self.assertEqual(caesarCipher("z", 1), "a")
        self.assertEqual(caesarCipher("a", 26), "a")
        self.assertEqual(caesarCipher("z", 26), "z")
        self.assertEqual(caesarCipher("a", 0), "a")
        self.assertEqual(
            caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 5),
            "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj",
        )

    def test_caesarCipher_invalid_input(self):
        self.assertEqual(caesarCipher(123, 2), "Invalid Input")
        self.assertEqual(caesarCipher("middle-Outz", "2"), "Invalid Input")
        self.assertEqual(caesarCipher(None, 2), "Invalid Input")
        self.assertEqual(caesarCipher("middle-Outz", None), "Invalid Input")
        self.assertEqual(caesarCipher([], 2), "Invalid Input")
        self.assertEqual(caesarCipher("middle-Outz", []), "Invalid Input")
        self.assertEqual(caesarCipher({}, 2), "Invalid Input")
        self.assertEqual(caesarCipher("middle-Outz", {}), "Invalid Input")
        self.assertEqual(caesarCipher("middle-Outz", -1), "Out of Range")
        self.assertEqual(caesarCipher("middle-Outz", 101), "Out of Range")
        self.assertEqual(caesarCipher("", 2), "Out of Range")
        self.assertEqual(caesarCipher("a", -1), "Out of Range")
        self.assertEqual(caesarCipher("a", 101), "Out of Range")
