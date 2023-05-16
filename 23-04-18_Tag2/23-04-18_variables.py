### Variables exercise
print("-------------VARIABLES------------")

# here we declare the var amount of cats
# we also assign in the value 2
amount_of_cats = 2
print(amount_of_cats)

# here we are reusing the same var
# we reassign it in value 2+1
amount_of_cats = amount_of_cats + 1
print(amount_of_cats)

# let's experiment
print(amount_of_cats + 99)   # das ädnert nicht den value von amount_of_cats weil kein =
print(amount_of_cats) 

print("----Dynamite----")
print()

spam = "eggs"
print(spam, type(spam))   # spam is a string! 

spam = 42    # = ist assignment operator
print(spam, type(spam))   # spam is now int - so_ var are dynamic!!

print()
print()
print("-----OPERATORS-----")
print()
print()

count = 1 
print(count + 1)
# print(count + "spam")    # man kann nicht einfach so string mit int mixen, also error

# hmmm.. decimals and ints are both numbers
print(count + 1.7)   #int + float klappt
print(count + .3)       # klappt
print(count + 7.)       # klappt
print(type(count + 7.)) # is n float bei + 7. 
print(count + True)     # ergibt 2 weil count is 1 und True = 1

print("eggs" + "spam")   # ergibt eggspam


print()
print()
print("---------OPERATORS--------")
print()
print()

score = 10
print(score - 51)
print(score * 4)
print(score / 4)
print("------------")
print(score % 1)  #modulus / modulo / remainder / residual
print(score % 2)
print(score % 3)   # weil 10/3 3,3333 ist.. und was übrig bleibt is 1.. das ist das reimainder ding % = 1
print(score % 4)   # 10/4 is 2.5 ; 10%4 = 2 weil 4 leuten kannst du 2 euro geben, es bleiben 2 übrig also ist  %=2
print(score % 5)   # 0, weil kein rest 
print(score % 6)   # 10/6 = 1,6666 .. es bleiben 4 übrig, also %=4
print(score % 7)
print(score % 8)
print(score % 9)
print(score % 10)

print("------ EXPONENTIAL-------")
print(score ** 2)    # score ** 2 = 100 weil hoch 2
print(score ** 3)       # 1000  weil hoch 3
print(score ** 4)

print("------Floor division------")
print(score // 1)   # floor is rounding down
print(score // 2)   #
print(score // 3)   # 10/3 ist 3.3333 also 3 
print(score // 4)   # 10/4 is 2.5, also 2
print(score // 5)   # 10/5 is 2, also 2
print(score // 6)   # 10/6 is 1,6666 , also 1
print(score // 7)   # 10/7 is .... also 1

print()
print()
print("---------Assignment operators----")
print()
print()


score = 100
# score = score + 20    # macht adiert 20 zu um 20 % mehr zu ahbaen
score += 20             # ist einfacher mit +=
print(score)

score -= 3              # nimmt score und subtrahiert daovn 3 .. easy
print(score)


my_name = "Batman"
my_name += " Spam"      # geht auch mit addieren von strings
print(my_name)
# es gibt noch mehr zb &= usw.. google, lerne es, wenn bock

print()
print()
print("----MATH FUN----")
print()
print()

print(max(2, 1, 4, 9, 1, 9))        # gibt dir doie größte nummer aus = 9
print(min(2, 1, 4, 9, 1, 9, -3))    # gibt kleinste nummer aus = -3

print(abs(5))                       # abs gibt dir den betrag einer zahl aus
print(abs(-41))                     # abs also absolute distance from 0

print(pow(3,4))                     # 3 to the power of 4 >> 3 hoch 4 = 3*3*3*3

print(round(3.14149))               # rundet ne dezimalzahl
print(round(3.9))                   # rundet ab .5 auf und darunter runter
print(round(3.14149, 3))            # 3 argument sagt auf welche kommastelle es rundet


print()
print()
print("---Math module")
print()
print()

import math
# instead of round
print(math.ceil(1.1))   # rounding, but it always go up!
print(math.ceil(1.2))   
print(math.ceil(1.8))
print(math.ceil(1.9))

print(math.floor(1.1))   # rounding, but it always go down!
print(math.floor(1.2))   
print(math.floor(1.8))
print(math.floor(1.9))

print(math)             # math is a builtin module
print(round)            # round is a built-in function

print()
print()
print()
print('Input funktion')
print()
print()
print()
            
my_name = input("Whats your name traveller? ")    # auch wenn du nix eingibst (), runr run, will er dennoch input   
print("Hello", my_name)
print(type(my_name))                            # egal was du eingibst, es ist ein string

print()
print()
print("----Type Casting----")
print()
print()
# willst du aber ne number als input: Type casting

money = input("How much you got? ")
money = int(money)                  # cast the money STRING into an INTEGER
money = money * 3                   # multipliziere wert von money mit 3
print("Now you have", money)        # gib das aus

money = input("How much you got? ")
money = float(money)                 # cast the money STRING into an float
money = money * 3                   # multipliziere wert von money mit 3
print("Now you have", money)        # gib das aus




















