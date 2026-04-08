def custom_power(x=0, /, e=1):
    return x ** e





def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:


    for param_name, value in [('x', x), ('y', y), ('a', a), ('b', b), ('c', c)]:
        if not isinstance(value, int):
            raise TypeError(f"{param_name} must be an integer")

    return float((x ** a + y ** b) / c)


def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "count"):
        fn_w_counter.count = 0
        
    fn_w_counter.count += 1
    

    return fn_w_counter.count, {__name__: fn_w_counter.count}
