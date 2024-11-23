import unittest
import calculate


class TriangleTest(unittest.TestCase):
    """Area"""

    def test_area_zero(self):
        area_zero = calculate.calc("triangle", "area", [0, 0, 0])
        self.assertEqual(area_zero, 0)

    def test_area_positive(self):
        res_area_1 = calculate.calc("triangle", "area", [4, 5, 3])
        self.assertEqual(res_area_1, 6)

        res_area_2 = calculate.calc("triangle", "area", [6, 6, 6])
        self.assertEqual(res_area_2, 9)

        res_area_3 = calculate.calc("triangle", "area", [9, 8, 7])
        self.assertEqual(res_area_3, 12)

    def test_area_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "area", [-52, -52, -52])
        self.assertEqual(str(context.exception),
                         "Size should be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "area", [-9, -8, -7])
        self.assertEqual(str(context.exception),
                         "Size should be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "area", [-13, -1, -56])
        self.assertEqual(str(context.exception),
                         "Size should be > 0.")

    """Perimeter"""

    def test_perimeter_zero(self):
        perimeter_zero = calculate.calc("triangle",
                                            "perimeter", [0, 0, 0])
        self.assertEqual(perimeter_zero, 0)

    def test_perimeter_positive(self):
        res_perimeter_1 = calculate.calc("triangle",
                                             "perimeter", [1, 2, 3])
        self.assertEqual(res_perimeter_1, 6)

        res_perimeter_2 = calculate.calc("triangle",
                                             "perimeter", [6, 6, 6])
        self.assertEqual(res_perimeter_2, 18)

        res_perimeter_3 = calculate.calc("triangle",
                                         "perimeter", [13, 56, 52])
        self.assertEqual(res_perimeter_3, 121)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "perimeter", [-1, -1, -1])
        self.assertEqual(str(context.exception),
                         "Size should be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "perimeter", [-1, -2, -3])
        self.assertEqual(str(context.exception),
                         "Size should be > 0.")

        with self.assertRaises(ValueError) as context:
            calculate.calc("triangle", "perimeter", [-4, -5, -6])
        self.assertEqual(str(context.exception),
                         "Size should be > 0.")


if __name__ == "__main__":
    unittest.main()
