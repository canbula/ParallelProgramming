import os
import pytest
import time


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("timer")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    for f in files:
        assert "Timer" in dir(eval(f[:-3])), "Timer is not defined in " + f[:-3]


def test_context_manager():
    for f in files:
        assert hasattr(eval(f[:-3]).Timer, "__enter__"), (
            "Timer is not a context manager in " + f[:-3]
        )
        assert hasattr(eval(f[:-3]).Timer, "__exit__"), (
            "Timer is not a context manager in " + f[:-3]
        )


def test_time_taken():
    for f in files:
        with eval(f[:-3]).Timer() as timer:
            time.sleep(2)
        assert 2.1 >= timer.end_time - timer.start_time >= 2, (
            "Timer is not working in " + f[:-3]
        )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
