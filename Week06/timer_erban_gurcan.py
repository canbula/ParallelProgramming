import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        # Runs when entering the 'with' block
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Runs when exiting the 'with' block
        self.end_time = time.perf_counter()


# Example Usage:
if __name__ == "__main__":
    # Using it as a context manager (via the 'with' statement)
    with Timer() as t:
        # The block of code to be measured goes here
        print("Doing some time-consuming work...")
        time.sleep(1.5) # Sleeping for 1.5 seconds for simulation

    # Calculate the elapsed time after the block finishes
    elapsed_time = t.end_time - t.start_time
    
    print(f"Start Time: {t.start_time}")
    print(f"End Time: {t.end_time}")
    print(f"Total time taken by the block: {elapsed_time:.4f} seconds")
