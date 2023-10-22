import time

counters = {} 
total_times = {} 

def performance_decorator(func):

    def wrapper(*args, **kwargs):
        function_name = func.__name__

        if function_name not in counters:
            counters[function_name] = 0
            total_times[function_name] = 0

        counters[function_name] += 1
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        total_times[function_name] += execution_time

        return result

    return wrapper

def print_function_summary():

    for function_name in counters:
        print(f"Function '{function_name}' took {total_times[function_name]:.6f} seconds.")
        print(f"Total time for '{function_name}': {total_times[function_name]:.6f} seconds")
        print(f"Function calls for '{function_name}': {counters[function_name]}")

@performance_decorator
def aggregation_function(arg1: int = 0, arg2: int = 0) -> int:
    return arg1 + arg2

@performance_decorator
def multiplication_function(arg1: float, arg2: float) -> float:
    return arg1 * arg2

if __name__ == "__main__":
    aggregation_function(3, 4)
    multiplication_function(2, 5)
    multiplication_function(534, 748)
    multiplication_function(489, 745)
    
print_function_summary()
