import time
import tracemalloc

def performance(fn):
  setattr(performance, 'counter', 0)
  setattr(performance, 'total_time', 0)
  setattr(performance, 'total_mem', 0)

  def wrapper(*args, **kwargs):
    setattr(performance, 'counter', performance.counter +1)

    start_time = time.time()
    tracemalloc.start()
    result = fn(*args, **kwargs)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    setattr(performance, 'total_time', performance.total_time + (end_time - start_time))
    setattr(performance, 'total_mem', performance.total_mem + peak)
    
    return result

  return wrapper
