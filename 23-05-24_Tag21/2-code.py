print('#### 1 ####')


def greet():
    a = 1
    b = 2
    print('hello', a+b)

hello1 = greet   # hello ist unn die func da es speicherort überbnimmt
hello2 = greet() # speichert die return value 
hello1() #printed hello und 3
print(greet)   # gibt dir den speicherort aus


print()

print('------pass func as args---------------')

def add_numbers(a,b):
    return a + b

def mult_numbers(a, b):
    return a* b

def math_operation(func, x, y):
    result = func(x, y)
    return result

result_add = math_operation(add_numbers, 2, 3)
print(result_add)

result_mult = math_operation(mult_numbers, 2, 3)
print(result_mult)


print()
print()
print('------return funcs as oputput from a func---------------')
print()
print()

def add_numbers(a,b):
    return a + b

def mult_numbers(a, b):
    return a* b

def math_operation(operation):
    if operation == "add":
        return add_numbers
    elif operation == "mult":
        return mult_numbers
    return None


result_add_func = math_operation("add")
print(type(result_add_func))  # type is a function
print(result_add_func(1,2))   # prints result 3

# shorter:
result_add_func = math_operation("add")(1, 2)  
print(result_add_func)



print()
print()
print('------closures---------------')
print()
print()

def make_averager():
    series = []    #free variable - can store values

    def averager(new_value):
        print(series)
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

avg = make_averager()  # what type is avg? --> function
print(avg)
print(avg(10))
print(avg(1))  #anderer avg weil free variable stores




print('---easier def in def--')



def outer_function(my_parameter1):
    def print_parameter1():
        print(my_parameter1)
    return print_parameter1

inner_func = outer_function("BLA")  # type: function
inner_func()    # prints "BLA"






print()
print('-def in def in def--')





def outer_function(my_parameter1):

    def print_parameter1(value1):
        #print(my_parameter1)
        #print(value1)

        def most_inner(value2):
            print(my_parameter1)
            print(value1)
            print(value2)
        return most_inner
    
    return print_parameter1


inner_func = outer_function("BLA")   #function
inner_func("Hello World")

outer_function("BLA")("World")("again")



