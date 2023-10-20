custom_power = lambda x=0, /, e=1: x**e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    a function that takes 5 arguments, 2 of which are optional, and returns a float

    :param x: (int) first value
    :param y: (int) second value
    :param a: (int) first exponent
    :param b: (int) second exponent
    :param c: (int) divisor
    :return: (float) result of the equation
    """
    return (x**a + y**b) / c


def count_calls():
    call_counts = {}  # Define a dict to store the call counts

    def decorator(func):
        def wrapper(*args, **kwargs):  # Define the wrapper function
            caller = func.__name__  # Get the name of the function being called
            if caller in call_counts:  # If the function has been called before
                call_counts[caller] += 1  # Increment the call count
            else:
                call_counts[caller] = 1  # Else, set the call count to 1
            total_calls = sum(call_counts.values())  # Sum the call counts
            return total_calls, call_counts  # Return the total calls and call counts
        return wrapper  # Return the wrapper function
    return decorator  # Return the decorator function


@count_calls()
def fn_w_counter():
    pass
