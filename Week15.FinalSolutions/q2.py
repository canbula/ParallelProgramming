import pytest
import sys
import multiprocessing
import asyncio
import threading


def function_1() -> int:
    return multiprocessing.cpu_count()


async def function_2(functions: list[callable], dummy_list: list[int]) -> None:
    threads = []
    for f in functions:
        threads.append(threading.Thread(target=f, args=(dummy_list,)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    for f in functions:
        f(dummy_list)
    await asyncio.sleep(0)


def dummy_function_1(dummy_list: list[int]) -> None:
    if not threading.current_thread() == threading.main_thread():
        dummy_list.append(1)


def dummy_function_2(dummy_list: list[int]) -> None:
    if not threading.current_thread() == threading.main_thread():
        dummy_list.append(2)


def dummy_function_3(dummy_list: list[int]) -> None:
    if not threading.current_thread() == threading.main_thread():
        dummy_list.append(3)


def test_imported_modules():
    list_of_modules = ["multiprocessing", "asyncio", "threading"]
    for module in list_of_modules:
        assert module in dir(sys.modules[__name__]), f"{module} is not imported"


def test_the_type_of_functions():
    assert callable(function_1), "function_1 is not a function"
    assert asyncio.iscoroutinefunction(function_2), "function_2 is not a coroutine"


def test_function_1():
    assert isinstance(function_1(), int), "function_1 does not return an int"
    assert function_1() == multiprocessing.cpu_count(), "function_1 does not return the correct value"


def test_function_2():
    dummy_list = []
    functions = [dummy_function_1, dummy_function_2, dummy_function_3]
    asyncio.run(function_2(functions, dummy_list))
    assert len(dummy_list) == 3, "function_2 does not run the functions in parallel"
    assert dummy_list == [1, 2, 3], "function_2 does not run the functions in the list"


def main():
    pytest.main(["-q", "--tb=no", __file__])


if __name__ == '__main__':
    main()
