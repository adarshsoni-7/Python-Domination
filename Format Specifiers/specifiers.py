# Format Specifiers in Pyhton

# Program to Add Two Numbers in Python

print("="*50)
print("Program: Adding Two Numbers in Python")
print("="*50)

# Method 1: Simple addition with direct input
print("\n--- Method 1: Simple Addition with User Input ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2

# Using format specifiers to display result
print(f"\nThe sum of {num1} and {num2} is {sum_result}")
print("Using % format specifier: %.2f + %.2f = %.2f" % (num1, num2, sum_result))
print("Using .format() method: {} + {} = {}".format(num1, num2, sum_result))


# Method 2: Function to add two numbers
print("\n--- Method 2: Using Function ---")
def add_numbers(a, b):
    """
    Function to add two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b


result = add_numbers(15, 25)
print(f"Result: 15 + 25 = {result}")
print("Formatted output: {:d}".format(result))


# Method 3: Using different format specifiers
print("\n--- Method 3: Different Format Specifiers ---")
num_a = 10
num_b = 20
sum_ab = num_a + num_b

# Integer format
print(f"Integer format: {num_a:d} + {num_b:d} = {sum_ab:d}")

# Float format
print(f"Float format: {num_a:.2f} + {num_b:.2f} = {sum_ab:.2f}")

# Exponential format
print(f"Exponential format: {num_a:.2e} + {num_b:.2e} = {sum_ab:.2e}")

# Percentage format (if applicable)
print(f"With padding: {num_a:5d} + {num_b:5d} = {sum_ab:5d}")


# Method 4: Class-based approach
print("\n--- Method 4: Using Calculator Class ---")
class Calculator:
    """Simple calculator class for addition."""
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        """Return the sum of num1 and num2."""
        return self.num1 + self.num2
    
    def display(self):
        """Display the addition result with formatting."""
        result = self.add()
        print(f"{self.num1} + {self.num2} = {result}")
        print(f"Formatted: {self.num1:.1f} + {self.num2:.1f} = {result:.1f}")


calc = Calculator(7.5, 12.3)
calc.display()


# Method 5: Lambda function
print("\n--- Method 5: Using Lambda Function ---")
add_lambda = lambda x, y: x + y

result_lambda = add_lambda(100, 50)
print(f"Lambda addition: 100 + 50 = {result_lambda}")
print("With format specifier: {:g}".format(result_lambda))


# Method 6: Using list comprehension
print("\n--- Method 6: Adding Multiple Numbers ---")
numbers = [5, 10, 15, 20]
total = sum(numbers)

print(f"Numbers: {numbers}")
print(f"Total sum: {total}")
print(f"Average: {total/len(numbers):.2f}")


print("\n" + "="*50)
print("Program completed successfully!")
print("="*50)
