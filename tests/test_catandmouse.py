from coe_number.catandmouse import cat_and_mouse
import unittest


class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_closer(self):
        self.assertEqual(cat_and_mouse(1, 5, 2), "Cat A")
        self.assertEqual(cat_and_mouse(1, 2, 1), "Cat A")
        self.assertEqual(cat_and_mouse(5, 1, 4), "Cat A")
        self.assertEqual(cat_and_mouse(99, 20, 85), "Cat A")
        self.assertEqual(cat_and_mouse(20, 99, 50), "Cat A")

    def test_cat_b_closer(self):
        self.assertEqual(cat_and_mouse(1, 5, 4), "Cat B")
        self.assertEqual(cat_and_mouse(1, 2, 3), "Cat B")
        self.assertEqual(cat_and_mouse(12, 2, 6), "Cat B")
        self.assertEqual(cat_and_mouse(77, 99, 90), "Cat B")
        self.assertEqual(cat_and_mouse(18, 67, 45), "Cat B")

    def test_both_cats_equal_distance(self):
        self.assertEqual(cat_and_mouse(1, 5, 3), "Mouse C")
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")
        self.assertEqual(cat_and_mouse(3, 1, 2), "Mouse C")
        self.assertEqual(cat_and_mouse(10, 20, 15), "Mouse C")
        self.assertEqual(cat_and_mouse(50, 50, 50), "Mouse C")

    def test_out_of_range(self):
        self.assertEqual(cat_and_mouse(0, 5, 2), "Out of Range")
        self.assertEqual(cat_and_mouse(1, 0, 2), "Out of Range")
        self.assertEqual(cat_and_mouse(1, 5, 0), "Out of Range")
        self.assertEqual(cat_and_mouse(101, 5, 2), "Out of Range")
        self.assertEqual(cat_and_mouse(1, 101, 2), "Out of Range")

    def test_invalid_input(self):
        self.assertEqual(cat_and_mouse("a", 5, 2), "Invalid Input")
        self.assertEqual(cat_and_mouse(1, "b", 2), "Invalid Input")
        self.assertEqual(cat_and_mouse(None, 5, 2), "Invalid Input")
        self.assertEqual(cat_and_mouse(1, None, 2), "Invalid Input")
        self.assertEqual(cat_and_mouse(1, 5, None), "Invalid Input")
