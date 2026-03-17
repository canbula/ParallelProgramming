from collections import defaultdict
import inspect
from typing import Tuple, Dict

_total_calls = 0
_caller_counts = defaultdict(int)

# 1. custom_power
custom_power = lambda x=0, e=1, / : x ** e

# 2. custom_equation
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
        Calculates a specific mathematical expression.
    
        :param x: positional-only integer, default 0
        :param y: positional-only integer, default 0
        :param a: positional-or-keyword integer, default 1
        :param b: positional-or-keyword integer, default 1
        :param c: keyword-only integer, default 1
        :return: result of (x**a + y**b) / c as float    
    """
n: Hesaplama sonucu float olarak doner.
    """
    return float((x**a + y**b) / c)

# 3. fn_w_counter
def fn_w_counter() -> Tuple[int, Dict[str, int]]:
    global _total_calls
    _total_calls += 1
    current_frame = inspect.currentframe()
    caller_frame = current_frame.f_back
    caller = caller_frame.f_globals.get('__name__', '<unknown>')
    _caller_counts[caller] += 1
    return _total_calls, dict(_caller_counts)
