# Write a function that takes a string and does the same thing as the strip() string method. 
# If no other arguments are passed other than the string to strip, then whitespace characters 
# will be removed from the beginning and end of the string. Otherwise, the characters specified 
# in the second argument to the function will be removed from the string.

#remove whitespace from string

import re

stringRegex = re.compile(r'^\s*(.*?)\s*$')
# print(stringOutput)

def stringMethod(string, *args):
    if args:
        print('arg given')
    else:
        #remove whitespace from strings 
        string = stringRegex.search(string)
        print(string.groups())
        # strippedString = ' '.join(stringRegex.findall(string))
        # return strippedString
        

print(stringMethod('    goo f ljl  '))