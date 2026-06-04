# A lambda function that calculates x raised to the power of e
# x is positional-only (must be given by position)
# e can be given as positional or keyword
custom_power = lambda x=0, /, e=1: x ** e


def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the mathematical equation.

    :param x: The first base value.
    :param y: The second base value.
    :param a: The exponent for x.
    :param b: The exponent for y.
    :param c: The divisor.
    :return: The result of the equation.
    """

    # Type checking to ensure all inputs are integers
    # This is required because tests expect TypeError for invalid types
    if not isinstance(x, int):
        raise TypeError("x must be int")
    if not isinstance(y, int):
        raise TypeError("y must be int")
    if not isinstance(a, int):
        raise TypeError("a must be int")
    if not isinstance(b, int):
        raise TypeError("b must be int")
    if not isinstance(c, int):
        raise TypeError("c must be int")

    # Perform the calculation: (x^a + y^b) / c
    return (x ** a + y ** b) / c


def fn_w_counter() -> (int, dict[str, int]):
    # Check if the function already has a counter attribute
    # If not, initialize it
    if not hasattr(fn_w_counter, "_count"):
        fn_w_counter._count = 0

    # Increment the counter each time the function is called
    fn_w_counter._count += 1

    # Get the module name (without package path if exists)
    # This ensures it matches the test expectation
    module_name = __name__.split(".")[-1]

    # Return a tuple:
    # 1. current call count
    # 2. dictionary with module name as key and count as value
    return fn_w_counter._count, {module_name: fn_w_counter._count}
