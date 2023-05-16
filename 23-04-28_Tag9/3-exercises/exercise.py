''' 
## Exercise 1
- Write a program that prompts the user for a number. The number should divide the number 1. Handle the ZeroDivisionError exception and print an error message.
- The program will keep prompting the user to enter a number until a non-zero number is entered.
Hint:
- use a while loop
- research on the keyword: *break*
'''

'''

x = 0
y = 0
while x == 0:
    try:
        x = int(input('Please give me a yummy number: ')) # user gibt number ein und diese als int in x
        print(1/x)                              # The number should divide the number 1
        break
    except (ValueError):
        print()
        print()
        print('================================================')
        print('<<PUKE>> Damn, you gave me sth like a string???!!')
        print('================================================')
        print()
        print()

    except (ZeroDivisionError):
        print()
        print()
        print('==============================')
        print("Yeachhh!! I don't like zeroes!")
        print('==============================')
        print()
        print()
print()
print()
print('===================================================')
print(f" Yeah!! With {x} you gave me a kool number to eat!")
print('===================================================')
print()
print()


#########   TASK 2
- Write a program that prompts the user to enter two numbers and performs division.
- Handle the ValueError exception if the user inputs a non-numeric value.
Note: The program will keep prompting the user to enter two numbers until a non-zero numeric value is entered as the second number.



while True:
    try:
        x = int(input('Please give me a yummy number: '))
        y = int(input('One number is too less, another please: '))
        print(x/y)                             
        break
    except (ValueError):
        print()
        print()
        print('================================================')
        print('<<PUKE>> Damn, you gave me sth like a string???!!')
        print('================================================')
        print()
        print()
    except (ZeroDivisionError):
        print()
        print()
        print('==============================')
        print("Yeachhh!! I don't like zeroes!")
        print('==============================')
        print()
        print()
print()
print()
print('===================================================')
print(f" Yeah!! With {x} you gave me a kool number to eat!")
print('===================================================')
print()
print()




- Write a program that prompts the user to enter a list of integers and computes the average.
- Handle the ValueError exception if the user inputs a non-numeric value.
Note: The program assumes that the user enters a comma-separated list of integers. I
f the user enters a list with a different separator, the program will not be able to parse
 the input and may raise other exceptions.




while True:
    try:
        a = int(input('Please give me 1st number: '))
        b = int(input('Please give me 2nd number: '))
        c = int(input('Please give me 3rd number: '))
        d = int(input('Please give me 4th number: '))
        x=(a+b+c+d)/4
        print(x)                             
        break
    except (ValueError):
        print()
        print()
        print('================================================')
        print('<<PUKE>> Damn, you gave me sth like a string???!!')
        print('================================================')
        print()
        print()
print()
print()
print('===================================================')
print(f"         ====>> {x} is the average! <<====")
print('===================================================')
print()
print()

'''
print('--------- Lösung mit liste----------------')

while True:
    try:
        a = input("Type Numbers (seperated by ,): ")                       
        li = a.split(",")
        if ',' not in a:
            raise ValueError("You forgot the damn ,")
        for i in range(len(li)):
            li[i] = int(li[i])    # li ist liste vonm integern
        m = sum(li)/len(li)
        print()
        print()
        print('===================================================')
        print(f"         ====>> {m} is YOUUR average! <<====")
        print('===================================================')
        print()
        print()
        break
    except ValueError:
        print('=================================================')
        print('<<PUKE>> Damn, you dont gave me a ,  ???!!')
        print('=================================================')



## Exercise 4:
# Create a Python function that receives two parameters: a date and a number of
# days.   Create a Python function that receives three parameters: a date 
# (datetime object), number of days (integers), timezone (string).
# The function should add the number of days to the date, considering 
# the timezone passed as an argument. If the timezone is not valid, the 
# function should raise an exception.



