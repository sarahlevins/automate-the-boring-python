# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.
# The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

import re

dateRegex = re.compile(r'''(
    ^(\d{2})
    /
    (\d{2})
    /
    (\d{4})$
)''', re.VERBOSE)

#test regex expression
def testRegex(x, regexName):
    output = regexName.search(x)
    if output == None:
        print('no matches found')
        return False
    else:
        print(output.group())
        return True

testRegex('04/22/1991', dateRegex)
testRegex('91/93/19922', dateRegex)
testRegex('04/', dateRegex)

def dateCheck(dateString):
    date = dateRegex.findall(dateString)[0]
    day = int(date[1])
    month = int(date[2])
    year = int(date[3])    

    if day > 31 or day < 1 or month > 12 or month < 1:
        return False
    elif day == 31 and month == 1 | 3 | 5 | 7 | 8 | 10 | 12:
        return True
    elif day <= 30 and month != 2:
        return True
    elif day <= 28 and month == 2:
        return True
    elif day == 29 and month == 2:
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
    else:
        return False


print(dateCheck('01/02/2020'))
print(dateCheck('01/02/1900'))
print(dateCheck('30/02/2021'))
print(dateCheck('29/02/2020'))
print(dateCheck('29/02/2021'))