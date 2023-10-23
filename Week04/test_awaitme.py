import os
import inspect
import time
import random
import asyncio


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("awaitme")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    for f in files:
        assert "awaitme" in dir(eval(f[:-3])), "awaitme is not defined in " + f[:-3]

def test_callables():
    for f in files:
        assert callable(eval(f[:-3]).awaitme), "awaitme is not callable in " + f[:-3]

def test_awaitable():
    for f in files:
        @eval(f[:-3]).awaitme
        def dummy_awaitable():
            return 1
        assert asyncio.iscoroutinefunction(dummy_awaitable), "awaitme is not awaitable in " + f[:-3]
