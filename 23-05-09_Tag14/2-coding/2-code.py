## dictionaries etc


print()
print()
print('=====================Tag 14===========================')
print()
print()
## Dictionaries continued

print('Dictionary Comprehension')
print()
print()
print()

count_code = [('land1', 123), ('land2', 345)]

dict = {country : dial_num for country, dial_num in count_code}  
print(dict)

#shorter
dict2 = {code[0] : code[1] for code in count_code}   # er nimmt die einzelnen tuples (code) der liste (list) und macht daraus dict (dict2) in der reiihenfolge code[0] und code [1]
print(dict2)

# mit bedingung
dict3 = {code : country.upper() for country, code in dict.items() if code > 200}   # macht alles upper wenn bedingung >200 erfüllt ist
print(dict3)

print()
print()
print()
print('=====================The Awesome Zip===========================')
print()
print()

list_zip = list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))       #zip is in-built func
print(list_zip)

list_zip = list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))       #zip is in-built func
print(list_zip)

print()
print('ziplongest')

#enumerate
list_enumerate = list(enumerate('ABC', start=1))
print(list_enumerate)

print(type(list_enumerate))
print()

my_fruits = ['Apple', 'Banana', 'Grapefruit']
for integer, value in enumerate(my_fruits, start=1):
    print(integer, value)



