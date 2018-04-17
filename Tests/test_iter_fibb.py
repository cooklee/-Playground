from unittest import TestCase
from math_functions.mat_functions import Fibonacci

fibonacci_iter = Fibonacci.fibonacci_iter


class FibonacciIterTests(TestCase):

    def test_fibonacci_zero(self):
        """
        input : 0
        expected result : 0
        """
        self.assertEqual(fibonacci_iter(0), 0, "this is from definition")
