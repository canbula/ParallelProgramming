custom_power = lambda x=0,/, e=1 : x ** e

def custom_equation(x: int = 0 , y: int = 0 , /, a:int = 1, b: int=1 , * , c: int = 1) -> float :
  """
   This function returns the result of an operation based on the specified base and exponent values.

   :param x: First base value
   :param y: Second base value
   :param a: First exponent value
   :param b: Second exponent value
   :param c: Divisor value
   :return: (x**a + y**b)/c
  """
  return (x**a + y**b)/c

def fn_w_counter() -> (int, dict[str, int]):
  if not hasattr(fn_w_counter, "count"):
      fn_w_counter.count = 0
  fn_w_counter.count += 1
  return fn_w_counter.count, {__name__.split('.')[-1]: fn_w_counter.count}
