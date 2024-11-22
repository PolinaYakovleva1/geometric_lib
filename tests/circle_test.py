import unittest
import calculate

class CircleTest(unittest.TestCase):
    """Area"""

    def test_area_positive(self):
        self.assertEqual(calculate.calc("circle", "area", [5]),
                         78.5398163397)
        self.assertEqual(calculate.calc("circle", "area", [2]),
                         12.5663706144)
        self.assertEqual(calculate.calc("circle", "area", [1]),
                         3.14159265359)

    def test_area_negative(self):
        error_message = "Radius must be > 0."
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-1])
        self.assertEqual(str(context.exception), error_message)

        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "area", [-52])
        self.assertEqual(str(context.exception), error_message)
        with self.assertRaises(ValueError) as context:

            calculate.calc("circle", "area", [-9])
        self.assertEqual(str(context.exception), error_message)

    """Perimeter"""

    def test_perimeter_positive(self):
        self.assertEqual(calculate.calc("circle", "perimeter", [1]),
                         6.283185307179586)
        self.assertEqual(calculate.calc("circle", "perimeter", [3]),
                         18.8495559215)
        self.assertEqual(calculate.calc("circle", "perimeter", [52]),
                        326.725635973)

    def test_perimeter_negative(self):
        error_message = "Radius must be > 0."
        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-5])
        self.assertEqual(str(context.exception), error_message)

        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-2])
        self.assertEqual(str(context.exception), error_message)

        with self.assertRaises(ValueError) as context:
            calculate.calc("circle", "perimeter", [-52])
        self.assertEqual(str(context.exception), error_message)


if __name__ == '__main__':
    unittest.main()