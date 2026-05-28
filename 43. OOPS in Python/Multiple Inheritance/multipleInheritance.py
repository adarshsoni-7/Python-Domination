# Multiple inheritance is a feature in Python where a child class inherits properties and methods from more than one parent class. This allows the child class to combine the functionalities of multiple parent classes, making it more versatile and powerful. In multiple inheritance, the child class can access the attributes and methods of all its parent classes, and it can also override them if needed.

# Parent class 1
class Grandfather:
    def grandfather_skill(self):
        print("Grandfather's skill: Storytelling")


# Parent class 2
class Father:
    def father_skill(self):
        print("Father's skill: Gardening")




# Parent class 3
class Mother:
    def mother_skill(self):
        print("Mother's skill: Cooking")


# Child class inheriting from both parents

class Child(Grandfather, Father, Mother):
    def child_skill(self):
        print("Child's skill: Coding")




# Create an instance of the Child class

obj = Child()

# Accessing methods from both parent classes and the child class

obj.grandfather_skill()  # Output: Grandfather's skill: Storytelling
obj.father_skill()  # Output: Father's skill: Gardening
obj.mother_skill()  # Output: Mother's skill: Cooking
obj.child_skill()   # Output: Child's skill: Coding