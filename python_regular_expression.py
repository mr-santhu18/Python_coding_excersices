'''
Regular Expressions in Python
Regular expressions (regex) are used for searching, 
matching, and manipulating text in Python using the (re) module.
'''

#1. Search (re.search())
#Finds the first occurrence of a pattern in a string.

import re

text = "Hello, welcome to Python programming!"
match = re.search(r'Python', text)

if match:
    print("Found:", match.group())  # Output: Found: Python
else:
    print("Not found")



#2. Find All Matches (re.findall())
# Finds all occurrences of a pattern in a string.


import re

text = "Python is fun. Learning Python is great!"
matches = re.findall(r'Python', text)

print(matches)  # Output: ['Python', 'Python']


#3. Replace Text (re.sub())
# Replaces all occurrences of a pattern with a new string.

import re

text = "I love Python programming"
new_text = re.sub(r'Python', 'Java', text)

print(new_text)  # Output: I love Java programming




# 5. Groups (re.group())
# Captures specific parts of a match using parentheses ().

import re

text = "My phone number is 987-654-3210"
match = re.search(r'(\d{3})-(\d{3})-(\d{4})', text)

if match:
    print("Full match:", match.group(0))  # Full match
    print("First part:", match.group(1))  # First group
    print("Second part:", match.group(2)) # Second group
    print("Third part:", match.group(3))  # Third group  


