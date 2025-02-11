import unittest

def add_numbers(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, -1), -2)
        self.assertEqual(add_numbers(10, -5), 5)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
