print("\n--- Exercise( Overloading * for Scalar Multiplication ---\n")
# You can multiplay a number to a vector: (x,y) * c = (x*c, y*c)
# use the dunder method __ mul__ to add a scalar (number) to an instance of Vector2d (see notes)

class Vector2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, c):
        return f" Vector2d ({self.x * c}, {self.y * c})"


# Test:
vec2d = Vector2d(1,1)
# new_vec2d = vec2d * 10
print(vec2d.__mul__(10))    # --> Vector2d (10, 10)


print("\n--- Exercise( Overloading * for Scalar Multiplication II ---\n")
# In this exercise we now reverse the order of the operands.
# You can also multiplay a number to a vector:  c * (x,y)  = (x*c, y*c)
# use the dunder method __ rmul__ to add a scalar (number) to an instance of Vector2d
# research how __mul__  and __rmul__  work together

class Vector2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __rmul__(self, c):                                  # Multiplikation andersherum?
        return f" Vector2d ({c * self.x}, {c * self.y})"
    
vec2d = Vector2d(1,1)
# new_vec2d = 10 * vec2d 
print(vec2d.__rmul__(10))   # --> Vector2d (10, 10)


print("\n--- Exercise(Unary Operators ---\n")
# Look at the following expression:
# -(x,y) = (-x,-y)
# use __ neg__ to achieve the same behavior for our vector instances

class Vector2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __neg__(self):                                
        return f" Vector2d ({-self.x}, {-self.y})"
    
vec2d = Vector2d(1,1)
# neg_vec2d = -vec2d
print(vec2d.__neg__())


print("\n--- Task 4: Exercise(Overloading + for Vector Addition ---\n")
# - implement + mathematical vector operation
# (x1,y1) + (x2,y2) = (x1+x2, y1+y2)

class Vector2d:

    def __init__(self, x):
        self.x = x
    
    def __add__(self, other):                                
        return f" Vector2d ({self.x[0] + other.x[0]}, {self.x[1] + other.x[1]}, {self.x[2] + other.x[2]})"
    
#Test:
v1 = Vector2d([3,4,5])
v2 = Vector2d([6,7,8])
# v3  = v1 + v2           #---> Vector2d([9, 11, 13])

print(v1.__add__(v2))