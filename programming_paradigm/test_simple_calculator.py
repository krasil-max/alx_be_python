import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_addition(self):
        self.calculator = SimpleCalculator()
        self.assertEqual(self.calc.add)
        self.assertEqual(self.calculator.add(2,3),5)
        self.assertEqual(self.calculator.add(5,-2),3)
        self.assertEqual(self.calculator.add(0,5),5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract)
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(1, -1), 2)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply)
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 5), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide)
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-10, 2), -5)
        self.assertEqual(self.calculator.divide(10, 0), None)  # Test for division by zero

if __name__ == '_main_':
    unittest.main()