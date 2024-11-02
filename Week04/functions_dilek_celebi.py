custom_power = lambda base=0, /, exponent=1: base**exponent

def custom_equation(val_x: int = 0, val_y: int = 0, /, exp_a: int = 1, exp_b: int = 1, *, divisor_c: int = 1) -> float:
    """
    Bu fonksiyon, özel bir denklemi hesaplar.
    :param val_x: Pozisyonel bir parametre, varsayılan değeri 0'dır.
    :param val_y: Pozisyonel bir parametre, varsayılan değeri 0'dır.
    :param exp_a: `val_x` için üstel, varsayılan değeri 1'dir.
    :param exp_b: `val_y` için üstel, varsayılan değeri 1'dir.
    :param divisor_c: Denklemin böleni, varsayılan değeri 1'dir.
    
    :type val_x: int
    :type val_y: int
    :type exp_a: int
    :type exp_b: int
    :type divisor_c: int
    :return: Özel denklemin sonucu ((val_x^exp_a) + (val_y^exp_b)) / divisor_c.
    :rtype: float
    """
    return (val_x**exp_a + val_y**exp_b) / divisor_c

def fn_w_counter() -> (int, dict[str, int]):
    """
    Bu fonksiyon, kaç kez çağrıldığını ve hangi çağırandan çağrıldığını sayar.
    :rtype: tuple(int, dict[str, int])
    """
    if not hasattr(fn_w_counter, "call_count"):
        setattr(fn_w_counter, "call_count", 0)
