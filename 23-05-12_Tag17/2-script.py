print('1. ======= RECAP =======')
print('----RegEx----')



# LISTE MIT SEQUENZEN
# \d - [0-9]
# \D - [^0-9]
# \w - [a-zA-Z0-9]
# \W - [^a-zA_Z0-9]
# \s - whitespace
# \S - everything except whoitespace
# \b - word boundery: when a alphanumerical char and _ is followed by any other char
# \b - word boundery: when \w char is followed by \W char and at hte beginning or end string 
 
# LISTE MIT SETS

# LISTE MIT METACHAR

my_str = 'Tomato Ketchup'

import re

my_matches = re.search(r'\w+\b', my_str)   
print(my_matches)

# r = raw strings are strings that start with r 
print('raw string' ,  r'\w\b')
print('string', '\b')  # \b doesnt work , weil 
print('new line: ', '\n')  # \n macht ja ne neue zeile.. wenn wir r davor schreiben wird es raw string (siehe näshte line)
print('new line: ', r'\n')


print("practrise EXAMPLE for this Theory")

my_str = """
day: 3, month: 1, year: 2012↵
day:1, month:12, year:2012↵
day:  3, month: 11, year: 2012↵
day:  10, month: 2, year: 2022↵
day:  1, month: 9, year: 20123453
"""

my_matches = re.findall(r'day:\s*\d,\smonth:\s*\d,\syear:\s*\d{4}', my_str)

my_matches = re.findall(r'day:\s*(\d+),\smonth:\s*(\d+),\syear:\s*(\d{2,4})', my_str)
# print(my_matches)

# for my_match in my_matches:
#     print(my_match)
#     day, month, year = my_match
#     print(f'day: {day}, month: {month}, year: {year}')

# a list of datetime objects
from datetime import datetime
my_dates = []
for day, month, year in my_matches:
    print(f'day: {day}, month: {month}, year: {year}')
    dt = datetime(int(year), int(month), int(day))
    my_dates.append(dt)

print(my_dates)

print()
print()
print('===========SUBSTITUTE REGEX===================')
print()

import re

input_str1 = "John Smith, 25 years old"
input_str = "John Smith, 25 years old; John   Smith, 25 years old"
matches_str = re.findall('(John)', input_str)
# print(matches_str)

output_str = re.sub('(John) Smith, 25 years old', r"REPLACED_STR \1", input_str1)
# matches the whole string and replaces it with REPLACE_STR  
print('REPLACE',output_str)

output_str = re.sub('(John)', r"First name: \1", input_str)
print(output_str)

output_str  = re.sub('(John)\s+(Smith)', r"First name: \1, surname: \2", input_str)
print(output_str)


input_str = "John Smith, 25 years old; Bon   Doe, 25 years old"
output_str = re.sub(r'[A-Za-z]+\s+[A-Za-z]+,', 'PLACHOLDER', input_str)
print(output_str)

input_str = "John Smith, 25 years old; Bon   Doe, 25 years old"
output_str = re.sub('([A-Za-z]+)\s+([A-Za-z]+),', r'FIRST_N: \1 SUR_N: \2', input_str)
print(output_str)


print('--------------')
# wir könnenmit den groups paar dinge  machern: 

def regex_group_helper(match):
    return f"FIRST_N: {match.group(1).upper()} SUR_N: {match.group(2).upper()}"

output_str = re.sub('([A-Za-z]+)\s+([A-Za-z]+),', regex_group_helper, input_str)
print(output_str)

output_str = re.sub('([A-Za-z]+)\s+([A-Za-z]+),', lambda match: f"F_N: {match.group(1).upper()}, S_N: {match.group(2).upper()}", input_str)
print(output_str)


my_dates_str = "01.02.2012 11.3.13 14.2.2023 14.3.333"   # 02(month)/01(day)/2012(year) ....
# year we would capture from 2 to 4
formated_str = re.sub(r"(\d{2})\.(\d{1,2})\.(\d{2,4})", r'\2/\1/\3', my_dates_str)
print(f'd{2,4}:', formated_str)
#year 2 digit or (|) 4 digits
formated_str = re.sub(r"(\d{2})\.(\d{1,2})\.(\d{2}\b|\d{4}\b)", r'\2/\1/\3', my_dates_str)
print(f'(d{2}|d{4}):',formated_str)