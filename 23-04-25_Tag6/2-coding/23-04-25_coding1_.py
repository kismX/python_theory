## Def a function
print('-------Def a Func-------')
def my_func(a):
    print(a)

my_func(5)


########## RECAP ##

#### STRING methods
print('-------------STRING METHODS---------------')
print('hello'.upper())  # make strings to capital letters
print('HELLO'.isupper())   # true or false
print('HELLO'.lower())   # makes lower
print('hello'.endswith('h')) # true / false endet mit---
print('hello world'.capitalize())  #  1 buchstabe groß
print(' BLA '.strip())   #nimmt leertasten raus
print('hello world'.count('l'))   #zählt alle l -> hier gibt er also 3 aus
print('hello world'.split())   #returns a list split by " "
print('hello world'.split('l'))  # returns list split by "l"
print('hello'.isalpha())   #ob nur alphabetische characters.. wenn ja True.. sonst FAlse
print('Hello World'.replace('l', 'ß'))  #tausche l mit ß aus
print('hello'.find("ll"))   # sagt uns wo die zeichenabfolge zu finden ist. hjier_: 2
print('hello'.find("c"))     # google warum es -1 ausgibt.. evtl der wert für nicht vorhanden?

print(';'.join(['Hello', 'World', 'again']))   #setzt zwischen strings zb ein ";"

#Bob&;Die&;walks
print('&;'.join(['Bob', 'Dow', 'walks']))

print('Hello worldß'.casefold())   # macht ß zu ss

print()
print()

#### CONCATINATING 
print('------------CONCATINATING------------')
print('hello' + ' ' +'world')    # addiert string oder int
print("The sum of 1 + 2 is {0}".format(1+2))    #


word1 = 'hello'
word2 = 'world'
print(f"{word1.capitalize()} {word2.capitalize()}")  # f strig / formatted string literal - macht wie + nur mit space dazwischen ohne + " " 


# % operator
# % can be used to insert calues into sa string in a formatted wasy
# left operand is a string containing one or more plaxyeholders e.g. (%s, %d, %f)
# %s for strings , %d for int , %f for floats
name = 'John'
age = 30
hight = 1.70
print("My Name is %s and %d years old and %f." % (name, age, hight))    #%s for string using and %d

print()
print()

##### SLICING
print('------------INDEX AND SLICING-------------')

my_string = 'Hello, World'
print('Hello, World', ) 
print('012345678910', '#Indexzahlen')
print(my_string[0])   # string ist wie ein list mit indexzahlen. gibt nam 0 ein wird erster buchstabe ausgegeben
print(my_string[5])  # gibt komma aus


## slicing 
print('----')
# slice()  --> string[start:end:step]  

print(my_string[0:5])   # Gibt zeichen 0 bis 5 aus von hallo, World
print(my_string[1:6:1])
print(my_string[::2])    #
print(my_string[::3])   # 
print(my_string[7:12])   # 1-12 Index --> World
print(my_string[-2])    # geht auch rückwärts.. zeigt von hinten die indexe an - hier dann 'l'
print(my_string[7::2])
print(my_string[6:0:-1])    # negative steps: dann muss auch 1 dun 2 wert tgetaucscht werden, 
print(my_string[::-1])  # dlroW , olleH


####### STRING IMMUTABILITY #######
print('----------STRING IMMUTABILITY')

# str are immutable objects (cant modify), which means thatr the content of str cannot be modified in-place
# print(my_string = 'B')  # it doeosnt work
# instead any modifications to a string will create a new string in memory
# because of this immutability property, two stri with the same value can be saved in the same memory location
str1 = 'Hello'
print(id(str1)) # mit id kannst du die speicherposition ausgeben lassen? (googlen)

str2 = 'Hello'
print(id(str2))  # es stored in selber location wie str1

## when these two strings are created , py checks id there is already a string with the same value in memory
# if there is, yp will not allocate a new block of mem for the second strin, but instead will assign the mem addres of the forst strin to the second string
# this behavior is possible because str are immutable objects in py
# in summery, becauise str are immutable objects in py, two str with same value acn be saved in the same memory location

################### ENCODING ##########
# string encoding refers to the process of converting a sequence of nicode charactoer into a series ob byte that can be stored or transmitted over a network
# this is nessessary because computers and other electronic devices can lny understand binary data (i.e. 0 and 1
# each maps unicode characters to a unique series of bytes
# some popiular endocing schgemas include ascii, utf-8 and UTF-16

# acsii (american standard code for information interchange)
# it represents each character using a singe byte (8 bits), ewhich can represent up to 256 different characters

print(2 ** 8)  # 2 hoch 8 geich 256

# acsii dosemt support characters other than english
# UTF-8 (unicode transformation format 8-but) is a variable -lenght encofding scheme that can represent any unicode character using to four bytes
# it is the most widely used encodoing scheme oin the web and supportas characters from all major languages, including cinese, aracic and hebrew

# UTF-16 (unicode... 16-bit) is a fixed .. that represents each charactoer using 2 bytes

string = 'Hello, World!'
encode_string = string.encode('utf-8')
print(encode_string)



my_bytes = "café".encode('utf-8')
print(my_bytes)   # du siehst es sind unbekannte zeichen
print(len(my_bytes)) # hier siehst du dass 5 characters ausgegeben werden durch das é 











