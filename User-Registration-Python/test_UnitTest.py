'''
* @Author: Samarth BM.
* @Date: 2021-09-21 13:53  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-21 13:53
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

