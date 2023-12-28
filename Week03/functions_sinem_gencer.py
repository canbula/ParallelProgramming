from typing import Tuple, Dict

custom_power = lambda x=0, /, e=1 : x**e
"""
Function to take power of a value.
:param x: Value that is being taken the power of.
:type x: float
:param e: Value that is the power.
:type e: float
:return: The result of equation x^e
"""

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
  """
  Function to calculate an equation and return float type value.
  :param x: Default value 0, positional-only.
  :type x: int
  :param y: Default value 0, positional-only.
  :type y: int
  :param a: Default value 1, positional and keyword.
  :type a: int
  :param b: Default value 1, positional and keyword.
  :type b: int
  :param c: Default value 1, keyword only.
  :type c: int
  :return: The result of equation.
  :rtype: float
  """
  return (x**a + y**b) / c

caller_counts = {}

def fn_w_caller() -> Tuple[int, Dict[str, int]]:
    """
    Function to return the number of calls with caller information.
    :return: A tuple containing an integer (total number of calls) and a dictionary (key: caller __name__, value: number of calls)
    :rtype: Tuple[int, Dict[str, int]]
    """
    caller_name = __name__
    caller_counts[caller_name] = caller_counts.get(caller_name, 0) + 1
    total_calls = sum(caller_counts.values())
    return total_calls, {caller_name: caller_counts[caller_name]}







  
