import os


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("pyramid")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])
    print(f"The module {f[:-3]} has been imported.")


def test_names():
    for f in files:
        assert "calculate_pyramid_height" in dir(eval(f[:-3])), (
            "calculate_pyramid_height is not defined in " + f[:-3]
        )


def test_types():
    for f in files:
        assert callable(eval(f[:-3]).calculate_pyramid_height), (
            "calculate_pyramid_height is not callable in " + f[:-3]
        )
        assert isinstance(eval(f[:-3]).calculate_pyramid_height(1), int), (
            "calculate_pyramid_height is not returning an int in " + f[:-3]
        )


def test_calculate_pyramid_height():
    for f in files:
        assert eval(f[:-3]).calculate_pyramid_height(1) == 1, (
            "calculate_pyramid_height is not working in " + f[:-3]
        )
        assert eval(f[:-3]).calculate_pyramid_height(2) == 1, (
            "calculate_pyramid_height is not working in " + f[:-3]
        )
        assert eval(f[:-3]).calculate_pyramid_height(6) == 3, (
            "calculate_pyramid_height is not working in " + f[:-3]
        )
        assert eval(f[:-3]).calculate_pyramid_height(20) == 5, (
            "calculate_pyramid_height is not working in " + f[:-3]
        )
        assert eval(f[:-3]).calculate_pyramid_height(100) == 13, (
            "calculate_pyramid_height is not working in " + f[:-3]
        )
        assert eval(f[:-3]).calculate_pyramid_height(1000) == 44, (
            "calculate_pyramid_height is not working in " + f[:-3]
        )
        assert eval(f[:-3]).calculate_pyramid_height(10000) == 140, (
            "calculate_pyramid_height is not working in " + f[:-3]
        )
        assert eval(f[:-3]).calculate_pyramid_height(100000) == 446, (
            "calculate_pyramid_height is not working in " + f[:-3]
        )
