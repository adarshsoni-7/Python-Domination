# A decorator in Python is a special function that adds extra functionality to another function without modifying its original code.

# In simple words:

# "Decorators allow us to wrap an existing function with additional behavior while keeping the original function unchanged."


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Ice-cream is being prepared...")
        func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice-cream 🍨")

get_ice_cream("Hazelnut Chocolate") # get_ice_cream = add_sprinkles(get_ice_cream) -> get_ice_cream()

