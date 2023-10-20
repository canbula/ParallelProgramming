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


call_counter = 0
call_counts = {}

def fn_w_counter() -> (int, dict[str, int]):
    global call_counter
    call_counter += 1

    caller = fn_w_counter.__name__

    if caller in call_counts:
        call_counts[caller] += 1
    else:
        call_counts[caller] = 1

    return call_counter, call_counts
