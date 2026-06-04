import time


class Timer:
    # __slots__ reduces memory usage and speeds up attribute access
    __slots__ = ("start_time", "end_time", "_running")

    def __init__(self):
        # Store start and end timestamps
        self.start_time = None
        self.end_time = None

        # Indicates whether the timer is currently running
        self._running = False

    def __enter__(self):
        # Automatically start the timer when entering context
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Automatically stop the timer when exiting context
        self.stop()

        # Returning False ensures exceptions are not suppressed
        return False

    def start(self):
        # Prevent starting an already running timer
        if self._running:
            raise RuntimeError("Timer is already running")

        # Use high-resolution performance counter
        self.start_time = time.perf_counter()

        # Reset end time
        self.end_time = None

        # Mark timer as running
        self._running = True

        return self

    def stop(self):
        # Prevent stopping a timer that isn't running
        if not self._running:
            raise RuntimeError("Timer is not running")

        # Record end time
        self.end_time = time.perf_counter()

        # Mark timer as stopped
        self._running = False

        return self

    @property
    def elapsed(self):
        # Ensure timer has been started
        if self.start_time is None:
            raise RuntimeError("Timer has not been started")

        # If still running, return current elapsed time
        if self._running:
            return time.perf_counter() - self.start_time

        # Otherwise return total elapsed time
        return self.end_time - self.start_time

    def __repr__(self):
        # Representation when not started
        if self.start_time is None:
            return "<Timer (not started)>"

        # Representation when running
        if self._running:
            return f"<Timer running: {self.elapsed:.6f}s>"

        # Representation when stopped
        return f"<Timer stopped: {self.elapsed:.6f}s>"
