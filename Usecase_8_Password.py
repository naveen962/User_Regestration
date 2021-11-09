import unittest
import re

def validate(password):

    pattern ="^(?=.*[A-Z])(?=.*[0-9])(?=.*[@_\$#!()=+.])[a-z0-9A-Z[@_\$#!()=+.]{8,}$"
    match= re.match(pattern,password)
    if match:
        return True
    else:
        return False

class UserRegistration(unittest.TestCase):
   
    def setUp(self):
        self.password=input("\nEnter Password : ")


    def test_Password(self):
        expect=True
       
        #Act
        result=validate(self.password)
        #Assert
        self.assertEqual(result,expect,"Not Valid")
   
    
if __name__=="__main__":
    unittest.main()