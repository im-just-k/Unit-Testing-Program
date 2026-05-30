# math_operations.py

# Add function
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

# Subtract function
def subtract(a, b):
    """Returns the result of a minus b."""
    return a - b

# Multiply function
def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

# Divide function
def divide(a, b):
    """Returns the result of a divided by b, raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero") # Shows error message if division by 0 is attempted
    return a / b
