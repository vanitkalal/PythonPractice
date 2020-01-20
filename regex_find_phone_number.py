#This code will find a phone number using regex

import re

phonenum = re.compile(r'(\d{3}-)?\d{3}-\d{4}')

message = ('The phone number is 123-456-7890')

MO = phonenum.search(message)

print(r'Search Completed. Matched Result: ' + MO.group())



