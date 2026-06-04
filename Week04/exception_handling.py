"""
try:
    # Code that may raise an exception
except Exception as e:
    # Code to handle the exception
else:
    # Code to execute if no exception is raised
finally:
    # Code that will be executed regardless of the result
"""

# Example 1: Handling exceptions
try:
    1 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Example 2: Handling multiple exceptions
try:
    number = int(input("Enter a number: "))
    result = 1 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Example 3: Handling all exceptions
try:
    number = int(input("Enter a number: "))
    result = 1 / number
except Exception as e:
    print("An error occurred:", e)


# Example 4: Using else block
try:
    number = int(input("Enter a number: "))
    result = 1 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("The result is:", result)


# Example 5: Using finally block
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully.")
    print("Content:", content)
finally:
    file.close()
    print("File closed.")


# Example 6: Raising exceptions
def calculate_area(radius):
    if radius < 0:
        raise ValueError("No negative radius!")
    return 3.14 * radius**2


try:
    area = calculate_area(-5)
except ValueError as e:
    print("An error occurred:", e)


# Example 7: Custom exceptions
class NegativeRadiusError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} is a negative radius."


def calculate_area(radius):
    if radius < 0:
        raise NegativeRadiusError(radius)
    return 3.14 * radius**2


try:
    area = calculate_area(-5)
except NegativeRadiusError as e:
    print("An error occurred:", e)
