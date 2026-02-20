from coe_number.two_characters import alternate
import unittest


class TestAlternate(unittest.TestCase):
    def test_alternate(self):
        self.assertEqual(alternate("beabeefeab"), 5)
        self.assertEqual(alternate("abaacdabd"), 4)
        self.assertEqual(alternate("asdcbsdcagfsdbgdfanfghbsfdab"), 8)

    def test_edge_cases(self):
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate("aa"), 0)
        self.assertEqual(alternate("ab"), 2)

    def test_invalid_input_types(self):
        self.assertEqual(alternate(12345), "Invalid Input")
        self.assertEqual(alternate(None), "Invalid Input")
        self.assertEqual(alternate(["a", "b", "c"]), "Invalid Input")
        self.assertEqual(alternate({"a": 1, "b": 2, "c": 3}), "Invalid Input")
        self.assertEqual(alternate((1, 2, 3)), "Invalid Input")
        self.assertEqual(alternate(True), "Invalid Input")
        self.assertEqual(alternate(False), "Invalid Input")

    def test_out_of_range_input(self):
        self.assertEqual(alternate("a" * 1001), "Out of Range")
        self.assertEqual(alternate(""), "Out of Range")
        self.assertEqual(alternate("a" * 1000), 0)
