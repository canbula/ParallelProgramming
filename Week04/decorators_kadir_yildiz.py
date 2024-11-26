import time
import tracemalloc

def measure_performance(func):
    func.cumulative_time = 0.0
    func.call_count = 0
    func.cumulative_memory = 0.0
  
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start = time.perf_counter()  
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        func.call_count += 1
        func.cumulative_time += (finish - start)
        func.cumulative_memory += peak_memory
        return result
      
    wrapper.statistics = lambda: {
        'calls': func.call_count,
        'total_time': func.cumulative_time,
        'total_memory': func.cumulative_memory,
    }
    return wrapper
