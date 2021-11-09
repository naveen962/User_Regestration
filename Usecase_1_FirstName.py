#Validating and perform unit test on First Name


import unittest
import re

def validate(firstname):

    pattern ="^[a-zA-Z]{3,20}$"
    match= re.match(pattern,firstname)
    if match:
        return True
    else:
        return False

class UserRegistration(unittest.TestCase):
   
    def setUp(self):
        self.firstname=input("\nEnter FirstName : ")


    def test_Firstname(self):
        expect=True
       
        #Act
        result=validate(self.firstname)
        #Assert
        self.assertEqual(result,expect,"Not Valid")
   
    
if __name__=="__main__":
    unittest.main()







