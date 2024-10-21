import asyncio
from functools import wraps

def coroutine_decorator(func):
    """
    A decorator to convert any function into a coroutine.
    
    It ensures that the decorated function can handle 
    both asynchronous and synchronous executions.
    
    :param func: The function to be decorated.
    :return: The coroutine-wrapped function.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Handle both synchronous and asynchronous return values
        result = func(*args, **kwargs)
        
        # If the result is awaitable, await it.
        if asyncio.iscoroutine(result):
            return await result
        return result
    
    return wrapper

# Example usage
@coroutine_decorator
def add_numbers(a, b):
    """
    Simple function to add two numbers.
    
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b

# Using the decorated coroutine function
async def main():
    result = await add_numbers(5, 3)
    print(f"Result: {result}")

# Running the coroutine
asyncio.run(main())
