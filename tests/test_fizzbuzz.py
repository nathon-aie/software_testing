from coe_number.fizzbuzz import fizzbuzz
import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_give_1_return_1(self):
        result = fizzbuzz(1)
        self.assertEqual(result, 1)

    def test_give_3_return_Fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, "Fizz")

    def test_give_5_return_Buzz(self):
        result = fizzbuzz(5)
        self.assertEqual(result, "Buzz")

    def test_give_15_return_FizzBuzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result, "FizzBuzz")

    def test_give_2_return_2(self):
        result = fizzbuzz(2)
        self.assertEqual(result, 2)

    def test_give_30_return_FizzBuzz(self):
        result = fizzbuzz(30)
        self.assertEqual(result, "FizzBuzz")

    def test_give_9_return_Fizz(self):
        result = fizzbuzz(9)
        self.assertEqual(result, "Fizz")

    def test_give_10_return_Buzz(self):
        result = fizzbuzz(10)
        self.assertEqual(result, "Buzz")

    def test_give_7_return_7(self):
        result = fizzbuzz(7)
        self.assertEqual(result, 7)

    def test_give_0_return_FizzBuzz(self):
        result = fizzbuzz(0)
        self.assertEqual(result, "FizzBuzz")
