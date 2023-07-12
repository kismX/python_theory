class Person:
    def __init__(self):
        self._name = None
        self._age = None

    def get_name(self): #Getter
        return self._name

    def get_age(self): #Getter
        return self._age

    def set_name(self, user_name): #Setter
        self._name = user_name

    def set_age(self, age):
        if age >= 0: #Constraint
            self._age = age
        else:
            raise ValueError('Age cannot be negative')

bob = Person()
bob.set_name('John')


print()
print("------------------------------------")
print()
print()

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

#When you use the @property decorator, 
#you define a method as a property of the class
#This method can be accessed like
#an attribute of an object



rect = Rectangle(1,2)

print(rect.width)   # hier braucht man keine () weil @property
print(rect.height) 
print(rect.__dict__)

print()

rect.height = 100
print(rect.height)

print(rect.__dict__)






print()
print()
print()
print()
print('-----simple descriptor--------------')
print()
print()


### Simple Descriptor

class Ten:
    def __get__(self, obj, cls=None):
        print(self) # instance of Ten
        print(obj) # instance of A
        print(cls)
        return 10

class A:
    y = Ten()

a = A()
a.y 


##### own property decorator

class my_property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, cls):
        return self.getter(obj)

class Test:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    # def width(self):
    #     return self._width
    
    # width = my_property(width)

    @my_property
    def width(self):
        return self._width

test = Test(10,2)
print(test.width)


print()
print()
print()
print()
print('-----abstraction / abstract methods--------------')
print()
print()

