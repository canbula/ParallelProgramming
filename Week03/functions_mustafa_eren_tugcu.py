from collections import defaultdict


custom_power = lambda x = 0 , e = 1, /: x**e 

def custom_equation(x = 0, y = 0, /, a = 1 , b = 1 , * , c  = 1 ):
    """
    This function raises x to the power of a, 
    adds y to the power of b, 
    then divides this sum by c, 
    and returns the result as a floating-point number.
    
    :param x : First Number 
    :param y : Second Number 
    :param a : Third Number 
    :param b : Fourth Number 
    :param c : Fifth Number 
    :return: result as a floating-point number.
    """
    return float((x**a + y **b ) / c)


def fn_w_counter():
    caller_count = defaultdict(int)
    total_calls = 0
    
    def _fn_w_counter(caller_name):
        nonlocal total_calls
        caller_name = __import__('inspect').currentframe().f_back.f_globals['__name__']
        caller_count[caller_name] += 1
        total_calls += 1
        
    return _fn_w_counter, lambda: (total_calls, dict(caller_count))
