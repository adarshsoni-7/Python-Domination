# @property = Decorators used to define a method as a property (it can be accessed like an attribute). 
# Benefit: add additional logic when reading, writing, or deleting attributes. 
# Gives you getter, setter, and deleter method. 


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width: .1f} cm"

    @property
    def height(self):
        return f"{self._height: .1f} cm"
    

    @width.setter
    def width(self, newVal):
        if newVal <= 0:
            print("Width cannot be zero or negative.")
        else:
            self._width = newVal


    @height.setter
    def height(self, newVal):
        if newVal <= 0:
            print("Height cannot be zero or negative.")
        else:
            self._height = newVal

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.")


    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted.")

rectangle = Rectangle(5, 10)

rectangle.width = 7
rectangle.height = 9

print(rectangle._width)
print(rectangle._height)

del rectangle.width
del rectangle.height

#    ==================================================       Explaiantion       ==================================================

# 1. We define a class `Rectangle` with an initializer that takes `width` and `height` as parameters and assigns them to private attributes `_width` and `_height`.
# 2. We use the `@property` decorator to define getter methods for `width` and `height`, which return the values formatted as strings with units.
# 3. We use the `@width.setter` and `@height.setter` decorators to define setter methods for `width` and `height`, which include validation to ensure that the values are positive.
# 4. We use the `@width.deleter` and `@height.deleter` decorators to define deleter methods for `width` and `height`, which delete the respective attributes and print a message.


# Important Matter to understood: When we print rectangle.width, Python sees that width has a @property decorator.

# So instead of looking for an attribute called width, it automatically calls the width() method and returns its result. This allows us to access the width as if it were a regular attribute, while still having the ability to add extra logic in the 'getter' method if needed. Same applied for height.

# When we set rectangle.width = 7, Python sees that width has a @width.setter decorator. So instead of setting an attribute called width, it automatically calls the width() method with the new value (7 in this case) and executes the logic defined in the 'setter' method. This allows us to add validation or other logic when setting the value of width. Same applied for height.

# When we delete rectangle.width, Python sees that width has a @width.deleter decorator. So instead of deleting an attribute called width, it automatically calls the width() method and executes the logic defined in the 'deleter' method. This allows us to perform any necessary cleanup or actions when deleting the width attribute. Same applied for height.