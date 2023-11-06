import os
import numpy as np


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("pi")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    for f in files:
        assert "next_pi" in dir(eval(f[:-3])), "next_pi is not defined in " + f[:-3]


def test_callables():
    for f in files:
        assert callable(eval(f[:-3]).next_pi), "next_pi is not callable in " + f[:-3]


def test_generators():
    for f in files:
        gen = eval(f[:-3]).next_pi()
        assert iter(gen) is gen, "next_pi is not generator in " + f[:-3]


def test_approaching():
    for f in files:
        np.random.seed(7)
        gen = eval(f[:-3]).next_pi()
        pi_estimate = next(gen)
        for _ in range(1000):
            pi_estimate = next(gen)
        assert np.isclose(pi_estimate, np.pi, atol=0.1), (
            "next_pi is not approaching to pi in " + f[:-3]
        )


if __name__ == "__main__":
    test_names()
    test_callables()
    test_generators()
    test_approaching()
    print("Everything passed")
