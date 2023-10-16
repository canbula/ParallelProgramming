import os
import inspect


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("functions")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    for f in files:
        assert "custom_power" in dir(eval(f[:-3])), "custom_power is not defined in " + f[:-3]
        assert "custom_equation" in dir(eval(f[:-3])), "custom_equation is not defined in " + f[:-3]
        assert "fn_w_counter" in dir(eval(f[:-3])), "fn_w_counter is not defined in " + f[:-3]

def test_callables():
    for f in files:
        assert callable(eval(f[:-3]).custom_power), "custom_power is not callable in " + f[:-3]
        assert callable(eval(f[:-3]).custom_equation), "custom_equation is not callable in " + f[:-3]
        assert callable(eval(f[:-3]).fn_w_counter), "fn_w_counter is not callable in " + f[:-3]

def test_custom_power():
    for f in files:
        sig = inspect.signature(eval(f[:-3]).custom_power)
        assert eval(f[:-3]).custom_power.__name__ == "<lambda>", \
            "custom_power is not a lambda function in " + f[:-3]
        assert 'x' in sig.parameters, \
            "custom_power has wrong parameters in " + f[:-3]
        assert 'e' in sig.parameters, \
            "custom_power has wrong parameters in " + f[:-3]
        assert sig.parameters['x'].kind == inspect._POSITIONAL_ONLY, \
            "custom_power has wrong kind in " + f[:-3]
        assert sig.parameters['e'].kind == inspect._POSITIONAL_OR_KEYWORD, \
            "custom_power has wrong kind in " + f[:-3]
        assert sig.parameters['x'].default == 0, \
            "custom_power has wrong default value in " + f[:-3]
        assert sig.parameters['e'].default == 1, \
            "custom_power has wrong default value in " + f[:-3]
        assert eval(f[:-3]).custom_power(2) == 2, \
            "custom_power is not working in " + f[:-3]
        assert eval(f[:-3]).custom_power(2, 3) == 8, \
            "custom_power is not working in " + f[:-3]
        assert eval(f[:-3]).custom_power(2, e=3) == 8, \
            "custom_power is not working in " + f[:-3]
        assert eval(f[:-3]).custom_power(49, e=0.5) == 7, \
            "custom_power is not working in " + f[:-3]

def test_custom_equation():
    for f in files:
        sig = inspect.signature(eval(f[:-3]).custom_equation)
        assert eval(f[:-3]).custom_equation.__doc__ is not None, \
            "custom_equation has no docstring in " + f[:-3]
        assert eval(f[:-3]).custom_equation.__doc__.count(":param") == 5, \
            "custom_equation has wrong docstring in " + f[:-3] + " (param)"
        assert eval(f[:-3]).custom_equation.__doc__.count(":return") == 1, \
            "custom_equation has wrong docstring in " + f[:-3] + " (return)"
        assert sig.return_annotation == float, \
            "custom_equation has wrong return annotation in " + f[:-3]
        assert 'x' in sig.parameters, \
            "custom_equation has wrong parameters in " + f[:-3]
        assert 'y' in sig.parameters, \
            "custom_equation has wrong parameters in " + f[:-3]
        assert 'a' in sig.parameters, \
            "custom_equation has wrong parameters in " + f[:-3]
        assert 'b' in sig.parameters, \
            "custom_equation has wrong parameters in " + f[:-3]
        assert 'c' in sig.parameters, \
            "custom_equation has wrong parameters in " + f[:-3]
        assert sig.parameters['x'].kind == inspect._POSITIONAL_ONLY, \
            "custom_equation has wrong kind for x in " + f[:-3]
        assert sig.parameters['y'].kind == inspect._POSITIONAL_ONLY, \
            "custom_equation has wrong kind for y in " + f[:-3]
        assert sig.parameters['a'].kind == inspect._POSITIONAL_OR_KEYWORD, \
            "custom_equation has wrong kind for a in " + f[:-3]
        assert sig.parameters['b'].kind == inspect._POSITIONAL_OR_KEYWORD, \
            "custom_equation has wrong kind for b in " + f[:-3]
        assert sig.parameters['c'].kind == inspect._KEYWORD_ONLY, \
            "custom_equation has wrong kind for c in " + f[:-3]
        assert sig.parameters['x'].annotation == int, \
            "custom_equation has wrong annotation for x in " + f[:-3]
        assert sig.parameters['y'].annotation == int, \
            "custom_equation has wrong annotation for y in " + f[:-3]
        assert sig.parameters['a'].annotation == int, \
            "custom_equation has wrong annotation for a in " + f[:-3]
        assert sig.parameters['b'].annotation == int, \
            "custom_equation has wrong annotation for b in " + f[:-3]
        assert sig.parameters['c'].annotation == int, \
            "custom_equation has wrong annotation for c in " + f[:-3]
        assert sig.parameters['x'].default == 0, \
            "custom_equation has wrong default value for x in " + f[:-3]
        assert sig.parameters['y'].default == 0, \
            "custom_equation has wrong default value for y in " + f[:-3]
        assert sig.parameters['a'].default == 1, \
            "custom_equation has wrong default value for a in " + f[:-3]
        assert sig.parameters['b'].default == 1, \
            "custom_equation has wrong default value for b in " + f[:-3]
        assert sig.parameters['c'].default == 1, \
            "custom_equation has wrong default value for c in " + f[:-3]
        try:
            eval(f[:-3]).custom_equation(1.5, 2.5)
        except TypeError as e:
            assert str(e).count("must") > 0, \
                "custom_equation has wrong raises in " + f[:-3]
        try:
            eval(f[:-3]).custom_equation(1, 2, c=1.5)
        except TypeError as e:
            assert str(e).count("must") > 0, \
                "custom_equation has wrong raises in " + f[:-3]
        assert eval(f[:-3]).custom_equation(1, 2) == 3, \
            "custom_equation is not working in " + f[:-3]
        assert eval(f[:-3]).custom_equation(1, 2, 3) == 3, \
            "custom_equation is not working in " + f[:-3]
        assert eval(f[:-3]).custom_equation(1, 2, 3, 4) == 17, \
            "custom_equation is not working in " + f[:-3]
        assert eval(f[:-3]).custom_equation(1, 2, 3, 4, c=5) == 3.4, \
            "custom_equation is not working in " + f[:-3]
        assert eval(f[:-3]).custom_equation(1, 2, 3, c=5, b=6) == 13, \
            "custom_equation is not working in " + f[:-3]

def test_fn_w_counter():
    for f in files:
        sig = inspect.signature(eval(f[:-3]).fn_w_counter)
        assert sig.return_annotation == (int, dict[str, int]), \
            "fn_w_counter has wrong return annotation in " + f[:-3]
        # call the function multiple times
        for i in range(1, 10):
            assert eval(f[:-3]).fn_w_counter() == (i, {f[:-3]: i}), \
                "fn_w_counter is not working in " + f[:-3]
        for i in range(10, 97):
            assert eval(f[:-3]).fn_w_counter() == (i, {f[:-3]: i}), \
                "fn_w_counter is not working in " + f[:-3]
        for i in range(97, 100):
            assert eval(f[:-3]).fn_w_counter() == (i, {f[:-3]: i}), \
                "fn_w_counter is not working in " + f[:-3]
