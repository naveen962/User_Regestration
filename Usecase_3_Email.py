import unittest
import re

def validate(email):

    pattern ="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    match= re.match(pattern,email)
    if match:
        return True
    else:
        return False

class UserRegistration(unittest.TestCase):
   
    def setUp(self):
        self.email=input("\nEnter Email : ")


    def test_Email(self):
        expect=True
       
        #Act
        result=validate(self.email)
        #Assert
        self.assertEqual(result,expect,"Not Valid")
   
    
if __name__=="__main__":
    unittest.main()