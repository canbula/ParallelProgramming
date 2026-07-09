custom_power = lambda x, e: x ** e

def custom_equation(x, y, a, b, c):
    return (x**a + y**b) / c

def fn_w_counter():
    if not hasattr(fn_w_counter, "count"):
        fn_w_counter.count = 0
    fn_w_counter.count += 1
    return fn_w_counter.count, {__name__.split('.')[-1]: fn_w_counter.count}
