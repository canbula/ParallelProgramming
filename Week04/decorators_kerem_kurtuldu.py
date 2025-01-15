import time
import tracemalloc

def performance(func):
    setattr(performance, '_count', 0)
    setattr(performance, '_time', 0.0)
    setattr(performance, '_memory', 0.0)

    def wrapper(*args, **kwargs):
        count = getattr(performance, '_count') + 1
        setattr(performance, '_count', count)

        start = time.time()
        tracemalloc.start()

        try:
            func(*args, **kwargs)
        except Exception as exc:
            print(f"Error: {exc}")
        finally:
            end = time.time()
            curr, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            elapsed = end - start
            total_time = getattr(performance, '_time') + elapsed
            total_mem = getattr(performance, '_memory') + peak

            setattr(performance, '_time', total_time)
            setattr(performance, '_memory', total_mem)

            print(f"{func.__name__}: Calls={count}, Time={elapsed:.4f}s, "
                  f"Memory={peak / 1024:.1f}KB, TotalTime={total_time:.4f}s, "
                  f"TotalMem={total_mem / 1024:.1f}KB")

    return wrapper
