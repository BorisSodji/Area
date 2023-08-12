import unittest
from area import *


class MyTestCase(unittest.TestCase):
    delta_value = 0.001

    def test_circle(self):
        self.assertRaises(ValueError, circle, 'x')
        self.assertRaises(TypeError, circle, -1)
        self.assertRaises(TypeError, circle, 0)
        self.assertAlmostEqual(circle(1), 3.141592653589739, delta=self.delta_value)
        self.assertAlmostEqual(circle(1.0), 3.141592653589739, delta=self.delta_value)

    def test_square(self):
        self.assertRaises(ValueError, square, 'x')
        self.assertRaises(TypeError, square, -1)
        self.assertRaises(TypeError, square, 0)
        self.assertEqual(square(1), 1)
        self.assertAlmostEqual(square(1.0), 1.0, delta=self.delta_value)

    def test_rectangle(self):
        self.assertRaises(ValueError, rectangle, 'x', 'y')
        self.assertRaises(ValueError, rectangle, 'x', 1)
        self.assertRaises(ValueError, rectangle, 1, 'y')

        self.assertRaises(TypeError, rectangle, -1, 1)
        self.assertRaises(TypeError, rectangle, 1, -1)
        self.assertRaises(TypeError, rectangle, -1, -1)

        self.assertRaises(TypeError, rectangle, 0, 1)
        self.assertRaises(TypeError, rectangle, 1, 0)
        self.assertRaises(TypeError, rectangle, 0, 0)

        self.assertEqual(rectangle(1, 2), 2)
        self.assertAlmostEqual(rectangle(1.0, 2.0), 2.0, delta=self.delta_value)
        self.assertAlmostEqual(rectangle(1.0, 2), 2.0, delta=self.delta_value)
        self.assertAlmostEqual(rectangle(1, 2.0), 2.0, delta=self.delta_value)

    def test_triangle(self):
        self.assertRaises(ValueError, triangle, 'x', 'y')
        self.assertRaises(ValueError, triangle, 'x', 1)
        self.assertRaises(ValueError, triangle, 1, 'y')

        self.assertRaises(TypeError, triangle, -1, 1)
        self.assertRaises(TypeError, triangle, 1, -1)
        self.assertRaises(TypeError, triangle, -1, -1)

        self.assertRaises(TypeError, triangle, 0, 1)
        self.assertRaises(TypeError, triangle, 1, 0)
        self.assertRaises(TypeError, triangle, 0, 0)

        self.assertAlmostEqual(triangle(1, 2), 1)
        self.assertAlmostEqual(triangle(1.0, 2.0), 1.0, delta=self.delta_value)
        self.assertAlmostEqual(triangle(1, 2.0), 1.0, delta=self.delta_value)
        self.assertAlmostEqual(triangle(1.0, 2), 1.0, delta=self.delta_value)


if __name__ == '__main__':
    unittest.main()
