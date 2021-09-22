'''
* @Author: Samarth BM.
* @Date: 2021-09-21 19:01  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-21 19:01
* @Title: To solve unit test cases for user details.
'''

from logging import NullHandler
from Validation import Validation
import unittest

class UserValidationTest(unittest.TestCase):
    """
        Description:
            This class holds all the test cases required to satisfy the
            created methods in Validation class.
        """ 

    
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
        

    def test_ValidPassword(self):
        """
        Description: 
            In this test case when given a valid password should return true.
        """        
        self.assertTrue(Validation.validate_password("Abc$123d"))
        self.assertTrue(Validation.validate_password("$amArth18"))


    def test_InvalidPassword(self):
        """
        Description: 
            In this test case when given a invalid password should return false.
        """        
        self.assertFalse(Validation.validate_password("abcdef"))
        self.assertFalse(Validation.validate_password("abcdefghi"))
        self.assertFalse(Validation.validate_password("Abcde12fgh"))

    
    def test_ValidEmail(self):
        """
        Description: 
            In this test case when given a valid email should return true.
        """        

        validEmails = ["abc@yahoo.com", "abc-100@yahoo.com", "abc.100@yahoo.com",
                       "abc111@abc.com", "abc-100@abc.net", "abc.100@abc.com.au",
                       "abc@1.com", "abc@gmail.com.com","abc+100@gmail.com"]
        for mails in validEmails:

            self.assertTrue(Validation.validate_email(mails))
        

    def test_InvalidEmail(self):
        """
        Description: 
            In this test case when given a invalid email should return false.
        """        
        inValidEmails = ["abc","abc@.com.my","abc123@gmail.a","abc123@.com",
                         "abc123@.com.com",".abc@abc.com","abc()*@gmail.com","abc@%*.com",
                         "abc..2002@gmail.com","abc.@gmail.com","abc@abc@gmail.com",
                         "abc@gmail.com.1a","abc@gmail.com.aa.au"]
        
        for mails in inValidEmails:
            self.assertFalse(Validation.validate_email(mails))

    def test_emptyFirstName(self):
        """
        Description: 
            In this test case when given a empty first name should raise
            null handler exception .
        """ 

        try:
            Validation.validate_first_name("")
        except Exception:
            self.assertRaises(NullHandler)


    def test_emptyLastName(self):
        """
        Description: 
            In this test case when given a empty last name should raise
            null handler exception .
        """ 

        try:
            Validation.validate_last_name("")
        except Exception:
            self.assertRaises(NullHandler)


    def test_emptyMobileNumber(self):
        """
        Description: 
            In this test case when given a empty mobile number should raise
            null handler exception .
        """ 

        try:
            Validation.validate_mobile("")
        except Exception:
            self.assertRaises(NullHandler)


    def test_emptyPassword(self):
        """
        Description: 
            In this test case when given a empty password should raise
            null handler exception .
        """ 

        try:
            Validation.validate_password("")
        except Exception:
            self.assertRaises(NullHandler)

    def test_emptyEmail(self):
        """
        Description: 
            In this test case when given a empty email should raise
            null handler exception .
        """ 

        try:
            Validation.validate_email("")
        except Exception:
            self.assertRaises(NullHandler)