print('------COLLECTIONS-------')
# es geht um COLLECTIONS
# items in a list.. diff datatypes
# C. are used to orga and manage data more efficient
# different types of collections, incl. lists tules, sets and dictionaries

####### Lists
# a list is a linear collection of items that are orderes and changeble
# lists are created by enclosing a sequence of items within sqare brackets.
# for example:

my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list = []  # empty list
my_list = list()  # also a empty list

# get an element by index:
my_list = [1, 2, 3, 4, 5]
my_list[3]   # gibt dir index 3 aus, was hier 4 wäre


print('------Mutability-------')
# lists are mutable , so u can modify the content
# For Example:
my_list[2] = 6 
print(my_list)  # ich habe index 2 von list getauscht durch 6

#my_str = 'BLA'
#my_str[2] = 'F'  # Error because immutable

my_list2 = my_list
print(id(my_list), id(my_list2))   # identische ID

my_list2[0] = 'Hello World'   #change an index 0 durch "Hello WOlrd"
print(my_list2)
print(my_list)     # chaanged auch hier, weil gleiche ID , weil oben inhalt aus erste liste geholt
print(my_list == my_list2)   # demnach ist es natürlicha uch True

print()
print()
print('------Collecting-Type: Tuples-------')
### similar to list, but it is immutable, which means u cannoit change its cvontent

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)    
# my_tuple[2] = 'hello'   #doiesnt work because: immutable

# kann string, int aber auch lists enthalten
my_tuple = ['hello', 1, True, [1,2]]   
print(my_tuple)
print(my_tuple[1])  # indexed ausgeben geht auch
print(my_tuple[0:2]) #auch slicing geht


###### manipulate in dem tuple - geht nciht:
# my_tuple = (1, 2, 3, 4, 5)
# my_tuple[3][0] = 'Changed'
# print(my_tuple)  

#my_tuple[2] = 'Hello'   
#print(my_tuple)

print('-----------------------')

####### Loop over Lists
for item in my_list:
    print(item)

for index in range(len(my_list)):   #macht den rage so lange die liste ebenm index hat
    print(my_list[index])           

for item in my_tuple:
    print(item)




print('---------------------')
### lists
# access values by index
# slice
# find the index
# count
# reverse
# sort
# append
# extend
# insert
# pop

my_list = [1,2,3, 'four', 5 ]
print(my_list)

