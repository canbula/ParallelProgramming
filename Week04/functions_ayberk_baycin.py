import inspect

# 1. custom_power: Lambda function with positional-only and default values
# '/' işareti öncesindekilerin sadece pozisyonla (x=0 gibi değil, sadece 0) girilebileceğini belirtir.
custom_power = lambda x=0, /, e=1: x ** e

# 2. custom_equation: Complex function with specific parameter rules
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates the result of a custom mathematical equation.

    :param x: Positional-only base for first power
    :param y: Positional-only base for second power
    :param a: Exponent for x
    :param b: Exponent for y
    :param c: Keyword-only divisor
    :return: The result of (x**a + y**b) / c as a float
    """
    return float((x**a + y**b) / c)

# 3. fn_w_counter: Function that counts its callers
# Global değişkenler kullanarak çağrı sayılarını takip ediyoruz
_total_calls = 0
_caller_counts = {}

def fn_w_counter() -> tuple[int, dict[str, int]]:
    global _total_calls
    _total_calls += 1
    
    # Bir üst seviyedeki (çağıran) fonksiyonun ismini alır
    frame = inspect.currentframe().f_back
    caller_name = frame.f_globals.get('__name__', '__main__')
    
    _caller_counts[caller_name] = _caller_counts.get(caller_name, 0) + 1
    
    return _total_calls, _caller_counts
