'''
* @Author: Samarth BM.
* @Date: 2021-09-21 15:47  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-21 15:47
* @Title: To solve unit test cases for user details.
'''

from Validation import Validation
import unittest

class UserValidationTest(unittest.TestCase):

    def test_ValidFirstName(self):
        """
        Description: 
            In this test case when given a valid first name should return true.
        """        
        self.assertTrue(Validation.validate_first_name("Samarth"))
        self.assertTrue(Validation.validate_first_name("Sam"))


    def test_InvalidFirstName(self):
        """
        Description: 
            In this test case when given a invalid first name should return false.
        """        
        self.assertFalse(Validation.validate_first_name("samarth"))
        self.assertFalse(Validation.validate_first_name("sa"))
        self.assertFalse(Validation.validate_first_name("sam123"))
        self.assertFalse(Validation.validate_first_name("$am"))
        self.assertFalse(Validation.validate_first_name("saMarth"))


    def test_ValidLastName(self):
        """
        Description: 
            In this test case when given a valid last name should return true.
        """        
        self.assertTrue(Validation.validate_last_name("Bm"))
        self.assertTrue(Validation.validate_last_name("Bms"))

    
    def test_InvalidLastName(self):
        """
        Description: 
            In this test case when given a invalid last name should return false.
        """        
        self.assertFalse(Validation.validate_first_name("bm"))
        self.assertFalse(Validation.validate_first_name("BM"))
        self.assertFalse(Validation.validate_first_name("Bm123"))
        self.assertFalse(Validation.validate_first_name("Bm$"))
        