## factorial function

def factorial(n):
    if n == 0:                            # exit condition: zu erst , weil sonst für immer läuft
        return 1
    else:                                 # recursive case: we return n times the factorial of n-1
        return n * factorial(n-1)
    

print(factorial(5))

# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
# For Example, 5! = 5 * 4 * 3 * 2 * 1 = 120.



print()
print()

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))



print()
print()

print('------ Fibbonacci ------')

# we call fibonacci(6)
# since 6 is not equal 0 or 1, we processeed to the elase block
# we call gibonacci(5) and fibonacci(4)
# fibonacci(5) is notequal to 0 or 1, so we proceed to the ease block
# 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


print()
print()

#shorter one:
def fibonacci_v2(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


print()
print()

print('------ countdown ------')

def countdown_iter(n):
    for i in range(n, 0, -1):
        print(i)



print()
print()

def countdown(n):
    if n == 0:
        return 1
    print(n)
    countdown(n-1)


countdown(11)

# 1. countdown(10) = countdown(9)= ... = countdown(0) = 1




