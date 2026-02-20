from coe_number.staircase import staircase
import unittest


class TestStaircase(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        # arrange
        n = 2
        pattern = "#"
        expected_output = " #\n##"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output, result, f"Should be {expected_output}")

    def test_give_2_with_AAA_should_be_invalid_input(self):
        # arrange
        n = 2
        pattern = "AAA"
        expected_output = "Invalid Input"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output, result, f"Should be {expected_output}")

    def test_give_0_with_hash_should_be_hh(self):
        # arrange
        n = 0
        pattern = "#"
        expected_output = ""
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output, result, f"Should be {expected_output}")

    def test_give_minus_1_with_hash_should_be_out_of_range(self):
        # arrange
        n = -1
        pattern = "#"
        expected_output = "Out of Range"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output, result, f"Should be {expected_output}")

    def test_give_30_with_hash_should_be_out_of_range(self):
        # arrange
        n = 30
        pattern = "#"
        expected_output = "Out of Range"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output, result, f"Should be {expected_output}")

    def test_give_str0_with_hash_should_be_invalid_input(self):
        # arrange
        n = "0"
        pattern = "#"
        expected_output = "Invalid Input"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output, result, f"Should be {expected_output}")

    def test_give_null_with_hash_should_be_invalid_input(self):
        # arrange
        n = None
        pattern = "#"
        expected_output = "Invalid Input"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output, result, f"Should be {expected_output}")

    def test_give_10_with_hash_should_be_hh(self):
        # arrange
        n = 10
        pattern = "#"
        expected_output = ""
        for i in range(1, n + 1):
            expected_output += (" " * (n - i)) + (pattern * i) + "\n"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output[:-1], result, f"Should be {expected_output}")

    def test_give_10_with_star_should_be_stars(self):
        # arrange
        n = 10
        pattern = "*"
        expected_output = ""
        for i in range(1, n + 1):
            expected_output += (" " * (n - i)) + (pattern * i) + "\n"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output[:-1], result, f"Should be {expected_output}")

    def test_give_10_with_stars_should_be_invalid_input(self):
        # arrange
        n = 10
        pattern = "***"
        expected_output = "Invalid Input"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(expected_output, result, f"Should be {expected_output}")
