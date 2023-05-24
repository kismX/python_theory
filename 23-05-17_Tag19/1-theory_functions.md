**TODAY**
- functions
- arguments vs parameters
- positional and kjeyword arguments
- packing and unpacking (*args ***kwargs)

# Functions
- make it more readable
- simplify code
- helps us to make our code DRY (Dont Repeat Yourself)
- way to organize and reuse codes in py
- performs specific task, and can be called multiple times


2 types of func:
1. **built-in functions**
e.g.
- print()
- isinstance()
- sorted()
- input()
- range() 
- ..
2. **custom functions**
- you create yourself
- can be tailored to perform specific tasks or operations

To **create a function** u need to follow a few basic steps:
- use the **def** keyword to define the func
- followed by the func name
- and any parameters the func may need
- use the return statement tp return any output of funk


``` python

def add_numbers(x,y):              # x, y are parameters
    result = x + y
    return result

```



To **call the function**
1. you use the func name
2. apply the () operator
3. and provide the parameters if applicable:


result = add_numbers(5, 10)     # 5, 10 are arguments.. 
print(result)


## how does interpreter work?
suppose we have

``` python
def multiply_number(a, b):
    result = a * b
    return result

```

1. **Function definition**
- the **def** keyword is used to define a func
- the func has two parameters a nd b
- paramters are def by the names that appear in a function definition
- arguments are the values actually passed to a func when calling it

2. **function call**
- call the func by passing two values a nd b as arguments

3. **input argument assignment**
- the interpreter assings the values 3 and 4 to the parameters a und b

4. **local variable assigenment**
- a new variable called result is createsd and assigned the value a * b
- this var is local to the func
- this var doesn't exist outside the func

5. **return statement**
- return keyword is used to send the value of result back to the calling code


**Input arguments**
- these are arguments that are assigned based on their position in the func call
- the first argument is assigned to the first par
- the 2nd arg is assigned to the 2nd par and so on

**keyword arguments**
- these are argzments that are explicitly assigned to parameter
- keyword args allow you to specify inputs in any other
- can be useful when u hav func with many input parameters

(bsp in .py)

- the keyword arg last_name="doe" and forst_name="john" are passed to the format_name func.
- they are assigned to the parameters first_name and last_name

**argument default value**
- u can set default values for the par using the = sign
- if no arg is passed in the func call, it will take on the default value

(sieh bsp in .py)


### Positional-Only parameters
- since py3.8, user-.defined signatures may specify positional-only par
- to define a func requiring positional par, use / in the parameter list:

(siehe .py)

# Packing and unpacking arguments
- there are two techniques that can be used to pass multipli arg to a func

**packing arguments**
- packing allows you to pass an ararbitrary number of arg to a func
- this is useful ehen u dont know ahed of time how many arg u need to pass
you can use:
1. the * operator to pack positional arguments
2. the ** operator to pack keyword arguments


**unpacking arguments**
- - unpacking allows u to pass a *sequence of arguemnts* to a func as seperate arguemnts
- this is useful when u hav a list, tuple, or dict if args that u want to pass to a func

you can use
1. the * operator to unpack a seq. of positional args
2. the ** op. to unpack a dict of keyword args.
