## guessing game

import random 

r_num = random.randint(1,100000)
u_num = int(input("Guess the number: "))
guess = 1

while u_num != r_num:
    print("Wrong number!")
    guess += 1
    if u_num < r_num:
        print("Your number is to small!!")
    elif u_num > r_num:
        print("Your number is to big!!")
    u_num = int(input("Guess the number: "))
print("Correct number: ", r_num)
print("You did it ", guess, " times")