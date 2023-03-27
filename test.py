import unittest
from string_functions import to_upper, to_lower, capitalize

class TestToUpper(unittest.TestCase):
    def test_to_upper(self):
        #Check the number, there couldn't be any change
        self.assertEqual(to_upper('43'), '43')
        #different edge cases
        self.assertEqual(to_upper('hello world'), "HELLO WORLD")
        self.assertEqual(to_upper('HELLO WORLD'), 'HELLO WORLD')
        self.assertEqual(to_upper(''), '')
        #Check invalid conditions
        self.assertNotEqual(to_upper('False'), 'False')
        self.assertNotEqual(to_upper('False'), 'false')
        

class TestToLower(unittest.TestCase):
    def test_to_lower(self):
        #Check the numbers as they couldn't be changed
        self.assertEqual(to_lower('54'), '54')
        self.assertEqual(to_lower('78'), '78')
        #Check the to_lower method with different edge cases 
        self.assertEqual(to_lower('Hello World'), 'hello world')
        self.assertEqual(to_lower('HELLO WORLD'), 'hello world')
        self.assertEqual(to_lower(''), '')
        #Check invalid conditions
        self.assertNotEqual(to_lower('False'), 'FALSe')
        self.assertNotEqual(to_lower('false'), 'fALSE')
        
        
class TestCapitalize(unittest.TestCase):
    def test_capitalize(self):
        #Check with numbers as they couldn't be changed
        self.assertEqual(capitalize('90'), '90')
        #Check the capitalize method with different edge cases
        self.assertEqual(capitalize('Hello world'), 'Hello world')
        self.assertEqual(capitalize('hello world'), 'Hello world')
        self.assertEqual(capitalize('HELLO WORLD'), 'Hello world')
        self.assertEqual(capitalize(''), '')
        #Check invalid conditions
        self.assertNotEqual(capitalize('Hello World'), 'Hello WORld')
        self.assertNotEqual(capitalize('Hello world'), 'hello world')
        

if __name__ == '__main__':
    unittest.main()