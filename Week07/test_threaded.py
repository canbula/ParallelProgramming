import os
import pytest
import time
import threading


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("threaded")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    """Test if the files are named correctly"""
    for f in files:
        assert "threaded" in dir(eval(f[:-3])), "threaded is not defined in " + f[:-3]


def test_callable():
    """Test if threaded is a function"""
    for f in files:
        assert callable(eval(f[:-3]).threaded), (
            "threaded is not a function in " + f[:-3]
        )


def test_accepts_argument():
    """Test if threaded accepts an argument"""
    for f in files:
        assert eval(f[:-3]).threaded.__code__.co_argcount == 1, (
            "threaded does not accept an argument in " + f[:-3]
        )


def test_decorator():
    """Test if threaded returns a function"""
    for f in files:
        assert callable(eval(f[:-3]).threaded(lambda x: x)), (
            "threaded is not a decorator which returns a function in " + f[:-3]
        )


def test_threads():
    """Test if the decorated function runs in a separate thread"""
    for f in files:
        thread_results = []

        @eval(f[:-3]).threaded(3)
        def dummy_function(value):
            thread_results.append((value, threading.current_thread().name))

        dummy_function("dummy")
        assert len(thread_results) == 3, "Threaded function did not run 3 times"
        assert all(
            [t[0] == "dummy" for t in thread_results]
        ), "Threaded function did not run with the correct argument"
        assert len(set([t[1] for t in thread_results])) == 3, (
            "Threaded function did not run in separate threads in " + f[:-3]
        )


def test_waiting():
    """Test if the main thread waits for the threads to finish"""
    for f in files:
        execution_order = []

        @eval(f[:-3]).threaded(2)
        def slow_function(value):
            execution_order.append(value)
            time.sleep(1)

        start_time = time.time()
        for i in range(2):
            slow_function(i)
        end_time = time.time()

        assert len(execution_order) == 4, "Threaded function did not run 2 times"
        assert execution_order == [0, 0, 1, 1], "Threaded function did not run in order"
        assert (
            end_time - start_time >= 1
        ), "Main thread did not wait for the threads to finish"


def test_multiple_calls():
    """Test if the decorated function can be called multiple times"""
    for f in files:
        call_results = []

        @eval(f[:-3]).threaded(4)
        def counter_function(value):
            call_results.append(value)

        counter_function(1)
        counter_function(2)

        time.sleep(1)

        assert len(call_results) == 8, "Threaded function did not run 8 times"
        assert (
            call_results.count(1) == 4
        ), "Threaded function did not run with the correct argument"
        assert (
            call_results.count(2) == 4
        ), "Threaded function did not run with the correct argument"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
