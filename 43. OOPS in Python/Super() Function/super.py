# Super() = Super() is a built-in Python function used to call methods or constructors of the parent class from the child class. It allows you to access and invoke methods of the parent class without explicitly naming it, which is especially useful in cases of multiple inheritance. Super() is commonly used in the __init__ method of a child class to ensure that the parent class's constructor is called, allowing for proper initialization of the inherited attributes.


class Parent:
    def __init__(self):
        print("This is the parent class constructor.")
        
        
class Child(Parent):
    def __init__(self):
        super().__init__()  # This calls the __init__ method of the Parent class, allowing the Child class to inherit and execute the constructor of the Parent class.

        print("This is the child class constructor.")


obj = Child()  # Output: This is the parent class constructor









class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius



class Square(Shape):
    def __init__(self, color, is_filled, side_length):
        super().__init__(color, is_filled)
        self.side_length = side_length


class Triangle(Shape):
    def __init__(self, color, is_filled, side_length):
        super().__init__(color, is_filled)
        self.side_length = side_length




circle =  Circle("Red", True, 5)
square =  Square("Blue", False, 4)
triangle =  Triangle("Green", True, 3)

print(f"Circle: Color = {circle.color}, Is Filled = {circle.is_filled}, Radius = {circle.radius}")
print(f"Square: Color = {square.color}, Is Filled = {square.is_filled}, Side Length = {square.side_length}")
print(f"Triangle: Color = {triangle.color}, Is Filled = {triangle.is_filled}, Side Length = {triangle.side_length}")



circle.describe()  # Output: It is Red and filled.
square.describe()  # Output: It is Blue and not filled.
triangle.describe()  # Output: It is Green and filled.