class CustomError(Exception):
    pass


def calculate_area(radius):
    if radius < 0:
        raise CustomError("No negative radius!")
    return 3.14159 * radius**2


try:
    area = calculate_area(-5)
except Exception as e:
    print(f"Error : {type(e).__name__}")
