class NegativeRadiusError(Exception):
    pass


def calculate_area(radius: float) -> float:
    """Calculates the area for a given radius."""
    if radius < 0:
        raise NegativeRadiusError("You can't use a negative radius!")
    return 3.14159 * radius**2


try:
    print(calculate_area(-5))
except NegativeRadiusError:
    print("You have an error")


try:
    number = int(input("Please enter a number: "))
    result = 1 / number
except Exception as e:
    print(f"You have an error: {e}")
    print(str(e))
    print(repr(e))
    print(type(e).__name__)
else:
    print(f"The result is {result}")
finally:
    print("The end")
"""
except ValueError:
    print("You must give a number!")
except ZeroDivisionError:
    print("You can't divide a number by zero!")
"""
