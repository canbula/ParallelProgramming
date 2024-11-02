from collections import defaultdict

custom_power = lambda base=0, /, exponent=1: base**exponent

def custom_formula(x: int = 0, y: int = 0, /, exp_x: int = 1, exp_y: int = 1, *, divisor: int = 1) -> float:
    """
    :param x: Positional-only integer base for the equation, default is 0
    :param y: Positional-only integer base for the equation, default is 0
    :param exp_x: Positional-or-keyword integer exponent for x, default is 1
    :param exp_y: Positional-or-keyword integer exponent for y, default is 1
    :param divisor: Keyword-only integer divisor, default is 1
    :return: Result of (x**exp_x + y**exp_y) / divisor as a float
    """
    return (x**exp_x + y**exp_y) / divisor

def function_with_counter() -> (int, dict[str, int]):
    if not hasattr(function_with_counter, '_total_calls'):
        function_with_counter._total_calls = 0
        function_with_counter._module_calls = defaultdict(int)
    
    current_module = "__name__"
    function_with_counter._total_calls += 1
    function_with_counter._module_calls[current_module] += 1
    
    return function_with_counter._total_calls, dict(function_with_counter._module_calls)
