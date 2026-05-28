# Multi-level inheritance is a type of inheritance where a class inherits from another derived class, forming a parent → child → grandchild relationship. In multi-level inheritance, the child class can access the properties and methods of both its parent class and its grandparent class. This allows for a more complex hierarchy of classes and promotes code reusability.


# Grandparent class
class Grandparent:
    def grandparent_property(self):
        print("Grandparent: House")


# Parent class inheriting from Grandparent
class Parent(Grandparent):
    def parent_property(self):
        print("Parent: Car")

# Child class inheriting from Parent
class Child(Parent):
    def child_property(self):
        print("Child: Bike")


# Create an instance of the Child class

obj = Child()

# Accessing properties from the grandparent class, parent class, and child class

obj.grandparent_property()
obj.parent_property()
obj.child_property()