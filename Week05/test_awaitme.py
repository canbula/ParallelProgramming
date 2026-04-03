import os
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
        @eval(f[:-3]).awaitme
        def dummy_function(x: int = 0, y: int = 0) -> int:
            return x + y
        assert asyncio.iscoroutinefunction(dummy_awaitable), "awaitme is not awaitable in " + f[:-3]
        assert asyncio.iscoroutinefunction(dummy_function), "awaitme is not awaitable in " + f[:-3]

def test_values():
    for f in files:
        @eval(f[:-3]).awaitme
        def dummy_awaitable():
            return 1
        @eval(f[:-3]).awaitme
        def dummy_function(x: int = 0, y: int = 0) -> int:
            return x + y
        @eval(f[:-3]).awaitme
        def another_dummy_function(s: str = "") -> str:
            return s.capitalize()
        @eval(f[:-3]).awaitme
        def dummy_tuple_return() -> tuple:
            return 1, 2, 3
        async def just_a_tester():
            result = await dummy_awaitable()
            assert result == 1, "awaitme is not returning the correct value in " + f[:-3]
            result = await dummy_function(1, 2)
            assert result == 3, "awaitme is not returning the correct value in " + f[:-3]
            result = await another_dummy_function("bora")
            assert result == "Bora", "awaitme is not returning the correct value in " + f[:-3]
            result = await dummy_tuple_return()
            assert result == (1, 2, 3), "awaitme is not returning the correct value in " + f[:-3]
        asyncio.run(just_a_tester())


if __name__ == "__main__":
    test_names()
    test_callables()
    test_awaitable()
    test_values()
    print("Everything passed")
