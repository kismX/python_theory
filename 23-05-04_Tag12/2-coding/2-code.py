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



print()
print()
print('=====================Tag 12===========================')
print()
print()

print('------cartasian product the long way------')
## Cartasian Product
#ist xyz mal 123 in x und y achse also_ x1 x2 x3 y1 y2 y3 z1 z2 z3

A= ['X', 'Y', 'Z']
B = [1,2,3]

def catesian_prod1(A, B):
    result = []
    for itemA in A:
        for itemB in B:
            result.append((itemA, itemB))
    return result

print(catesian_prod1(A, B))

print('-------Cartasian product with list Comprehension--------------')
####  SAme with List Comprehension#

def cartesian_prod2(A,B):
    result = [ (itemA, itemB) for itemA in A
                                for itemB in B]
    return result

print(cartesian_prod2(A,B))

print()
print()
print('-------------Building List of lists------------------------')
print()
print()

board = [ ['_']*3 for num in range(3)]    # ['_','-','-'], ['_','-','-'],['_','-','-']
print(board)

board[1][2] = "x"   # mach bei list index 1 index 2 n 
print(board)

print()
print('-----')

### kurze schreibweise macht aber was anderes:
weird_board = [['-']*3] *3
print(weird_board)

print()

weird_board[1][2] = 'O'    # weil es wird oben bei dem erst stellten tabelle eingefügt, die dann mit 3 moultipliziert wird
print(weird_board)


print()
print('-----')
# each list inside the outer list points to the same memory adress
one_line = ['_'] * 3
two_line = one_line
three_line = one_line

weird_board2 = [one_line, two_line, three_line]
weird_board2[0][0] = 'O'
print(weird_board2)

print()
print('-----')
# due to the slicing we make a copy of the inner lists and point therefore to different memory adresses
one_line = ['_'] * 3
two_line = one_line[:]
three_line = one_line[:]

weird_board2 = [one_line, two_line, three_line]
weird_board2[0][0] = 'O'
print(weird_board2)

print()
print()
print('------list.sort vs. the sort Biult-in----')
print()
# the list.sort method sorts a list in place
# in contrast, the bvuilt-in func 'sorted' cerated a new list and returns it

fruits = ['grape', 'rasperry', 'apple', 'banana']
sorted(fruits, reverse=True)                           # gibt umgekerhte reihenfolge der list aus

print()
print()

print(sorted(fruits, key=len))    # gibt list geordnet nach länge aus

print()
print()


books = [('hello', 3), ('world', 1), ('again', 2)]

def sort_helper(item):
    return item[1]                  # das argument sagrt, welche stelle angesprochen werden soll, (nach der dann unten sortiert wird)
    

print(sorted(books, key=sort_helper))

print()
print()

numbers = [[1,2], [1,1], [0,2]]
print(sorted(numbers, key=sum))                       # den versteh ich nicht!!

print()
print()
print('------------all() and any()-----------------------')
print()
print()

print(all([True,True,True]))
print(all([True, False, True]))   # sobald eine false, dann false
print(all([]))                      # standard true


print()
print()

print(any([False, False]))
print(any([False, True]))           # sobald eine True, dann True      
print(any([]))                  # standard false


print()
print()

my_str = 'd33CI'
my_list = [any(char.isdigit() for char in my_str)]
print(my_list)


print()
print()
print('----------------Tag13-------------------')
## Anonymous Functions 
# Lambda

fruits = ["strawberry", "fig", "apple", "cherry", "raspberry"]

sort_helper = lambda word: word[::-1]   # wir machen function ohne def zu benötigen

for fruit in fruits:
    print(sort_helper(fruit))

print()

sorted(fruits, key=lambda word: word[::-1])   # man kann functoina uch direkt bei key in sorted einfügen
print(sorted(fruits, key=lambda word:word[::-1]))
# if lambda is hard to read, convert lambda to a def stateent

print()
print()
tuple_list = [(2,5),(1,7),(4,3),(6,1),(3,8)]

sort_helper = lambda item: item[-1]
print(sort_helper((tuple_list)))

#sorted(tuple_list, key=sort_helper)


print('----------DOCTIONARIES---------------------------------')

### dictionaries
## in the {} ist the 'word': the key. like an index on the left of : .. and the value on the right
# du darfst in so nem dict nur einen key einmal verwendfen.. also geht schon, aber das wird dann überschrieben..  
my_list = {'name': 'Alice', 'age': 25, 'city': 'New York'}  

bob_dict = {'name': 'Bob', 'boss': [{'name': 'jeremy'}, {'name': 'John'}]}
print(bob_dict['boss'][0]['name'])

for employee in bob_dict['boss']:
    print(employee['name'])

print('---------------')
print()


my_list = ['Bob', 'Bob', 'Karl']

my_dict = {}

my_dict['Bob'] = '1st'   # diese wird durch das zerite überschribeen
my_dict['Bob'] = '2nd'
my_dict['Karl'] = "3rd"
print(my_dict)


print('-------FROMKEYS-----------')

my_keys = ['name', 'age', 'city']
my_dict = dict.fromkeys(my_keys, '-')
print(my_dict)

print()
print()

my_dict = {}
for key in my_keys:
    my_dict[key] = '-'

print(my_dict)

print('-----------')

my_dict.get('name', 'BLA')   # 2nd argument is a default value and used if the key doesnt exist



print()
print('-------------setdefault()-----------')
print()

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'} 
print(my_dict['name'])  # gibt den key 'name' aus, welcher hier 'Alice' ist
print(my_dict.setdefault('name', 'Bob'))   # eyx existiert alice, also wird kein Bob ausgegeben
print(my_dict.setdefault('country', 'USA')) #es gibt kein country.. also gibt es USA aus

my_dict['country'] = 'Germany' # nun haben wir key country mit Germany hinzugefügt
print(my_dict['country'])  #also gibt es Germany aus
print(my_dict)  # siehste, country mit germany ist in dict enthalten

print()
print()
print('------UPDATE-DICTIONARIES: update()------------')
print()


my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'} 
new_dict = {'country': 'USA', 'age': 26}

my_dict.update(new_dict)   # wir updaten das my_dict mit den infos von new_dict
print(my_dict)  #siehe da, alter nun 26 und country nun germany

my_dict['zip'] = 3333   # habe den key 'zip' mit dem value 3333 hinzugefügt
print(my_dict)  # hier, zip ist dabei

print()
print()

print(my_dict.items())


print('---')
#for loop: für jedes item in my_dict soll index0 (key) und index1 (value) ausgegeben und dan  geprinted werden
for item in my_dict.items():
    key = item[0]     # index position 0 = key
    value = item[1]   # index position 1 = value
    print(key, value)


print()
print()
print('------------------')
print()
print()
print(my_dict.keys())       # gibt die keys allein aus
print(my_dict.values())   # gibt die values allein aus
print()
print()


for value in my_dict.values():
    print(value)








