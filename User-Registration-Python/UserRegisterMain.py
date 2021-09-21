'''
* @Author: Samarth BM.
* @Date: 2021-09-21 19:18  
* @Last Modified by: Samarth BM
* @Last Modified time: 2021-09-21 19:18
* @Title: To take the user input for details, validate it and store it.
'''

from LogHandler import logger
from Validation import Validation

class UserRegisterMain:
    """
        Description:
            This class holds method to take the user input for 
            all the details and then store it to a dictionary.
        """ 

    def __init__(self):
        self.userDetails = []

    def user_input(self):
        """
        Description:
            This function is to take user input for all details, 
            validate the details and then store to a dictionary.
        """        
        details = {}

        try:
            while True:

                firstName = input("Enter your first name: ")
                if Validation.validate_first_name(firstName):
                    details['FirstName'] = firstName
                    logger.info("First name is added")
                else:
                    logger.error("Invalid first name")
                

                lastName = input("Enter your last name: ")
                if Validation.validate_last_name(lastName):
                    details['LastName'] = lastName
                    logger.info("Last name is added")
                else:
                    logger.error("Invalid last name")

                mobileNumber = input("Enter your mobile number: ")
                if Validation.validate_mobile(mobileNumber):
                    details['Mobile'] = mobileNumber
                    logger.info("Mobile number is added")
                else:
                    logger.error("Invalid mobile number")

                email = input("Enter your email: ")
                if Validation.validate_email(email):
                    details['Email'] = email
                    logger.info("Email is added")
                else:
                    logger.error("Invalid email")
                        

                password = input("Enter your password: ")
                if Validation.validate_password(password):
                    details['Password'] = password
                    logger.info("Password is added")
                else:
                    logger.error("Invalid password")

                self.userDetails.append(details)
                print(self.userDetails)

        except Exception:
            logger.error("Inavlid input")


if __name__ == "__main__":
    userRegistration = UserRegisterMain()
    userRegistration.user_input()
