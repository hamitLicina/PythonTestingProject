import unittest
from math import add, subtract, multiply, divide



class TestMath(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_add(self):
        result = self.add(2, 2)
        self.assertEqual(result, 4)  # Test addition

    def test_subtract(self):
        result = self.subtract(5, 3)
        self.assertEqual(result, 2)  # Test subtraction

    def test_multiply(self):
        result = self.multiply(3, 3)
        self.assertEqual(result, 9)  # Test multiplication

    def test_divide(self):
        result = self.divide(10, 2)
        self.assertEqual(result, 5) # Test division

    def tearDown(self):
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
    print("Test passed")