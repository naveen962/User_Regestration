import unittest
import re

def validate(phno):

    pattern ="^(91)?[-\s]?[0-9]{10}$"
    match= re.match(pattern,phno)
    if match:
        return True
    else:
        return False

class UserRegistration(unittest.TestCase):
   
    def setUp(self):
        self.phno=input("\nEnter PhoneNumber : ")


    def test_PhoneNumber(self):
        

        expect=True
       
        #Act
        result=validate(self.phno)
        #Assert
           
        self.assertEqual(result,expect,"Not valid")
       
    
if __name__=="__main__":
    unittest.main()