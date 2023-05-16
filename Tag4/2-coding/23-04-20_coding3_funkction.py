## FUNCTIONS

# My first functin!


# here we define a functions
def lucky_number():
    print("Feeling lucky?")
    print(7777)

# here we call that function
lucky_number()


print("-------------------------------------")

# define a function with an argument
def greet(name):
    print("Hello", name, "!!")

greet("Veera")
greet("Rauli")




print("--------------------------")


# wir definieren eine function die eine nummer mit3 ,multipliziert
def triple(num):
    return num * 3

result = triple(9)  # declarieren var, die ergebnis beinhaltet
print(result)


my_test = triple("Hello")   # wir stellen fest es trippled auch strings
print(my_test)              # python triplled alles


print("--------------------------")

import random   # importiere random
money = 100       # var money, die 100 ist

def double_or_nothing(bet): 
    lucky = random.randint(0,1)    # vat with  random 0,1
    if lucky == 1:
        return bet * 2
    else:
        return -bet

money = money + double_or_nothing(money)

print(money)