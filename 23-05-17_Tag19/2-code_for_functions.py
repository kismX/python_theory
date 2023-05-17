def multiply_number(a, b):
    result = a * b
    return result



## positional arg vs keyword arg

def format_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(format_name(last_name="Doe", first_name="john" )) #keyword arg
print(format_name('John', 'Doe')) # positional arg

print()
print()
print('----------------------------')

# default arg

def exponential(base, exponent=2):      # 2 is default value
    return base ** exponent

print(exponential(3))
print(exponential(3,3))

print()
print()

def calculate_price(unit_price, quantity, tax_rate=0.1): # the default values comes last
    return unit_price * quantity * (1 + tax_rate)

# wenn man alle s default values macht, braucht man beim callen in () nichts schreiben!!

price1 = calculate_price(10, 2)    #postional arguments
print(price1)
price2 = calculate_price(12, quantity=5, tax_rate=0.05)   # mixed poitional and keyword arg
price3 = calculate_price(12, quantity=5, tax_rate=0.05)   # mixed poitional and keyword arg

print()
print()
print('--------positional only par--------------------')



# positional only parameters
def add(a, b, /, c=5):   # alles vor  / is positional-.only
    return a + b + c

print(add(1,2,3))
print(add(1,2,c=3))
#add(2, b=1)     # geht nicht weil positional only



print()
print()
print('--------packing args--------------------')

# packing arguments

def add_numbers(*args):
    print("my_arguments: ", args)
    print(type(args))

result1 = add_numbers(1,2,3,4)

print('---')

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
result2 = add_numbers(1,2,3,4)
print(result2)


print('---')

def test_func(a, *args):
    print(a)
    print(args)            # args printet alle arg bis auf a

test_func(1,2,3,4)             

## the same:

a, *rest = 1,2,3,4
print(rest)                   # printed 2,3,4


print('----')

# packing keyword arguments

def get_keywords(**kwargs):
    print(kwargs)   # keywords arguments are stored in kwargs as a dictionary

get_keywords(bla=1, blu=2)  


# packing keyword arguments with other keyword ans poitoinal arguments before
def get_keywords(a, blob='hello', **kwargs):
    print(blob)  # keyword argument with default "hello"
    print(kwargs)   # keywords arguments are stored in kwargs as a dictionary

get_keywords(1, bla=1, blu=2)  




print()
print()
print('----------unpacking args------------------')
def calculate_total_price(unit_price, quantity, tax_rate):
    return unit_price * quantity * (1+ tax_rate)

# unpacking sequence of positional args
my_args = [1,2,3]
print(calculate_total_price(*my_args)) #put my_args as args
print(calculate_total_price(*[1,2,3]))  # will be same 
print(calculate_total_price(1,2,3))  # will print same 


# unpacking sequence of keyword args
my_args = {'unit_price': 8, 'quantity':3, 'tax_rate':0.05}
print(calculate_total_price(**my_args))
print(calculate_total_price(**{'unit_price':8, 'quantity':3, 'tax_rate':0.05}))

