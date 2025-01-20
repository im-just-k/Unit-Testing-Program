# test_math_operations.py
import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        """Test the addition of two numbers."""
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-2, -3), -5)

    def test_subtract(self):
        """Test the subtraction of two numbers."""
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(-2, -3), 1)

    def test_multiply(self):
        """Test the multiplication of two numbers."""
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        """Test the division of two numbers."""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertRaises(ValueError, divide, 5, 0)  # Test division by zero

    def test_divide_edge_case(self):
        """Test division when dividing by a very small number."""
        self.assertAlmostEqual(divide(1, 0.0001), 10000)

if __name__ == '__main__':
    unittest.main()