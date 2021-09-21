'''
* @Author: Samarth BM.
* @Date: 2021-09-21 15:41  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-21 15:41
* @Title: To validate user details using regex.
'''

import re
from LogHandler import logger

class Validation():

    def validate_first_name(firstName):
        """
        Description:
            This function is to validate first name.
            Condition: Name should start with Capital letter and should have min 3 letters.

        Args:
            firstName: First name to validate

        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^[A-Z]{1}[a-z]{2,}$", firstName))

        except Exception as e:
            logger.error(e)

    def validate_last_name(lastName):
        """
        Description:
            This function is to validate last name.
            Condition: Last name should start with Capital letter and should have min 2 letters.

        Args:
            lastName: Last name to validate

        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^[A-Z]{1}[a-z]{1,}$", lastName))

        except Exception as e:
            logger.error(e)

    def validate_mobile(mobile):
        """
        Description:
            This function is to validate mobile number.
            Condition: Mobile number should start with country code 91
            and followed by space and 10 digits.

        Args:
            mobile: Mobile number to validate

        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^(91)\\s[0-9]{10}$", mobile))

        except Exception as e:
            logger.error(e)
