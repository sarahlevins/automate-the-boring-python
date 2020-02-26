import pyperclip, re

#PHONE REGEX
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #area code (in or out of parenthesis)
    (\s|-|\.)           #separator (space, hyphen or .)
    (\d{3})             #first three digits
    (\s|-|\.)           #separator
    (\d{4})             #last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #match extension
)''', re.VERBOSE)

#EMAIL REGEX
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #username
    @                   #at symbol
    [a-zA-Z0-9.-]+      #domain
    (\.[a-zA-Z{2,4}])   #dot something
    (\.[a-zA-Z{2,4}])?  #extra dot something
)''', re.VERBOSE)

#FIND MATCHES IN CLIPBOARD TEXT
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#COPY RESULTS TO CLIPBOARD
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else: print('No phone numbers or email addresses found.')