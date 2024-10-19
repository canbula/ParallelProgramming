import os


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("info")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])
    print(f"The module {f[:-3]} has been imported.")


def test_names():
    for f in files:
        assert "student_id" in dir(eval(f[:-3])), (
            "student_id is not defined in " + f[:-3]
        )
        assert "full_name" in dir(eval(f[:-3])), "full_name is not defined in " + f[:-3]


def test_types():
    for f in files:
        assert isinstance(eval(f[:-3]).student_id, str), (
            "student_id is not a string in " + f[:-3]
        )
        assert isinstance(eval(f[:-3]).full_name, str), (
            "full_name is not a string in " + f[:-3]
        )
