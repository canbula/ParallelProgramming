import os


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("types")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])
    print(f"The module {f[:-3]} has been imported.")


def test_names():
    for f in files:
        assert "my_int" in dir(eval(f[:-3])), "my_int is not defined in " + f[:-3]
        assert "my_float" in dir(eval(f[:-3])), "my_float is not defined in " + f[:-3]
        assert "my_bool" in dir(eval(f[:-3])), "my_bool is not defined in " + f[:-3]
        assert "my_complex" in dir(eval(f[:-3])), (
            "my_complex is not defined in " + f[:-3]
        )


def test_types():
    for f in files:
        assert isinstance(eval(f[:-3]).my_int, int), "my_int is not an int in " + f[:-3]
        assert isinstance(eval(f[:-3]).my_float, float), (
            "my_float is not a float in " + f[:-3]
        )
        assert isinstance(eval(f[:-3]).my_bool, bool), (
            "my_bool is not a bool in " + f[:-3]
        )
        assert isinstance(eval(f[:-3]).my_complex, complex), (
            "my_complex is not a complex in " + f[:-3]
        )
