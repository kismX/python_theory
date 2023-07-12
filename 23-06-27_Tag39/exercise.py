# Exercise(Polymorphism - Negator):
# Write a class called Negator
#   use @singlesipatchmethod on the neg method
# if you use int as argument: return the negative value of this integer
# if you use bool:  return the oppsite boolean
# if you use str: return an empty string

from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError("Cannot negate arg")
    
    # if you use int as argument, return the negative value of this integer
    @neg.register
    def _(self, arg: int):
        return arg * -1

    # if you use bool, return the oppsite boolean
    @neg.register
    def _(self, arg: bool):
        return not arg 
    
    # if you use str, return an empty string
    @neg.register
    def _(self, arg: str):
        return ""

# Test the functions
obj = Negator()
print(obj.neg(15))
print(obj.neg(True))
print(obj.neg("Guckuck"))
# print(obj.neg(5.6))


print()
print()
print('-------------TASK 2--------------------------------')
print()
print()




# Exercise(Polymorphism - OverloadingII- Math):
# - Create a Python class called MathOperations with overloaded methods for:
# 1. addition (add()),
# 2. subtraction (subtract()), and
# 3. multiplication (multiply()).
# Each method should take different numbers of arguments and perform the corresponding operation.
# In your main() function, create an instance of the MathOperations class and demonstrate the polymorphic behavior by calling each method with different numbers of arguments.

import numpy as np

class MathOperations:
    def add(self, *args):
        return sum(args)

    def subtract(self, *args):
        first = args[0]
        for arg in args[1:]:
            first -= arg
        return first
    
    def multiply(self, *args):
        first = args[0]
        for arg in args[1:]:
            first *= arg 
        return first



def main():
    math_ops = MathOperations()

    # Addition
    result = math_ops.add(2, 3)
    print(f"Addition Result: {result}")

    result = math_ops.add(4, 6, 8)
    print(f"Addition Result: {result}")


    # Subtraction
    result = math_ops.subtract(10, 3)
    print(f"Subtraction Result: {result}")

    result = math_ops.subtract(20, 5, 3)
    print(f"Subtraction Result: {result}")


    # Multiplication
    result = math_ops.multiply(2, 5)
    print(f"Multiplication Result: {result}")

    result = math_ops.multiply(3, 4, 2)
    print(f"Multiplication Result: {result}")


main()