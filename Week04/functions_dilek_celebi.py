# Lambda fonksiyonu
custom_power = lambda base_val=0, /, exponent_val=1: base_val ** exponent_val

def custom_equation(
    num1: int = 0, num2: int = 0, /, power_x: int = 1, power_y: int = 1, *, divisor_val: int = 1
) -> float:
    """
    Bu fonksiyon (num1**power_x + num2**power_y) / divisor_val hesaplar.

    :param int num1: Birinci değişken, varsayılan 0
    :param int num2: İkinci değişken, varsayılan 0
    :param int power_x: num1'in üssü, varsayılan 1
    :param int power_y: num2'nin üssü, varsayılan 1
    :param int divisor_val: Bölücü, varsayılan 1
    :return: Hesaplamanın sonucu (num1**power_x + num2**power_y) / divisor_val
    :rtype: float
    :raises ZeroDivisionError: Eğer divisor_val 0 ise
    """
    return (num1 ** power_x + num2 ** power_y) / divisor_val

def fn_w_counter() -> (int, dict[str, int]):
    """
    Bu fonksiyon toplam çağrı sayısını ve modül bazında çağrı sayısını takip eder.
    """
    if not hasattr(fn_w_counter, "counter"):
        fn_w_counter.counter = (0, {})
    total_calls = fn_w_counter.counter[0]
    module_calls = fn_w_counter.counter[1]
    
    # Mevcut modülün adını al
    current_module = __name__
    total_calls += 1
    
    if current_module in module_calls:
        module_calls[current_module] += 1
    else:
        module_calls[current_module] = 1
    
    fn_w_counter.counter = (total_calls, module_calls)
    return fn_w_counter.counter

# Kullanım örnekleri
result1 = custom_power(3, 2)  # 3^2 = 9

result2 = custom_equation(2, 4, power_x=2, power_y=1, divisor_val=2)  # (2^2 + 4^1) / 2 = 6.0

call_count1 = fn_w_counter()  # (1, {'__main__': 1})
call_count2 = fn_w_counter()  # (2, {'__main__': 2})
