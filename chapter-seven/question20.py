#How would you write a regex that matches a number with commas for every three digits?
#It must match the following:
#'42'
#'1,234'
# #'6,368,745'
# but not the following
# '12,34,567'
# '1234'

import re

commaNumber = re.compile(r'''(
    ^\d{1,3}
    (,\d{3})*$
    )''', re.VERBOSE)


#test
def testRegex(x, regexName):
    output = regexName.search(x)
    if output == None:
        print('no matches found')
    else:
        print(output.group())

#test cases
testRegex('1234', commaNumber)
testRegex('120,000', commaNumber)
testRegex('103', commaNumber)
