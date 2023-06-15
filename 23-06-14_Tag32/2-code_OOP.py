# creating a class

class Dog:
    def __init__(self, name, breed, is_real_dog=True):  #contructor, used to initialize the attributes of obj
        self.name = name
        self.breed = breed
        if is_real_dog:
            self.legs = 4
        else:
            self.legs = 8
        
    # self is a reference to the object being created
    # name and breed are atttributes

    def bark(self):
    # the _bark_ method is a function can be called on an object of the Dog class to make it bark
        print(self.name)
        print("Woof!")


dog_obj = Dog("goofy", "australian dog", True)
print("adress dog_obj:", dog_obj.legs)


dog_obj.bark()


print()
print("-----Another ex.---------------")
print()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and iḿ {self.age} yrs old.")


bob = Person("Bob", 42)
bob.say_hello()

rob = Person("Rob", 29)
rob.say_hello()

print(bob)  # different store address
print(rob)  # diff store addres
print(__name__)


print()
print("-------------------")
print()

class BankAccount:
    def __init__(self, bla) -> None:
        self.balance = bla

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
    

my_bank = BankAccount(100)
# print(my_bank.balance)
my_bank.withdraw(1000)
# print(my_bank.balance)
my_bank.deposit(900)
# print(my_bank.balance)
        
class BankAccount2:
    def __init__(self, bla) -> None:
        self.balance = bla
        self.limit = -500

    def withdraw(self, amount):
        if self.balance - amount > self.limit:
            self.balance -= amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    

my_bank = BankAccount2(100)
print(my_bank.balance)
my_bank.withdraw(1000)
print(my_bank.balance)
my_bank.deposit(900)
print(my_bank.balance)



print('--------')

class BankAccount3:
    def __init__(self, bla) -> None:
        self.balance = bla
        self.limit = 0

    def withdraw(self, amount, limit):
        self.limit = limit
        if self.balance - amount > self.limit:
            self.balance -= amount
        else:
            print('limit reached')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('negatives not allowed')


my_bank = BankAccount3(100)
print(my_bank.balance)
my_bank.withdraw(1000, -600)
print(my_bank.balance)
my_bank.deposit(-900)
print(my_bank.balance)
