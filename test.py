import unittest
from string_functions import to_upper, to_lower, capitalize

class TestToUpper(unittest.TestCase):
    def test_to_upper(self):
        #Check the number, there couldn't be any change
        self.assertEqual(to_upper('43'), '43')
        self.assertEqual(to_lower('54'), '54')
        #Check the to_upper and to_lower methods with
        #different edge cases
        self.assertNotEqual(to_upper('False'), 'False')
        self.assertNotEqual(to_upper('False'), 'false')
        self.assertNotEqual(to_upper('False'), 'FALSe')
        self.assertNotEqual(to_upper('false'), 'fALSE')
        self.assertNotEqual(to_upper('false'), 'False')
        self.assertEqual(to_lower('False'), 'false')
        self.assertNotEqual(to_lower('False'), 'FALSe')
        self.assertNotEqual(to_lower('false'), 'fALSE')
        self.assertNotEqual(to_lower('false'), 'False')
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