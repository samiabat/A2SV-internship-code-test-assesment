import unittest
from string_functions import to_upper, to_lower, capitalize

class TestToUpper(unittest.TestCase):
    def test_to_upper(self):
        #Check the number, there couldn't be any change
        self.assertEqual(to_upper('43'), '43')
        self.assertEqual(to_lower('54'), '54')
        #Check the to_upper method with
        #different edge cases
        self.assertNotEqual(to_upper('False'), 'False')
        self.assertNotEqual(to_upper('False'), 'false')
        self.assertNotEqual(to_upper('False'), 'FALSe')
        self.assertNotEqual(to_upper('false'), 'fALSE')
        self.assertNotEqual(to_upper('false'), 'False')
        self.assertEqual(to_upper(''), '')
class TestToLower(unittest.TestCase):
    def test_to_lower(self):
        #Check the numbers as they couldn't be changed
        self.assertEqual(to_lower('78'), '78')
        #Check the to_lower method with different edge cases 
        self.assertEqual(to_lower('False'), 'false')
        self.assertNotEqual(to_lower('False'), 'FALSe')
        self.assertNotEqual(to_lower('false'), 'fALSE')
        self.assertNotEqual(to_lower('false'), 'False')
        self.assertEqual(to_lower(''), '')
        
class TestCapitalize(unittest.TestCase):
    def test_capitalize(self):
        #Check with numbers as they couldn't be changed
        self.assertEqual(capitalize('90'), '90')
        #Check the capitalize method with different edge cases
        self.assertEqual(capitalize('Sefineh'), 'Sefineh')
        self.assertEqual(capitalize('sefineh'), 'Sefineh')
        self.assertEqual(capitalize('SEFINEH'), 'Sefineh')
        self.assertNotEqual(capitalize('SEFINEH'), 'sEfINEH')
        self.assertNotEqual(capitalize('Sefineh'), 'sefineh')
        self.assertNotEqual(capitalize('sefineh'), 'sEfineh')
        self.assertNotEqual(capitalize('SEFINEH'), 'SefineH')
        

if __name__ == '__main__':
    unittest.main()