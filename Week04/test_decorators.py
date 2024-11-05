import os
import inspect
import time
import random


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("decorators")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    for f in files:
        assert "performance" in dir(eval(f[:-3])), "timer is not defined in " + f[:-3]

def test_callables():
    for f in files:
        assert callable(eval(f[:-3]).performance), "timer is not callable in " + f[:-3]

def test_performance():
    for f in files:
        @eval(f[:-3]).performance
        def dummy_timer(x):
            time.sleep(x)
        @eval(f[:-3]).performance
        def dummy_memory(x):
            return [random.randint(0, 100) for _ in range(x)]
        dummy_timer(1)
        assert eval(f[:-3]).performance.counter == 1, \
            "performance is not working in " + f[:-3] + " (counter)"
        assert eval(f[:-3]).performance.total_time > 1, \
            "performance is not working in " + f[:-3] + " (total_time)"
        dummy_timer(1)
        dummy_timer(2)
        dummy_timer(3)
        assert eval(f[:-3]).performance.counter == 4, \
            "performance is not working in " + f[:-3] + " (counter)"
        assert eval(f[:-3]).performance.total_time > 7, \
            "performance is not working in " + f[:-3] + " (total_time)"
        dummy_memory(1000000)
        assert eval(f[:-3]).performance.counter == 5, \
            "performance is not working in " + f[:-3] + " (counter)"
        assert eval(f[:-3]).performance.total_mem > 8.e6, \
            "performance is not working in " + f[:-3] + " (total_mem)"
