# Inheritance = In Python, inheritance allows us to define a class that inherits all the methods and properties from another class and extend or modify them in the derived class.

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")


    def sleep(self):
        print(f"{self.name} is sleeping.")





class Dog(Animal):  # We can also make derived class's own methods. Here, we are adding a new method bark() to the Dog class that is not present in the Animal class. We can use now both bark() and eat() methods with the dog instance because the Dog class inherits from the Animal class.

    def bark(self):
        print(f"{self.name} is barking.")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")


class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} is squeaking.")


dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Squeaky")

# dog.eat()
# dog.sleep()
# dog.is_alive = False  # We can also modify the properties of the parent class in the derived class. Here, we are setting the is_alive property of the dog instance to False.

# cat.eat()
# cat.sleep()

# mouse.eat()
# mouse.sleep()


dog.bark() # Output: Buddy is barking.
cat.meow() # Output: Whiskers is meowing.
mouse.squeak() # Output: Squeaky is squeaking.