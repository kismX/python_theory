
x = ('hello world')
print(x, end='\n')  #mends with default value
print(x, end='2')    #endet mit einer 2
print(x)            #gibt output von x
print('hello', 'world', sep=':') # separiert mit einem : oder auch was du willst


#create file that has that string in it
with open('output.txt', "w") as f:        # f is a random letter "w" stands for write
    print('Hello World', file=f)      #creates and prints it in a file
    print('Hello World')                # printed it only in output


##Nested Quotes
my_string = "Hello World"
my_string2 = "She said, \"Is is a beautiful day\" "  #so kann man wörtliche rede einbauen weil " sonst den string beendet
my_string3 = "She said, 'it is a beautiful day'"     #use single quotes in double quotes
my_string3 = ''' She said, "it is a beautiful day" '''  #use tripple quotes, than u can use souble quote



#######'DATA TYPES #######
#1. INTEGER: whole numbers: 0-9 ; -1
#2. FLOAT: decimal numbers with piunts: e.g. 0.1 ; -0.5
#3. BOOLEAN:true or false
#4. STRING
#5. COMPLEX NUMBERS: numbers consisting of two parts 8imaginary and real part) (e.g. 3+4: 3 the real, 4 the imaginary)
d = 2 + 3j #2 real #3 imaginary
e = -4j #

#6. None: abcense of a value
j = None
type(j) 

