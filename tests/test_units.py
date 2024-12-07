import unittest

from application_name.main import Greeter, MathOperations


class TestGreeter(unittest.TestCase):
    def setUp(self):
        self.greeter = Greeter()

    def test_greet_world(self):
        self.assertEqual(self.greeter.greet(), "Hello, World!")

    def test_greet_person(self):
        self.assertEqual(self.greeter.greet("Alice"), "Hello, Alice!")


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(MathOperations.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(MathOperations.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(MathOperations.multiply(6, 7), 42)

    def test_divide(self):
        self.assertEqual(MathOperations.divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            MathOperations.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
