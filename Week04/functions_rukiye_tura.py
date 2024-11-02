custom_power = lambda x=0,/,e=1 : x**e


def custom_equation(x: int = 0, y: int = 0,/, a: int = 1, b: int = 1,*, c: int = 1) -> float:

    return (x**a + y**b) / c


def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = (0, {})
    counter_num = fn_w_counter.counter[0]
    counter_dict = fn_w_counter.counter[1]
    if __name__ in counter_dict:
        counter_dict[__name__] += 1
    else:
        counter_dict[__name__] = 1
    fn_w_counter.counter = (counter_num + 1, counter_dict)
    return fn_w_counter.counter
