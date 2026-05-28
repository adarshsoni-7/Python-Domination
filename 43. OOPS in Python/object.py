# Object = An instance of a class. It is a collection of data (variables) and methods (functions) that operate on the data. Objects are created from classes, which serve as blueprints for creating objects.

# Class = A blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. A class is like a template for creating objects.

class Car:
    def __init__(self, model, year, color, for_sale):
         
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"The {self.color} {self.model} is driven by someone.")

    def stop(self):
        print(f"The {self.color} {self.model} is stopped.")


car1 = Car("Toyota Camry", 2020, "Red", True)
print(car1.model)  # Output: Toyota Camry
car1.drive()  # Output: The Red Toyota Camry is driven by someone.
car1.stop()  # Output: The Red Toyota Camry is stopped.