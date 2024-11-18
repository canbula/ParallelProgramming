# custom_power: Lambda function
custom_power = lambda x=0, e=1: x ** e

# custom_equation: Function with detailed type annotations and docstring
def custom_equation(
    x: int = 0, 
    y: int = 0, 
    a: int = 1, 
    b: int = 1, 
    *, c: int = 1
) -> float:
    """
    Computes the value of the custom equation.

    :param x: Positional-only integer, default is 0
    :param y: Positional-only integer, default is 0
    :param a: Positional-or-keyword integer, default is 1
    :param b: Positional-or-keyword integer, default is 1
    :param c: Keyword-only integer, default is 1
    :return: Float result of the equation (x**a + y**b) / c
    """
    return (x**a + y**b) / c

# fn_w_counter: Function with call counting and caller tracking
def fn_w_counter():
    """
    Counts the number of times this function is called,
    keeping track of caller information.

    :return: A tuple of the total number of calls (int) and
             a dictionary with caller names and their call counts.
    """
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
        fn_w_counter.caller_dict = {}

    fn_w_counter.call_count += 1
    caller = __name__
    if caller not in fn_w_counter.caller_dict:
        fn_w_counter.caller_dict[caller] = 0
    fn_w_counter.caller_dict[caller] += 1

    return fn_w_counter.call_count, fn_w_counter.caller_dict

# Örnek kullanımlar
if __name__ == "__main__":
    # custom_power örnekleri
    print(custom_power(2))             # 2
    print(custom_power(2, 3))          # 8
    print(custom_power(2, e=2))        # 4

    # custom_equation örnekleri
    print(custom_equation(2, 3))       # 5.0
    print(custom_equation(2, 3, 2))    # 7.0
    print(custom_equation(3, 5, a=2, b=3, c=4))  # 33.5

    # fn_w_counter örnekleri
    for i in range(10):
        fn_w_counter()
