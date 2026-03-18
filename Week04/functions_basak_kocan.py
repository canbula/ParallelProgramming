custom_power = lambda x = 0, /, e = 1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
  """
  This function calculates the value of the equation (x**a + y**b) / c.

  :param x: Positional-only base value for the first term, default value is 0.
  :param y: Positional-only base value for the second term, default value is 0.
  :param a: Exponent for 'x', default value is 1.
  :param b: Exponent for 'y', default value is 1.
  :param c: Divisor of the equation, default value is 1.

  :type x: int
  :type y: int
  :type a: int
  :type b: int
  :type c: int

  :return: The result of the custom equation (x**a + y**b) / c.
  :rtype: float
  """
  return (x**a + y**b) / c

def fn_w_counter() -> (int, dict[str, int]):
  if not hasattr(fn_w_counter, "call_count"):
    fn_w_counter.call_count = 0
    fn_w_counter.callers_dict = {}
  
  fn_w_counter.call_count += 1
  caller = __name__

  if caller in fn_w_counter.callers_dict:
    fn_w_counter.callers_dict[caller_name] += 1
  else:
    fn_w_counter.callers_dict[caller_name] = 1
  
  return fn_w_counter.call_count, fn_w_counter.callers_dict
