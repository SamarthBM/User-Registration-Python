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
        self.assertFalse(Validation.validate_last_name("bm"))
        self.assertFalse(Validation.validate_last_name("BM"))
        self.assertFalse(Validation.validate_last_name("Bm123"))
        self.assertFalse(Validation.validate_last_name("Bm$"))
        

    def test_ValidMobileNumber(self):
        """
        Description: 
            In this test case when given a valid mobile number should return true.
        """        
        self.assertTrue(Validation.validate_mobile("91 9452147754"))
        
    
    def test_InvalidMobileNumber(self):
        """
        Description: 
            In this test case when given a invalid mobile number should return false.
        """        
        self.assertFalse(Validation.validate_mobile("9451457854"))
        self.assertFalse(Validation.validate_mobile("919856478525"))
        self.assertFalse(Validation.validate_mobile("8745874"))
        self.assertFalse(Validation.validate_mobile("91 7521478$"))
        