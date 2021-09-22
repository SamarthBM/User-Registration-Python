from Validation import Validation

def test_validFirstName():
    """
    Description: 
        In this test case when given a valid first name should return true.
    """ 
    
    validFirstName = ["Samarth","Sam"]
    
    for names in validFirstName:
        assert Validation.validate_first_name(names) == True


def test_invalidFirstName():
    """
    Description: 
        In this test case when given a invalid first name should return false.
    """ 

    invalidFirstName = ["samarth", "sa", "sam123", "sam", "$am" ]

    for names in invalidFirstName:
        assert Validation.validate_first_name(names) == False


def test_validLastName():
    """
    Description: 
        In this test case when given a valid last name should return true.
    """ 

    validLastName = ["Bm", "Bms"]

    for names in validLastName:
        assert Validation.validate_last_name(names) == True


def test_invalidLastName():
    """
    Description: 
        In this test case when given a invalid last name should return false.
    """ 

    invalidLastName = ["bm", "Bms123", "Bm$", "BM"]

    for names in invalidLastName:
        assert Validation.validate_last_name(names) == False


def test_validMobileNumber():
    """
    Description: 
        In this test case when given a valid mobile number should return true.
    """ 

    validMobileNumber = ["91 9452147754", "91 9874563214"]

    for numbers in validMobileNumber:
        assert Validation.validate_mobile(numbers) == True


def test_invalidMobileNumber():
    """
    Description: 
        In this test case when given a invalid mobile number should return false.
    """ 

    invalidMobileNumber = ["919452147754", "9874563214", "91-9654789665", "919854785", "91 9854521"]

    for numbers in invalidMobileNumber:
        assert Validation.validate_mobile(numbers) == False


def test_validPassword():
    """
    Description: 
        In this test case when given a valid password should return true.
    """ 

    validPassword = ["Abcd@1234", "$Ama1254a", "Acde7854$"]

    for passwords in validPassword:
        assert Validation.validate_password(passwords) == True


def test_invalidPassword():
    """
    Description: 
        In this test case when given a invalid password should return false.
    """

    invalidPassword = ["Abcd1234", "$Ama", "sam1234", "$amkkal56", "$AM785KKL"]

    for passwords in invalidPassword:
        assert Validation.validate_password(passwords) == False


def test_validEmail():
    """
    Description: 
        In this test case when given a valid email should return true.
    """ 

    validEmails = ["abc@yahoo.com", "abc-100@yahoo.com", "abc.100@yahoo.com",
                    "abc111@abc.com", "abc-100@abc.net", "abc.100@abc.com.au",
                    "abc@1.com", "abc@gmail.com.com","abc+100@gmail.com"]

    for mails in validEmails:
        assert Validation.validate_email(mails) == True


def test_invalidEmail():
    """
    Description: 
        In this test case when given a invalid email should return false.
    """ 

    inValidEmails = ["abc","abc@.com.my","abc123@gmail.a","abc123@.com",
                     "abc123@.com.com",".abc@abc.com","abc()*@gmail.com","abc@%*.com",
                     "abc..2002@gmail.com","abc.@gmail.com","abc@abc@gmail.com",
                     "abc@gmail.com.1a","abc@gmail.com.aa.au"]

    for mails in inValidEmails:
        assert Validation.validate_email(mails) == False