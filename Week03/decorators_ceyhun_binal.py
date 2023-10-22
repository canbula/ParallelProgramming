import time

counter = {} 
total_times = {} 

def performance(func):
    def _performance(*args, **kwargs):
        function_name = func.__name__

        if function_name not in counters:
            counter[function_name] = 0
            total_times[function_name] = 0

        counter[function_name] += 1
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        total_times[function_name] += execution_time

        return result

    return _performance

def print_function_summary():
    for function_name in counter:
        print(f"Function '{function_name}' took {total_times[function_name]:.6f} seconds.")
        print(f"Total time for '{function_name}': {total_times[function_name]:.6f} seconds")
        print(f"Function calls for '{function_name}': {counter[function_name]}")

@performance
def aggregate_function(arg1: int = 0, arg2: int = 0) -> int:
    return arg1 + arg2

@performance
def multiple_function(arg1: float, arg2: float) -> float:
    return arg1 * arg2

if __name__ == "__main__":
    aggregate_function(3, 4)
    multiple_function(2, 5)
    multiple_function(534.4, 748.7)
    multiple_function(489.25, 745.62)
    
print_function_summary()
