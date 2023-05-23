print('-------Global scopes-----')
print()


x = 10     # difinesd as global scope

def print_global():
    print(x)     # takes global scope from before

print(print_global())  




print('-------local scopes-----')
print()

def print_local():
    y = 5             # defined as local scope
    print(y)

print_local()  # gibt dir none aus


print()
print()
print('-------global vs local scopes-----')
print()

z=10

def print_global_vs_local():
    z=5
    print(z)

print_global_vs_local()
print(z)




print()
print()
print('-------scopes lifespan-----')
print()

print(globals())  # alle globald werden dir ausgegeben


def print_local():
    y = 5             
    print(locals())   # goibt dir die local scopes aus, die in der func existieren
    print(y)

print_local()  



print()
print()
print('-------diff scope var to func-----')
print()

a = 10

def print_sum(b):
    c = a + b
    print(c)

print_sum(5)


###
a = 3

def   f1():
    print(a)
    print(b)

# f1()  # name error, b not defined
b = 6
f1()

### 

def f2(a):
    print('A', a)
    print(b)  # unboundedlocalError
    b = 9

#f2(3) #unboundedlocalerror

# print(b) was never run
# when python compiles the body of the func, it decides that b is a local var
# if we want the interpreter to treat b as global var and still assign a new value within the func use the *global* declatation

print()
print()
print('---reference---------')
print()

x = 5
print(id(x))


print()
print()
print('---func par as reference---------')
print()

def f(a,b):
    a += b
    return a

x = 1
y = 2
f(x,y)
print(x, y ) ## unchanged

my_list1 = [1,2]
my_list2 = [3,4]

f(my_list1,my_list2) 
print(my_list1, my_list2) ## changed

t =(10, 20)
u = (30, 40)
f(t, u)
print(t, u)
