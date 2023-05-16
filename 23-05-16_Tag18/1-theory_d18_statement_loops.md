# Statements and Loops
- instruction in py that performs some action
- bsp: print statements; loop statements; assignment statements 
    - a = 5   # assign statement
    - print(5, 'bla')  # a print statement


## Expression
- combination of values var and operatoirs that provide a result
- ex. can be usedd in statements
- collections  of symbols that jointly express a quatity

operators:
- math-op: +, -, *, /, % 
- ()   # operator to call a func


BSP:
a = 5
b = 3
c = a+b    
len('ab')  

expressions:
1. a + b
2. len('ab')


## Iterations
- is the proess of repeating a set of instrucitons miltiple times
- in py i. is implemented using looops

#### Definite Iteration:
- its a type of loop that execute a set of instructions a fixed number of times

for i in range(5):
    print(i)


#### Indefinite iteration:
- a type of loop that executes a set of instr. until a specific condition is met.

i = 0
while i < 5:
    print(i)
    i += 1

### when eo use loops?
- .. see script


**NUmber range loop**
for i in range(5):
    print(1)


**collection based loop**
fruits = ['apple', 'banana', 'kiwi']

for friut in fruits:
    print(fruit)


### else clause
- see script


**Break Statement**
- terminate loop prematurely


**Continue Statement**
- used to skip particular iteration of a loop
- stops one interation and resumes at the next iteration



## Iterables
- obj that can be iterated over using a loop
- lists, tuples, string, dict, sets..

- an iterable is defined by implementing the __iter__() method
- __iter__() returns an iterator

## Iterator 
- obj. that produces a seq of values
- calue is retrieved one at a time, by using the **next** method

- iter _ method returns iterator obj itself
- nect method returns the next item in iteration 

## Iter()
- creatues an iterator from iterable (anscheinend nicht printable?)

    **next()**
    - iteratres over the list one item at a time
    - 
- iter() can also be called with two arguments:
1. argument must be callable (to be involved repeatly with no parameter)
2. 2. argument is a sentinel  (a marker value, when returned, causes t raise a **StopIteration**)


### for Loop and Iterators
behind the curtain iterators are therefore iter() are used:
-  if there was no **for statement** in python
- we had to emulate the for-machinery by hand with a while loos this is what we'd have to write: (siehe in .py)
