## While loop

number = 0
while (number < 5):     #it runs the block until contition is False, also 5
    number = number + 1
    print(number)

print("Done.")

## when it is an infinite loop that wont stop, press: crtl + c 



# make a list in py
foods = ["Banana", "Coffee", "Honey", 8]      # listen macht man mit eckigen klammern

# To access oitems based on their index
print(foods[0])  # weil lists are indexed, wir können sagen was von der liste geprinted werden soll
print(foods[1])
print(foods[2])
print(foods[3])  

print("--------")

# to loop over items one by one
for item in foods:   # for var in list
    print(item)        # do sth.. here: print

print("--------------------------------------")

for pet in ["cat", "dog", "rat"]:
    print("I want a ", pet)

for char in "Coffee":   # printed einen buchgstaben nach dem andren
    print(char)         # auch bucstaben sind indexed 0,1,2.3..

print("---------------")

drink = "Tea"
print(drink[0])  #access index 0 of the var "drink"


print("------------------")
my_range = range(2,10)    # createds a range from 2-10
print(my_range)

for x in my_range:          # gibt alle zahlen außer der 10 aus
    print(x)

print(my_range[0])          # gibt die 2 aus, weil die index = 0 hat



print("----------------------------------")


fun_fruits = ["Rawberry", "Cutecumber", "Melown"]

for f in fun_fruits:
    print(f)
    for char in f:
        print(char)


