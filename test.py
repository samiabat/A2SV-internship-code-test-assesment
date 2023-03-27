import unittest
from string_functions import to_upper, to_lower, capitalize

class TestToUpper(unittest.TestCase):
    def test_to_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertEqual(to_upper("HELLO"), "HELLO")
        self.assertEqual(to_upper("Hello"), "HELLO")
        self.assertEqual(to_upper(""), "")
        
class TestToLower(unittest.TestCase):
    def test_to_lower(self):
        
        self.assertEqual(to_lower("WORLD"), "world")
        self.assertEqual(to_lower("world"), "world")
        self.assertEqual(to_lower("World"), "world")
        self.assertEqual(to_lower(""), "")
        
class TestCapitalize(unittest.TestCase):
    def test_capitalize(self):
        
        self.assertEqual(capitalize("hello world"), "Hello world")
        self.assertEqual(capitalize("HELLO WORLD"), "Hello world")
        self.assertEqual(capitalize("Hello World"), "Hello world")
        self.assertEqual(capitalize(""), "")
        
if __name__ == '__main__':
    unittest.main()