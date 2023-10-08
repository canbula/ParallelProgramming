import os


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("sequences")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    for f in files:
        assert "my_list" in dir(eval(f[:-3])), "my_list is not defined in " + f[:-3]
        assert "my_tuple" in dir(eval(f[:-3])), "my_tuple is not defined in " + f[:-3]
        assert "my_set" in dir(eval(f[:-3])), "my_set is not defined in " + f[:-3]
        assert "my_dict" in dir(eval(f[:-3])), "my_dict is not defined in " + f[:-3]


def test_types():
    for f in files:
        assert isinstance(eval(f[:-3]).my_list, list), "my_list is not a list in " + f[:-3]
        assert isinstance(eval(f[:-3]).my_tuple, tuple), "my_tuple is not a tuple in " + f[:-3]
        assert isinstance(eval(f[:-3]).my_set, set), "my_set is not a set in " + f[:-3]
        assert isinstance(eval(f[:-3]).my_dict, dict), "my_dict is not a dict in " + f[:-3]


def test_remove_duplicates():
    for f in files:
        assert eval(f[:-3]).remove_duplicates([1, 2, 3, 3, 4, 5, 5, 5, 6]) == [1, 2, 3, 4, 5, 6], \
            "remove_duplicates is not working in " + f[:-3]
        assert eval(f[:-3]).remove_duplicates([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6], \
            "remove_duplicates is not working in " + f[:-3]
        assert eval(f[:-3]).remove_duplicates([1, 1, 1, 1, 1, 1]) == [1], \
            "remove_duplicates is not working in " + f[:-3]
        assert eval(f[:-3]).remove_duplicates([]) == [], \
            "remove_duplicates is not working in " + f[:-3]


def test_list_counts():
    for f in files:
        assert eval(f[:-3]).list_counts([1, 2, 3, 3, 4, 5, 5, 5, 6]) == {1: 1, 2: 1, 3: 2, 4: 1, 5: 3, 6: 1}, \
            "list_counts is not working in " + f[:-3]
        assert eval(f[:-3]).list_counts([1, 2, 3, 4, 5, 6]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}, \
            "list_counts is not working in " + f[:-3]
        assert eval(f[:-3]).list_counts([1, 1, 1, 1, 1, 1]) == {1: 6}, \
            "list_counts is not working in " + f[:-3]
        assert eval(f[:-3]).list_counts([]) == {}, \
            "list_counts is not working in " + f[:-3]


def test_reverse_dict():
    for f in files:
        assert eval(f[:-3]).reverse_dict({1: 1, 2: 2, 3: 3}) == {1: 1, 2: 2, 3: 3}, \
            "reverse_dict is not working in " + f[:-3]
        assert eval(f[:-3]).reverse_dict({1: 2, 2: 3, 3: 4}) == {2: 1, 3: 2, 4: 3}, \
            "reverse_dict is not working in " + f[:-3]
        assert eval(f[:-3]).reverse_dict({1: 1, 2: 1, 3: 1}) == {1: 3}, \
            "reverse_dict is not working in " + f[:-3]
        assert eval(f[:-3]).reverse_dict({}) == {}, \
            "reverse_dict is not working in " + f[:-3]
