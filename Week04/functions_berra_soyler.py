from typing import Callable, Tuple, Dict

custom_power: Callable[[int, int], int] = lambda x=0, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Compute a custom equation.

    :param x: An integer, positional-only, with default value 0
    :param y: An integer, positional-only, with default value 0
    :param a: An integer, positional-or-keyword, with default value 1
    :param b: An integer, positional-or-keyword, with default value 1
    :param c: An integer, keyword-only, with default value 1
    :return: Result of (x**a + y**b) / c as a float
    """
    return (x ** a + y ** b) / c

call_counter: Dict[str, int] = {}

def fn_w_counter() -> Tuple[int, Dict[str, int]]:
    """
    Count the number of function calls and return caller information.

    :return: A tuple containing the total number of calls and a dictionary with caller names as keys and call counts as values.
    """
    caller = "__main__"
    call_counter[caller] = call_counter.get(caller, 0) + 1
    return call_counter[caller], call_counter
