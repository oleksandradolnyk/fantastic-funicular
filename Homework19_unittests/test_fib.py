import unittest
from functions import Fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_sequence(self):
        fib = Fibonacci()

        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)

    def test_negative_input(self):
        fib = Fibonacci()

        # Test invalid input (negative numbers)
        with self.assertRaises(ValueError) as exp:
            fib(-1)
        self.assertEqual(str(exp.exception), 'Positive integer number expected, got "-1"')

    def test_float_input(self):
        fib = Fibonacci()

        with self.assertRaises(ValueError) as exp:
            fib(3.14)
        self.assertEqual(str(exp.exception), 'Positive integer number expected, got "3.14"')


if __name__ == '__main__':
    unittest.main()
