from coe_number.guess_num import guess_int, guess_float
import unittest


class TestGuessNum(unittest.TestCase):
    def test_guess_int(self):
        for _ in range(100):
            result = guess_int(1, 10)
            self.assertIsInstance(result, int)
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 10)

    def test_guess_int_invalid_input(self):
        cases = [
            ("1", 10),
            (1, "10"),
            (1.0, 10),
            (1, 10.0),
            (None, 10),
            (1, None),
            (True, 10),
            (1, False),
            ([], 10),
            (1, {}),
        ]
        for start, stop in cases:
            with self.subTest(start=start, stop=stop):
                self.assertEqual(guess_int(start, stop), "Invalid Input")

    def test_guess_int_out_of_range(self):
        cases = [
            (5, 5),
            (10, 1),
            (0, 0),
        ]
        for start, stop in cases:
            with self.subTest(start=start, stop=stop):
                self.assertEqual(guess_int(start, stop), "Out of Range")

    def test_guess_float(self):
        for _ in range(100):
            result = guess_float(1.0, 10.0)
            self.assertIsInstance(result, float)
            self.assertGreaterEqual(result, 1.0)
            self.assertLessEqual(result, 10.0)

    def test_guess_float_invalid_input(self):
        cases = [
            ("1.0", 10.0),
            (1.0, "10.0"),
            (1, 10.0),
            (1.0, 10),
            (None, 10.0),
            (1.0, None),
            (True, 10.0),
            (1.0, False),
            ([], 10.0),
            (1.0, {}),
        ]
        for start, stop in cases:
            with self.subTest(start=start, stop=stop):
                self.assertEqual(guess_float(start, stop), "Invalid Input")

    def test_guess_float_out_of_range(self):
        cases = [
            (5.0, 5.0),
            (10.0, 1.0),
            (0.0, 0.0),
        ]
        for start, stop in cases:
            with self.subTest(start=start, stop=stop):
                self.assertEqual(guess_float(start, stop), "Out of Range")
