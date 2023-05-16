
### Exceptions ###

    Exceptions are a way of handling errors that occur during program execution in Python.

    When an error occurs in Python, an exception is raised, which interrupts the normal flow of the program.

    It transfers control to an exception handler.

    If there is no exception handler present, the program terminates with an error message.

    Python also provides built-in exceptions that are raised for specific errors.

    (Python provides a built-in Exception class that can be used to create custom exceptions. We will talk about it after the OOP Module)

**Some of the built-in exceptions in Python include:**
  Exception 	Description
- SyntaxError: 	raised when there is a syntax error in the code
- NameError: 	raised when a variable is not defined
- TypeError: 	raised when an operation or function is applied to an object of inappropriate type
- ValueError: 	raised when an operation or function receives an argument of the correct type but an inappropriate value
- ZeroDivisionError: 	raised when division by zero occurs
Scenarios when Exception might occur

    A file does not exist, and you want to read data from the file.
    You want to convert a string to an integer, but the string is not a valid integer.
    You want to access an element of a list or dictionary that does not exist.
    You want to divide a number by zero.
    You want to open a network connection, but the connection fails.
    You want to access a database, but the database is not available.
    You want to access a website, but the website is down.
    You want to access a resource that requires authentication, but you are not authenticated.
    You want to perform an operation that is not supported on a particular platform or operating system.
    You want to access a resource that does not have the necessary permissions or access rights.


**Errors and Exceptions**
There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

- Syntax Errors

    also called parsing errors

- Exceptions
Even if a statement or expression is syntactically correct, it may cause an error.

An exception in python is an event that occurs during the execution of programs that disrupt the normal flow of execution.

    Exceptions help developers to debug their code (Standardized error handling)
    Cleaner code
    Robust application

exceptions are object and contain:

    Error type (exception name)
    An error message describing the error event

Unhandled exceptions result in error messages consisting of:

    exception type
    error message
    error message showing the context where the exception occurred, in the form of a stack traceback

a=10
b=0
c=a/b
print(c)

---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
/home/dci-student/PYDCI/p23_e02_live-code/PYTHON/2.04_EXCEPTION/exceptions.ipynb Cell 7 in 3
      <a href='vscode-notebook-cell:/home/dci-student/PYDCI/p23_e02_live-code/PYTHON/2.04_EXCEPTION/exceptions.ipynb#Y102sZmlsZQ%3D%3D?line=0'>1</a> a=10
      <a href='vscode-notebook-cell:/home/dci-student/PYDCI/p23_e02_live-code/PYTHON/2.04_EXCEPTION/exceptions.ipynb#Y102sZmlsZQ%3D%3D?line=1'>2</a> b=0
----> <a href='vscode-notebook-cell:/home/dci-student/PYDCI/p23_e02_live-code/PYTHON/2.04_EXCEPTION/exceptions.ipynb#Y102sZmlsZQ%3D%3D?line=2'>3</a> c=a/b
      <a href='vscode-notebook-cell:/home/dci-student/PYDCI/p23_e02_live-code/PYTHON/2.04_EXCEPTION/exceptions.ipynb#Y102sZmlsZQ%3D%3D?line=3'>4</a> print(c)

ZeroDivisionError: division by zero

The error message will contain the following information:

    The type of the exception: ZeroDivisionError
    A brief description of the error: division by zero
    The line number where the error occurred: c=a/b

    The first line of the error message (Traceback (most recent call last)) indicates the start of the traceback.

    The second line of the error message (File "/home/dci-student/PYDCI/p23_e02_live-code/PYTHON/2.04_EXCEPTION/except.py") indicates the file name and line number where the error occurred. (line 3, in module)

    The third line of the error message (c = a/b) shows the line of code that raised the exception.

    The fourth line of the error message (ZeroDivisionError: division by zero) indicates the type of the exception ( ZeroDivisionError) and a brief description of the error (division by zero).

**Handling Exceptions**

You can handle selected Exceptions:

try:
    x = int(input('Please give a number.'))
except ValueError:
    print('Wrong type)

try:
    x = int(input('Please give a number.'))
    #print(x/0)
except ValueError:
    print('Wrong type')

---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
Cell In [5], line 3
      1 try:
      2     x = int(input('Please give a number.'))
----> 3     print(x/0)
      4 except ValueError:
      5     print('Wrong type')

ZeroDivisionError: division by zero

The try statement works as follows:

    First, the try clause is executed.
    If no exception occurs, the except clause is skipped and execution of the try statement is finished.
    If an exception occurs during execution of the try clause, the rest of the try clause is skipped and the except clause is executed
    If an exception occurs which does not match the exception named in the except clause, it is an unhandled exception and execution stops

An except clause may name multiple exceptions as a parenthesized tuple, for example:

try:
    x = int(input('Please give a number.'))
    print(x/0)
except (ValueError, ZeroDivisionError):
    print('Error')

Error

try:
    x = int(input('Please give a number.'))
    print(x/0)
except ValueError:
    print('give me the right value')
except ZeroDivisionError:
    print('do not divide by zero')

give me the right value

You can also catch all errors at once, but this considered as bad practice.

try:
    x = int(input('Please give a number.'))
    print(x/0)
except:
    print('Error')

Error

try:
    x = int(input('Please give a number.'))
    print(x/0)
except Exception as e:
    print('Error', e)

Error invalid literal for int() with base 10: 'a'

Defining Clean-up Actions (finally)

The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances.

try:
    1 + 'Hello'
finally:
    print('Goodbye, world!')

Goodbye, world!

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [12], line 2
      1 try:
----> 2     1 + 'Hello'
      3 finally:
      4     print('Goodbye, world!')

TypeError: unsupported operand type(s) for +: 'int' and 'str'

    The finally clause runs whether or not the try statement produces an exception.
    If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement.

def bool_return():
    try:
        return True
    finally:
        return False

bool_return()

False

    the else clause can be also be used in try statements
    the else block will run only if no exception is raised in the try block.

Consider the following code:

def dangerous_call(num):
    print(1+num)

def after_call():
    print('everything alright')

try:
    dangerous_call('2')
    after_call()
except TypeError:
    print('Type error')

Type error

For clarity, the body of a try block should only have the statements that may generate the expected exceptions. This is better

try:
    dangerous_call(2)
except TypeError:
    print('Type error')
else:
    after_call()

3
everything alright

the try block is guarding against possible errors in dangerous_call
Raising exceptions

The raise statement allows the programmer to force a specified exception to occur.

raise SomeExceptionClass(<value>)

raise NameError('HiThere')

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In [22], line 1
----> 1 raise NameError('HiThere')

NameError: HiThere

# raise NameError()
raise NameError

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In [24], line 2
      1 # raise NameError()
----> 2 raise NameError

NameError: 

If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception:

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

An exception flew by!

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In [25], line 2
      1 try:
----> 2     raise NameError('HiThere')
      3 except NameError:
      4     print('An exception flew by!')

NameError: HiThere

Exercise 1

    Write a program that prompts the user for a number. The number should divide the number 1. Handle the ZeroDivisionError exception and print an error message.
    The program will keep prompting the user to enter a number until a non-zero number is entered.

Hint:

    use a while loop
    research on the keyword: break

while True:
    try:
        num = int(input("Enter a number: "))
        result = 1 / num
        print(result)
    except ZeroDivisionError:
        print("Error: Cannot divide by 0.")
    else:
        break

Error: Cannot divide by 0.
1.0

Exercise 2

    Write a program that prompts the user to enter two numbers and performs division.
    Handle the ValueError exception if the user inputs a non-numeric value.

Note: The program will keep prompting the user to enter two numbers until a non-zero numeric value is entered as the second number.

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print(f"{num1}/{num2} = {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")
    except ZeroDivisionError:
        print("Error: Cannot divide by 0.")
    else:
        break

Error: Invalid input. Please enter a numeric value.
Error: Invalid input. Please enter a numeric value.
Error: Cannot divide by 0.
1/1 = 1.0

Exercise:

    Write a program that prompts the user to enter a list of integers and computes the average.
    Handle the ValueError exception if the user inputs a non-numeric value.

Note: The program assumes that the user enters a comma-separated list of integers. If the user enters a list with a different separator, the program will not be able to parse the input and may raise other exceptions.

while True:
    try:
        nums = input("Enter a list of integers, separated by commas: ").split(',')
        nums = [int(num) for num in nums]  #use for loop instead
        avg = sum(nums) / len(nums)
        print(f"Average: {avg}")
    except ValueError:
        print("Error: Invalid input. Please enter a list of integers, separated by commas.")
    else:
        break

Error: Invalid input. Please enter a list of integers, separated by commas.
Error: Invalid input. Please enter a list of integers, separated by commas.
Average: 1.0

--------------------------------------------------------------------- FOR LATER AFTER THE OOP MODULE ------------
Exception classes: Custom exceptions

Sometimes we have to define and raise exceptions that are not provided natively by Python. Such type of exceptions are called user-defined exception or customized exception.

class UnderAgeError(Exception):
    pass

raise UnderAgeError('Wrong Age')

---------------------------------------------------------------------------
UnderAgeError                             Traceback (most recent call last)
Cell In [26], line 4
      1 class UnderAgeError(Exception):
      2     pass
----> 4 raise UnderAgeError('Wrong Age')

UnderAgeError: Wrong Age

    We can customize the classes by accepting arguments as per our requirements.
    Exception classes can be defined which do anything any other class can do, but are usually kept simple
    Many standard modules define their own exceptions

class NegativeAgeError(Exception):
    # def __init__(self, age):
    #     self.message = f"Age should not be negative. Age was {age}."
    #     super().__init__(self.message)

raise NegativeAgeError(-23)

---------------------------------------------------------------------------
NegativeAgeError                          Traceback (most recent call last)
Cell In [28], line 6
      3         self.message = f"Age should not be negative. Age was {age}."
      4         super().__init__(self.message)
----> 6 raise NegativeAgeError(-23)

NegativeAgeError: Age should not be negative. Age was -23.

Exception class hierarchy

    Python has arranged the built-in exception into a class hierarchy using inheritance.
    Therefore, any class of exceptions used in an exception statement will also catch errors from its corresponding sub-class as well.

IndexError.__mro__

(IndexError, LookupError, Exception, BaseException, object)

KeyError.__mro__

(KeyError, LookupError, Exception, BaseException, object)

try:
    raise IndexError('TEST')
except LookupError as err:
    print('1.exception', err)

1.exception TEST

try:
    raise KeyError('TEST')
except LookupError as err:
    print('1.exception', err)

1.exception 'TEST'

try:
    raise LookupError('TEST')
except KeyError as err:
    print('1.exception', err)

---------------------------------------------------------------------------
LookupError                               Traceback (most recent call last)
Cell In [33], line 2
      1 try:
----> 2     raise LookupError('TEST')
      3 except KeyError as err:
      4     print('1.exception', err)

LookupError: TEST

