# Duck typing in Python means:
# “If an object has the methods/attributes I need and they behave as expected, I use it, without caring what its class or parent is.”

# In other words, code is written to depend on behavior, not on type or inheritance.



# Inheritance vs duck typing: side‑by‑side
# 1. Using inheritance


class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

def make_it_speak(animal: Animal):
    animal.speak()

print("Using inheritance:")
d = make_it_speak(Dog())  # Output: Woof
m = make_it_speak(Cat())  # Output: Meow

# Here Dog and Cat inherit from Animal.

# make_it_speak is designed to take an Animal (or subclasses like Dog, Cat).

# The relation is: “Dog is an Animal”, “Cat is an Animal”.

# 2. Using duck typing





class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

class Robot:
    def speak(self):
        print("Beep boop")

def make_it_speak(thing):
    thing.speak()

print("\nUsing duck typing:")
d = make_it_speak(Dog()) # Output: Woof
m = make_it_speak(Cat()) # Output: Meow
r = make_it_speak(Robot()) # Output: Beep boop


# None of Dog, Cat, or Robot inherit from a common base class.

# make_it_speak does not care about their type, only that thing has a .speak() method.

# If it “walks like a duck and quacks like a duck” (has .speak()), the function is happy.



# Key differences in plain language:


# Inheritance style thinking:

# “All my animals must inherit from Animal, then I will accept Animal everywhere and call .speak() on it.”

# Duck typing style thinking:

# “I will write functions that just call .speak(). Anything with a .speak() method is fine, even if the classes are unrelated.”

# So: Inheritance organizes classes into a hierarchy and reuses code.

# Duck typing loosens coupling: functions only demand “you must have these methods,” not “you must be this type.”