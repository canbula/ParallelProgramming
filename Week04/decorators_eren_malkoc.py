import time
import tracemalloc


def performance(fn):
    performance.counter = 0
    performance.total_time = 0.0
    performance.total_mem = 0

    def wrapper(*args, **kwargs):
        
        start_time = time.time()
        tracemalloc.start()

        
        result = fn(*args, **kwargs)

        
        end_time = time.time() - start_time
        current_mem, peak_mem = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        
        performance.counter += 1
        performance.total_time += end_time
        performance.total_mem += peak_mem

        
        print(f"Execution {performance.counter}:")
        print(f"Time: {end_time:.6f} seconds")
        print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KB\n")

        return result

    return wrapper
