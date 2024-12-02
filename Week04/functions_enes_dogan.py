import functools

custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates (x**a + y**b) / c.

    :param x: Base of the first term (default: 0)
    :param y: Base of the second term (default: 0)
    :param a: Power of the first term (default: 1)
    :param b: Power of the second term (default: 1)
    :param c: Constant divisor (default: 1)
    :return: Result of (x**a + y**b) / c
    """
    return (x ** a + y ** b) / c

# 3. Function for fn_w_counter
def fn_w_counter() -> (int, dict[str, int]):
    """
    Count the number of calls with caller information.

    :return: Tuple containing total number of calls and a dictionary
             with the caller name as key and the number of calls as value.
    """
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter.callers_dict = {}
    
    fn_w_counter.call_count += 1
    caller = __name__
    
    if caller in fn_w_counter.callers_dict:
        fn_w_counter.callers_dict[caller] += 1
    else:
        fn_w_counter.callers_dict[caller] = 1
    
    return fn_w_counter.call_count, fn_w_counter.callers_dict

if __name__ == "__main__":
    # Example usage of custom_power
    print("custom_power(2, 3):", custom_power(2, 3))
    print("custom_power(5):", custom_power(5))

    # Example usage of custom_equation
    print("custom_equation(2, 3, 2, 1, 1):", custom_equation(2, 3, 2, 1, 1))  
    print("custom_equation(2, 3):", custom_equation(2, 3))                    

    # Example usage of fn_w_counter
    print(fn_w_counter()) 
    print(fn_w_counter())  
