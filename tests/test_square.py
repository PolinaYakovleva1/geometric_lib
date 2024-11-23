import unittest
import calculate


class SquareTest(unittest.TestCase):
    """Area"""

    def test_area_zero(self):
        area_zero = calculate.calc("square", "area", [0])
        self.assertEqual(area_zero, 0)

    def test_area_positive(self):
        res_area_1 = calculate.calc("square", "area", [52])
        self.assertEqual(res_area_1, 2704)

        res_area_2 = calculate.calc("square", "area", [5])
        self.assertEqual(res_area_2, 25)

        res_area_3 = calculate.calc("square", "area", [2])
        self.assertEqual(res_area_3, 4)

    def test_area_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "area", [-1])
        self.assertEqual(str(context.exception), "Size must be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "area", [-52])
        self.assertEqual(str(context.exception), "Size must be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "area", [-1356])
        self.assertEqual(str(context.exception), "Size must be > 0.")

    """Perimeter"""

    def test_perimeter_zero(self):
        perimeter_zero = calculate.calc("square", "perimeter", [0])
        self.assertEqual(perimeter_zero, 0)

    def test_perimeter_positive(self):
        res_perimeter_1 = calculate.calc("square", "perimeter", [1])
        self.assertEqual(res_perimeter_1, 4)

        res_perimeter_2 = calculate.calc("square", "perimeter", [25])
        self.assertEqual(res_perimeter_2, 100)

        res_perimeter_3 = calculate.calc("square", "perimeter", [3])
        self.assertEqual(res_perimeter_3, 12)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "perimeter", [-5])
        self.assertEqual(str(context.exception), "Size must be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "perimeter", [-6])
        self.assertEqual(str(context.exception), "Size must be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("square", "perimeter", [-52])
        self.assertEqual(str(context.exception), "Size must be > 0.")


if __name__ == "__main__":
    unittest.main()
