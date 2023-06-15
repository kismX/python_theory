# attribute references

class MyClass:
    """ A simple class"""
    i = 12345

    def f(self):
        return "Hello World"
    
print(MyClass.i)
print(MyClass.f)
print(MyClass.__doc__)  # printed "A simple Class"


x = MyClass()
print(x.f)

def hallo():
    print "x"
 