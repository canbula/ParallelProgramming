'''
GIL - Global Interpreter Lock
GIL is a lock that prevents multiple threads from executing Python bytecodes at once.
This lock is necessary mainly because CPython's memory management is not thread-safe.
This means that when one thread is using CPython's memory manager to allocate some memory,
another thread can't use it at the same time.
You can release GIL by using JIT (Just-In-Time) compilers like Numba or Cython.
'''