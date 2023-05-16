# to: else clause
my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
else:
    print('Iteration finished!')

print()
print('---')
print()


# to: else clause / Breal-Statement
my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
    break                  # es stoppt den loop direkt beim ersten durchlauf
else:
    print('Iteration finished!')

print()
print('---')
print()


i = 1
while i <= 5:
    print(i)
    if i == 3:          
        break               # bei 3. durchlauf macht es break
    i += 1
else:
    print('after finished')



print()
print('---')
print()


## to: comtinue statement

# i = 1
# while 1 <= 5:
#     if i == 3:
#         i += 1
#         continue             # irgendwas stimmt hier noch nicht
#     print(i)
#     i += 1


## continue in loops:
numbers = [1,2,3,4,5]

for number in numbers:
    if number == 3:
        continue
    print(number)

print()
print('-ITER--')
print()

## to: iteration and iter(), next()

my_list = [1,2,3,4,5]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))  # das ist letztes item.. noch eine zeile, dann gäbe es error



print()
print('---')
print()

import random

def d6():
    return random.randint(1,6)

d6_iter = iter(d6, 1)   # an 1 macht er StopIteration
print('iterator is called:',d6_iter)  # just to show this

for roll in d6_iter:
    print('randomziffern und wenn 1 dann stopiteration:',roll)

print()
print()
print('----Same but with lambda and without def:')
d6_iter = iter(lambda: random.randint(1,6), 1)   # an 1 macht er StopIteration
for roll in d6_iter:
    print('randomziffern und wenn 1 dann stopiteration:',roll)

print()
print('---')
print()

# implement a for loop with while
s = "ABC"
for char in s:
    print(char)

# emulating for loop (when there was no for loop in py)
s = "ABC"

it = iter(s)

while True:
    try:
        print(next(it)) 
    except StopIteration:
        del it     #release reference to iterator - iterator obj is discarde
        break
