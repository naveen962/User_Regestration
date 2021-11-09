import unittest
import re

def validate(lastname):

    pattern ="^[A-Z]{1}[a-z]{3,20}$"
    match= re.match(pattern,lastname)
    if match:
        return True
    else:
        return False

class UserRegistration(unittest.TestCase):
   
    def setUp(self):
        self.lastname=input("\nEnter LastName : ")


    def test_Lastname(self):
        expect=True
       
        #Act
        result=validate(self.lastname)
        #Assert
        self.assertEqual(result,expect,"Not Valid")
   
    
if __name__=="__main__":
    unittest.main()

