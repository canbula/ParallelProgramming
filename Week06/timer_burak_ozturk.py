import time
import logging

class Timer:
    def __init__(self):
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time.time()
        logging.info("---- Timer started ----")
        logging.info(f"Invoked by module: {__name__}")
        return self

    def __exit__(self, exc_type=None, exc_value=None, exc_tb=None):
        self.end = time.time()

        if exc_type or exc_value or exc_tb:
            logging.error(f"Error during execution in module: {__name__}")
            logging.info("---- Timer stopped ----")
            return False

        elapsed = self.end - self.start
        logging.info(f"Execution time in module {__name__}: {elapsed:.4f} seconds")
        logging.info("---- Timer stopped ----")
        return elapsed
