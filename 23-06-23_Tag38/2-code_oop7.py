class SillyClass:
    def __init__(self): 
        self.my_dict = {'a': 'A', 'b': 'B'}
        self.num = 5
    def __getitem__(self, key):
        print('key:', key)
        """ Determines behavior of `self[key]` """
        return self.my_dict[key]
        return [True, False, True, False]
    
    def __pow__(self, other):
        """ Determines behavior of `self ** other` """
        return self.num ** other
        return "Python Like You Mean It"


silly = SillyClass()
print(silly['a'])
print(silly ** 2)





import math

class Vector2d:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"Vector2d {(self.x, self.y)}" 

    def angle(self):
        # rad1 = math.atan(self.y/self.x)
        rad2 = math.atan2(self.y, self.x)
        degrees = math.degrees(rad2)
        return degrees
    
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
        return (self.x**2 + self.y**2)**(0.5)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
        return self.x == other.x and self.y == other.y
    
    def __bool__(self):
        return bool(abs(self))



class Vector2d:

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f"Vector2d {(self.x, self.y)}" 

    def angle(self):
        # rad1 = math.atan(self.y/self.x)
        rad2 = math.atan2(self.y, self.x)
        degrees = math.degrees(rad2)
        return degrees
    
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
        return (self.x**2 + self.y**2)**(0.5)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
        return self.x == other.x and self.y == other.y
    
    def __bool__(self):
        return bool(abs(self))

    def __hash__(self) -> int:
        my_tuple = (self.x, self.y)
        return hash(my_tuple)

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y




vec2d_1 = Vector2d(4, 3)
vec2d_2 = Vector2d(4, 3)

print(vec2d_1 @ vec2d_2)
print(bool(vec2d_1))
print(hash(vec2d_1))

print(vec2d_1 == vec2d_2)