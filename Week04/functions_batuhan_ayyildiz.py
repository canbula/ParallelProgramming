custom_power = lambda x=1, /, e=1: x ** e
"""
Bu lambda fonksiyonu bir sayının kuvvetini hesaplar.

:param x: Taban sayı (varsayılan 1, sadece pozisyonel).
:param e: Üs değeri (varsayılan 1).
:return: x'in e kuvveti.
"""

def custom_equation(x: int = 1, y: int = 1, /, a: int = 2, b: int = 2, *, c: int = 1) -> float:
    """
    Bu fonksiyon (x'in a kuvveti) ile (y'nin b kuvveti)'nin toplamını c'ye böler.

    :param x: Birinci sayı (varsayılan 1, sadece pozisyonel).
    :param y: İkinci sayı (varsayılan 1, sadece pozisyonel).
    :param a: x'in üssü (varsayılan 2).
    :param b: y'nin üssü (varsayılan 2).
    :param c: Bölme işlemi için bölen (varsayılan 1, sadece keyword ile).
    :return: (x**a + y**b) / c işleminin sonucu.
    """
    return (x**a + y**b) / c

def fn_w_counter() -> (int, dict[str, int]):
    """
    Bu fonksiyon, kaç defa çağrıldığını ve hangi modülden çağrıldığını takip eden bir sayaç döndürür.

    :return: (çağrı sayısı, modül adı ile sayaç değerlerini tutan sözlük)
    """
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
