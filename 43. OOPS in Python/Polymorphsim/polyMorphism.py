# Polymorphism means 'same name but different behavior '.

# In Python, polymorphism allows the same method name or same interface to behave differently depending on the object that calls. 

# One method name, multiple behaviors. 


# TWO WAYS TO ACHIEVE POLYMORPHISM IN PYTHON:
# 1. Inheritance: Subclasses inherit methods from a parent class and can override them to provide specific implementations.
# 2. Duck Typing: If an object has the required method, it can be used in place of any object that has that method, regardless of its actual type.

from abc import ABC, abstractmethod

# Example of Polymorphism using Inheritance:

# Here Shape is the parent class, and Circle, Square, Triangle, and Pizza are subclasses that inherit from Shape. Each subclass implements the area method differently based on its shape. The loop at the end demonstrates polymorphism by calling the area method on different types of shapes without needing to know their specific types.

class Shape():
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Here Pizza class is inheriting the Circle class, and using it's area method in order to find the area of the pizza. This is an example of polymorphism, where the same method name (area) is used in different classes (Circle and Pizza) to perform different tasks based on the context of the object. Here now Pizza class can use the area method of Circle class and also use area method of it's own if needed.

class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings
         

shapes = [Circle(5), Square(4), Triangle(6, 8), Pizza("Pepperoni", 14)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.area()} cm²")  # This will call the appropriate area method based on the object type (Circle or Square or Triangle).

# Notice that the loop doesn't care where the object is, Circle or Rectangle or Triangle. It simply calls the area() method.




#                                       ========================== Explaination of important concepts =========================

# 1. Abstract Base Class (ABC): The Shape class is an abstract base class that defines a common interface for all shapes. It contains an abstract method area() that must be implemented by any subclass.

# 2. Method Overriding: Each subclass (Circle, Square, Triangle, and Pizza) provides its own implementation of the area() method, which is an example of method overriding. This allows each shape to calculate its area according to its specific formula by using area method on their own.








#                                       ========================== Duck Typing =========================

#                                 Duck typing = Another way to achieve polymorphism besides Inheritance 
#                                 Object must have the minimum necessary attributes/methods  
#                              "If it looks like a duck and quacks like a duck, then it must be a duck."


class Animal:
    alive = True



class Dog(Animal):
    def speak(self):
        print("Dog says: WOOF!")



class Cat(Animal):
    def speak(self):
        print("Cat says: MEOW!")


class Car():
    # def horn(self):
    #     print("HONK!")

    alive = False

    def speak(self):
        print("Car says: HONK!")


animals = [Dog(), Cat(), Car()]  


# Here Car hasn't any speak method, it will give an error: AttributeError: 'Car' object has no attribute 'speak'. Here duck typing comes in where we try to make the Car exactly behave like a Dog or Cat by adding a speak method to it. This way we can use the same code to call the speak method on all objects in the animals list without worrying about their specific types.


for animal in animals:
    animal.speak()
    print(animal.alive)  
# This will print True for all objects since they all inherit the alive attribute from the Animal class except Car class because it does not have isalive attribute. By adding alive attribute to Car class, we can make it behave like a Dog or Cat and print True for all objects in the animals list. This is an example of duck typing, where we can use any object that has the required method (speak) regardless of its actual type.