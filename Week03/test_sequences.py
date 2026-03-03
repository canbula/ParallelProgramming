import os


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("sequences")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])
    print(f"The module {f[:-3]} has been imported.")


def test_names():
    for f in files:
        assert "remove_duplicates" in dir(eval(f[:-3])), (
            "remove_duplicates is not defined in " + f[:-3]
        )
        assert "list_counts" in dir(eval(f[:-3])), (
            "list_counts is not defined in " + f[:-3]
        )
        assert "reverse_dict" in dir(eval(f[:-3])), (
            "reverse_dict is not defined in " + f[:-3]
        )


def test_types():
    for f in files:
        assert callable(eval(f[:-3]).remove_duplicates), (
            "remove_duplicates is not callable in " + f[:-3]
        )
        assert callable(eval(f[:-3]).list_counts), (
            "list_counts is not callable in " + f[:-3]
        )
        assert callable(eval(f[:-3]).reverse_dict), (
            "reverse_dict is not callable in " + f[:-3]
        )
        assert isinstance(eval(f[:-3]).remove_duplicates([1, 2, 3, 4, 5, 6]), list), (
            "remove_duplicates is not returning a list in " + f[:-3]
        )
        assert isinstance(eval(f[:-3]).list_counts([1, 2, 3, 4, 5, 6]), dict), (
            "list_counts is not returning a dict in " + f[:-3]
        )
        assert isinstance(eval(f[:-3]).reverse_dict({1: 1, 2: 2, 3: 3}), dict), (
            "reverse_dict is not returning a dict in " + f[:-3]
        )


def test_remove_duplicates():
    for f in files:
        assert eval(f[:-3]).remove_duplicates([1, 2, 3, 3, 4, 5, 5, 5, 6]) == [
            1,
            2,
            3,
            4,
            5,
            6,
        ], (
            "remove_duplicates is not working in " + f[:-3]
        )
        assert eval(f[:-3]).remove_duplicates([1, 2, 3, 4, 5, 6]) == [
            1,
            2,
            3,
            4,
            5,
            6,
        ], (
            "remove_duplicates is not working in " + f[:-3]
        )
        assert eval(f[:-3]).remove_duplicates([1, 1, 1, 1, 1, 1]) == [1], (
            "remove_duplicates is not working in " + f[:-3]
        )
        assert eval(f[:-3]).remove_duplicates([]) == [], (
            "remove_duplicates is not working in " + f[:-3]
        )


def test_list_counts():
    for f in files:
        assert eval(f[:-3]).list_counts([1, 2, 3, 3, 4, 5, 5, 5, 6]) == {
            1: 1,
            2: 1,
            3: 2,
            4: 1,
            5: 3,
            6: 1,
        }, (
            "list_counts is not working in " + f[:-3]
        )
        assert eval(f[:-3]).list_counts([1, 2, 3, 4, 5, 6]) == {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
        }, (
            "list_counts is not working in " + f[:-3]
        )
        assert eval(f[:-3]).list_counts([1, 1, 1, 1, 1, 1]) == {1: 6}, (
            "list_counts is not working in " + f[:-3]
        )
        assert eval(f[:-3]).list_counts([]) == {}, (
            "list_counts is not working in " + f[:-3]
        )


def test_reverse_dict():
    for f in files:
        assert eval(f[:-3]).reverse_dict({1: 1, 2: 2, 3: 3}) == {1: 1, 2: 2, 3: 3}, (
            "reverse_dict is not working in " + f[:-3]
        )
        assert eval(f[:-3]).reverse_dict({1: 2, 2: 3, 3: 4}) == {2: 1, 3: 2, 4: 3}, (
            "reverse_dict is not working in " + f[:-3]
        )
        assert eval(f[:-3]).reverse_dict({1: 1, 2: 1, 3: 1}) == {1: 3}, (
            "reverse_dict is not working in " + f[:-3]
        )
        assert eval(f[:-3]).reverse_dict({}) == {}, (
            "reverse_dict is not working in " + f[:-3]
        )
