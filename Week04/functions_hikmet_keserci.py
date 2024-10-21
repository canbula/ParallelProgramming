custom_power = lambda x = 0, /, e = 1: x**e
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
  """
  Calculates a custom equation: (x**a + y**b)) / c

  :param x: Positional-only integer, default is 0
  :param y: Positional-only integer, default is 0
  :param a: Positional-or-keyword integer, default is 1
  :param b: Positional-or-keyword integer, default is 1
  :param c: Keyword-only integer, default is 1

  :return: The result of the equation as a float
  """
  return (x**a + y**b)/c

def fn_w_counter():
  """
  Keeps track of the number of times the function has been called.

  :return: A tuple containing:
          - Total number of calls (int)
          - A dictionary with caller information (function names as keys and call counts as values)
  """
  fn_w_counter.counter += 1
  fn_w_counter.calls[__name__] = fn_w_counter.calls.get(__name__, 0) + 1
  return fn_w_counter.counter, fn_w_counter.calls

# Initialize the function's attributes
fn_w_counter.counter = 0
fn_w_counter.calls = {}
