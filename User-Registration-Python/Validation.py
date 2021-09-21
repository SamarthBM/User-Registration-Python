'''
* @Author: Samarth BM.
* @Date: 2021-09-21 13:28  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-21 13:28
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
