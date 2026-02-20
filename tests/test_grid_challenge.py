from coe_number.grid_challenge import gridChallenge
import unittest


class TestGridChallenge(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(
            gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES"
        )
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")
        self.assertEqual(gridChallenge(["abc", "fed", "ghi"]), "YES")
        self.assertEqual(gridChallenge(["a", "b", "c"]), "YES")
        self.assertEqual(gridChallenge(["cba", "fed", "ihg"]), "YES")

    def test_edge_cases(self):
        self.assertEqual(gridChallenge([]), "YES")
        self.assertEqual(gridChallenge(["a"]), "YES")

    def test_invalid_cases(self):
        self.assertEqual(gridChallenge(["abc", "def", 123]), "Not String")
        self.assertEqual(gridChallenge(["abc", "def", "GHI"]), "Not Lowercase")
        self.assertEqual(gridChallenge(["abc", "def", "ghi!"]), "Not Lowercase")
        self.assertEqual(gridChallenge([123, "def", "ghi"]), "Not String")
        self.assertEqual(gridChallenge(["abc", 123, "ghi"]), "Not String")
        self.assertEqual(gridChallenge(["abc", "def", None]), "Not String")
        self.assertEqual(gridChallenge(["abc", "def", []]), "Not String")
        self.assertEqual(gridChallenge(["abc", "def", {}]), "Not String")
        self.assertEqual(gridChallenge(["abc", "def", ()]), "Not String")
        self.assertEqual(gridChallenge(["abc", "def", True]), "Not String")
        self.assertEqual(gridChallenge(["abc", "def", False]), "Not String")
