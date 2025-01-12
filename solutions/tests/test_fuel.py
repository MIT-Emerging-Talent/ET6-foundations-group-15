import unittest

from ..fuel import convert, gauge


class TestFractionToPercentage(unittest.TestCase):
    "Test the functions in the fuel.py file"

    def test_convert_half(self):
        """
        It should return 50
        """
        self.assertEqual(convert("1/2"), 50)

    def test_convert_higher_numerator(self):
        """
        It should raise an Assertion Error when Numerator greater than denominator
        """
        with self.assertRaises(AssertionError):
            convert("3/2")

    def test_convert_deno_zero(self):
        """
        It should raise an Assertion Error when the Denominator is zero
        """
        with self.assertRaises(AssertionError):
            convert("1/0")

    def test_convert_higher_non_numeric(self):
        """
        It should raise an Assertion Error when dealing with a Non-numeric input
        """
        with self.assertRaises(AssertionError):
            convert("a/b")

    def test_convert_negative_values(self):
        """
        It should raise an Assertion Error when the input is negative
        """
        with self.assertRaises(AssertionError):
            convert("-2/3")

    def test_gauge_half(self):
        """
        It should return 50%
        """
        self.assertEqual(gauge(50), "50%")

    def test_gauge_full(self):
        """
        It should return F
        """
        self.assertEqual(gauge(100), "F")

    def test_gauge_empty(self):
        """
        It should return E
        """
        self.assertEqual(gauge(0), "E")

    def test_gauge_higher_than_100(self):
        """
        It should raise an Assertion Error when the reading is above 100
        """
        with self.assertRaises(AssertionError):
            gauge(132)

    def test_gauge_99(self):
        """
        It should return 99%
        """
        self.assertEqual(gauge(99), "99%")

    def test_gauge_1(self):
        """
        It should return 1%
        """
        self.assertEqual(gauge(1), "1%")


if __name__ == "__main__":
    unittest.main()
