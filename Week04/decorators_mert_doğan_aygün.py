import time
import tracemalloc


def track_performance(func):
    setattr(track_performance, 'call_count', 0)
    setattr(track_performance, 'cumulative_time', 0.0)
    setattr(track_performance, 'cumulative_memory', 0.0)

    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        setattr(track_performance, 'call_count', getattr(track_performance, 'call_count') + 1)
        setattr(track_performance, 'cumulative_time', getattr(track_performance, 'cumulative_time') + (end_time - start_time))
        setattr(track_performance, 'cumulative_memory', getattr(track_performance, 'cumulative_memory') + peak_memory)
        return result

    return wrapper
