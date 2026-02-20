from coe_number.number_utils import is_prime_list
import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_5_6_is_not_prime(self):
        prime_list = [4, 5, 6]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_7_8_9_is_not_prime(self):
        prime_list = [7, 8, 9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_11_13_17_is_prime(self):
        prime_list = [11, 13, 17]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_15_16_18_is_not_prime(self):
        prime_list = [15, 16, 18]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_empty_list_is_not_prime(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_non_integer_list_is_not_prime(self):
        prime_list = ["a", "b", "c"]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_mixed_list_is_not_prime(self):
        prime_list = [2, "a", 3]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_negative_numbers_is_not_prime(self):
        prime_list = [-2, -3, -5]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_large_prime_numbers_is_prime(self):
        prime_list = [101, 103, 107]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
