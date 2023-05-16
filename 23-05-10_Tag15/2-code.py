## Today: 
# collections module (setdefault, counter)
# set theory

zen_python = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

words = zen_python.split()
dict_index = {}

for index, word in enumerate(words):
    occurences = dict_index.get(word, [])   # ; here  return a list
    occurences.append(index)
    dict_index[word] = occurences
    
    if word == 'is':
        print(dict_index['is'])

print()
print()
print('----Alternative version:----------')
print()
print()


words = zen_python.split()
dict_index = {}
for word in words:
    dict_index[word] = []

for index, word in enumerate(words):
    dict_index[word].append(index)
print(dict_index)


print()
print()
print('-----------------collections .. .hier fehlt ein thema ;) -----------')
print()
print()
' ()...) '

print()
print()
print('-----------------collections.Counter-----------')
print()
print()

import collections    # ist n module, dass geladen werden muss


ct = collections.Counter('abracadabra') # gibt dir ein dict mit keys und dazugehöroigen values , welche die häufigkeit des keys sind
print(ct) 

print()

ct.update('aaaazzz')    # adding the chars
print(ct)               # so the counter gets 4 more a and 3 more z

print()
print()
print(ct.most_common(2))  # die zb 2 häufigsten werden ausgegeben

print()
print()

subjects = [
    {'name': 'English', 'grade': 'A'},
    {'name': 'German', 'grade:': 'F'},
    {'name': 'Maths', 'grade:': 'F'}
]

ct2 = collections.Counter()

for subject in subjects:
    ct2.update(subject['grade'])   #irgendwas stimmt nicht in dieser line

ct2['F']



print()
print()
print('-----------------Sets and set theory-----------')
print()
print()

# store collections of unique elements
# elements in ser cann be any data type that is immutable
# sets are useful for math operations:
## 1. intersections
## 2. difference
## 3. and more

# use in py
## 1. remove duplicates
## 2. checking membership
## 3. sets have hashable data tyopes as elemnmts: thereffore u can use the set's elements as dict keys

# set is mutable
# frozenset is immutable

# use case removing dupliucation:
l = ['spam', 'spam', 'eggs', 'spam', 'bacen', 'eggs']
print(set(l))   # entfernt die doppelten! 

print()
# set elemets must be hasable: thar means: obj that has a hash code which never changes during its lifetime
# with hash code we can compare two obj

# hashable obj which compare must have the same hash code

# numeric types, str are all hashable
# immutable sequence like a tuple with only immutable elements are also hashable and can therefore be used in sets

my_hashable_tuple = (1,2)
hash(my_hashable_tuple)  # gibt mir eine hash number aus

my_unhashable_tuple = (1,2, [1,2])  
#    hash(1,2, [1,2])  # this is immutable

print()


set()          # not hashable! takes immutable obj and itself it is mutable
frozenset([1,2,3])   # hashable .. takes immutable obj and itself it is also immutable

# hashcode varriert von pc zu pc.. hat was mit dem speicherplatz zu tun
## it depends on: py version, machine itself 
## hash code of correctly implementeds obj is guaranteed to be constant only within one py process

s = set()   # defindes an empty set
type(s)    # its a set

s = {1.0, 2.0, 3.0}  
s.add(5)   # fügt zb 5 in das set hinzu
print(s)  # siehe da, alles incl 5   
# adding elements to a set may change the order of existing elements randomly

s= {1.0, 2.0, 3.0}
s.pop() # removes the first element 
print(s)  


print()
s= set([1,2,3,4]) #or {1,2,3,4}
print(s)

# there is no special syntax to represent frozenset (immutable) literals
s_frozen = frosenset([1,2,3,4])
print(s)

print()
print()
print('--------------Set Comprehension------------')
print()

l = ['spam', 'spam', 'egg']
my_set = {item for item in l}  #weil sets jedes item nur einmal enthalten kann... -->?? hmmm warum entfernt er die doppelten hier, dachte das geht mit set() und ist { } nicht n dict?!
print(my_set)

print()
print()
print('--------------Set Operations------------')
print()

# set types implement set operations
# giiven teo sets a and b:
## 1. Union: a | b 
## 2. Intersection: a & b
## 3. Digfferences: a - b
## 4. symmertric diff: a ^ b

#smart use of set op can reduce both the line count
# and the executioin time of py programms
# at the same time making code easier to read

### 1. union: input siehe livecode...
A = {1, 3, 5, 7}
B = {1, 2, 4, 6, 7}
union = A | B       # fügt zusammenm und entfernt alle überschenidungen, also: 1,2,3,4,5,6,7
print(union) 

A.__or__(B)         # alternative die das genauso macht .  its a magical method.. we'll talk later about magic. m.
A.union(B)          # ebenso alternative

### 2- intersection --> input siehe livecode
A = {1,2,5,7}
B = {1,2,4,6}
A & B               # entfernt alle, die nicht gleich sind.. also bleiben: 1,2

A.intersection(B)     # wieder alternative schreibweise
C = {1}
A.intersection(B,C) #macht er auch mit C .. dann bleibt: 1

### 3- Difference  --> siehe wieder livecode
A = {1,2,3}
B = {2,3,4}
B - A               # entfernt alle aus B bis auf die zu A unterschiedliche, es bleibt: 4
A - B               # entfernt alle aus A bis auf die zu B unterschiedliche, es bleibt: 1

## 4- symmeteric diff.. siehe...
A = {1,2,3}
B= {3,4}
A ^ B               # entfernt alle bis auf die in beiden unterschiedlichem- es bleibena lso: 1,2,4



# further operations
#... siehe livecode