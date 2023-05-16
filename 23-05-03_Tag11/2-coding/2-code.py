## weiter von gestern:

my_list = [1,2,3,'four',5]
print(my_list.index('four'))   # gibt dir list index aus , hier 3

print()
print('-----------------')
print()


print(my_list.count(3)) # counts the occurrence of the element


print()
print('-----------------')
print()


my_list.insert(3, 'New Value')   # fügt list-inhalt ein
print(my_list)


print()
print('-----------------')
print()


my_list.reverse()       # umkehren der liste .. changing in place
print(my_list)


print()


my_list[::-1]  # im vgl: returning the reversed version of a list, but list wont be change
print(my_list)


print()
print('-----------------')
print()


my_list = [3,2,1,5,4]
print(my_list)
my_list.sort()       # sorts list in place
print(my_list)

print()

my_list = [3,2,1,5,4]
print(sorted(my_list))  # returns the sorted version of the list
print(my_list)          


print()
print('-----------------')
print()


my_list = [1,2,3,'four', 5.0]
my_list.extend([6,7,8])     # change list in place - means: änderungen werden in liste selbst gemacht udn braucht kein return in neue var
print(my_list)

print()

new_list = my_list[::] + [9,10]   # returns in new var-- weil es macht ncihts in liste selbst sondern erst im return zur neuen wvar
print(new_list)


print()
print('--PROBLEM-EXERCISE---------------')
print()

# write proig that takes a list of stirngs a new list containing the strings taht have a lenght of 4 or more

lst = ['apple', 'banana', 'cat', 'dog', 'elephant', 'frog']
result = []

def capitalize_anlong_string(lst):
    for item in lst:
        if len(item) > 4:    #geht auch >= 5
            result.append(item.upper())
    return result

print(capitalize_anlong_string(lst))

print('-----LIST COMPREHENSION-----')
## hier nun eine alternative, die einfacher ist und sehre gängig in python

strings = ['hello', 'world', 'again', 'bla']
length = []

print('')
print('')


for word in strings:
    length.append(len(word))
print(length)

print('')
print('--hier nun einfache code-weise')
# tabelle = 

length = [len(word) for word in strings if len(word) > 4]  
print(length)

print('')
print('---------------------------------')
print('')


## mapping and filtering with listcomps
uppercase_words = [word.upper() for word in strings]
print(uppercase_words)

print('')
print('')

list_numbers = [[5,6,3], [8,3,1], [9,10,4], [8,4,2]]
print(list_numbers[0][0])   # gibt charaktor 0 von element 0 aus

my_sums = [sum(nums) for nums in list_numbers]    #[14,12,23,14]
print(my_sums)

print('')
print('')
