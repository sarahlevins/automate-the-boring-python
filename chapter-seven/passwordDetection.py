# Write a function that uses regular expressions to make sure the password string it is passed is strong. 
# A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, 
# and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

import re

#use lookaheads, doesn't work for length due to multiple repeats
lengthRegex = re.compile(r'(.){8,}')
uppercaseRegex = re.compile(r'(?=.*[A-Z])')
lowercaseRegex = re.compile(r'(?=.*[a-z])')
numericRegex = re.compile(r'(?=.*[0-9])')

def testRegex(x, regexName):
    output = regexName.search(x)
    if output == None:
        return False
    else:
        return True

def passwordStrengthTest(password):
    if testRegex(password, lengthRegex) and testRegex(password, uppercaseRegex) and testRegex(password, lowercaseRegex) and testRegex(password, numericRegex):
        print(password + ' is a strong password')
        return True
    else: 
        print(password + ' isn\'t a strong password')
        return False

print(passwordStrengthTest('2Llll8ll'))
print(passwordStrengthTest('sarah123'))
print(passwordStrengthTest('SarahLevins123'))
print(passwordStrengthTest('Password'))
print(passwordStrengthTest('**48391ljLsd'))