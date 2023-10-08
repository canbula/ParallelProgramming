import first


def test_names():
    assert "my_first_int" in dir(first), "my_first_int is not defined"
    assert "my_first_float" in dir(first), "my_first_float is not defined"
    assert "my_first_bool" in dir(first), "my_first_bool is not defined"
    assert "my_first_complex" in dir(first), "my_first_complex is not defined"

def test_types():
    assert isinstance(first.my_first_int, int), "my_first_int is not an int"
    assert isinstance(first.my_first_float, float), "my_first_float is not a float"
    assert isinstance(first.my_first_bool, bool), "my_first_bool is not a bool"
    assert isinstance(first.my_first_complex, complex), "my_first_complex is not a complex"
