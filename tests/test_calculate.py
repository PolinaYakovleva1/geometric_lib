import unittest
from math import pi
from calculate import calc


class MyTestArea(unittest.TestCase):
    def test_calc_circle_area(self):
        fig = "circle"
        func = "area"
        size = [10]
        desired_result = 100*pi

        result = calc(fig, func, size)

        self.assertEqual(result, desired_result)

    def test_calc_square_area(self):
        fig = "square"
        func = "area"
        size = [2]
        desired_result = 4

        result = calc(fig, func, size)

        self.assertEqual(result, desired_result)

    def test_calc_triangle_area(self):
        fig = "triangle"
        func = "area"
        size = [3, 4, 5]
        desired_result = 6

        result = calc(fig, func, size)

        self.assertEqual(result, desired_result)


class MyTestPerimeter(unittest.TestCase):
    def test_calc_circle_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [5]
        desired_result = 10 * pi

        result = calc(fig, func, size)

        self.assertEqual(result, desired_result)

    def test_calc_square_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [6]
        desired_result = 24

        result = calc(fig, func, size)

        self.assertEqual(result, desired_result)

    def test_calc_triangle_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [1, 2, 3]
        desired_result = 6

        result = calc(fig, func, size)

        self.assertEqual(result, desired_result)


class MyTestNegativeNumber(unittest.TestCase):
    def test_calc_circle_neg_area(self):
        fig = "circle"
        func = "area"
        size = [-5]
        expected_result = "Size should be > 0."

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_circle_neg_perimeter(self):
        fig = "circle"
        func = "perimeter"
        size = [-5]
        expected_result = "Size should be > 0."

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_square_neg_area(self):
        fig = "square"
        func = "area"
        size = [-1]
        expected_result = "Size should be > 0."

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_square_neg_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [-1]
        expected_result = "Size should be > 0."

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_triangle_neg_area(self):
        fig = "triangle"
        func = "area"
        size = [-1, 2, 3]
        expected_result = "Size should be > 0."

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)

    def test_calc_triangle_neg_perimeter(self):
        fig = "triangle"
        func = "perimeter"
        size = [-1, 2, 3]
        expected_result = "Size should be > 0."

        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

        self.assertEqual(str(context.exception), expected_result)
