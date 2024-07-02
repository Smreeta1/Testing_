import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Adds the parent directory of 'tests' to the Python path

from summ.add import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):             
        
        data = [1, 2, 4]                #Test that it can sum a list of integers
        result = sum(data)
        self.assertEqual(result, 7) 	#a == b
        self.assertTrue(result)         #bool(result) is True
         
if __name__ == '__main__':
    unittest.main()