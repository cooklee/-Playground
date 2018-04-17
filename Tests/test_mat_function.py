from unittest import TestCase
from math import sqrt

from math_functions.mat_functions import private_pow, Fibonacci


class FibonacciTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        Fibonacci.number_of_execution = 0

    def test_fibonacci_zero(self):

        """
        input : 0
        expected result : 0
        """
        self.assertEqual(Fibonacci.fibonacci(0), 0, "this is from definition")




