custom_power = lambda x=0, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    return (a * x + b * y) / c

counter = 0
def fn_w_counter() -> (int, dict[str, int]):
    counter += 1
    return counter, {"functions_1": counter}
