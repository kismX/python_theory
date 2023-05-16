# a = 10
# b = 0
# c = a/b 
# print(c)   

# ZeroDivisionError : division by zero

print("------------------------------")
print()
# handling exeptions


## CATCH ERRORS IN EACH LINE
try:
    x = int(input('Please give a number.'))
    print(x/0)
except ValueError:                              # akzeptieren der Fehlermeldung unn print
    print('Wrong type')
except ZeroDivisionError:
    print('Do not divide by Zero.')


## BEIDES ZUSAMMEN IN EINEM BLOCK
try:
    x = int(input('Please give a number.'))
    print(x/0)
except (ValueError, ZeroDivisionError):
    print('Error')



# man kann alle fehler, die es gibt, aber das ist sehr unklar, was für ein fehler war - schwer zu debuggen
try:
    x = int(input('Please give a number: '))
    print(1/x)
except:
    print('Error')


# also typ des errors anzeigen lassen:
try: 
    x = int(input('Pls giv a num: '))
    print(1/x)
except Exception as e:
    print("Error", e)


## Defining cleanup Actions (finally)
try: 
    1 + 'Hello'   
finally:
    print('Goodbye, world!')   # das hier sollte eigtl ausgegeben werden

print("This will not be executed.")


def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())




def dangerous_call(num):
    print(1+num)

def after_call():
    print('Everything alright')

try:
    dangerous_call('2')
    after_call()
except TypeError:
    print('TypeError')

try:
    dangerous_call('2')
except TypeError:
    print('TypeError')
else:
    after_call()



## Raising exceptions // Errors erstellen
# raise NameError('he there - aber muss keine nachricht hier stehen')

##

try:
    raise NameError('Hi there')
except NameError:
    print('An exception flew by!')
    raise



try:
   raise TypeError('Bla')
except TypeError('Bla'):
    print("cant do that")
    raise

