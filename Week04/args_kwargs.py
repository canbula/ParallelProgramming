def my_function(*args, **kwargs):
    print(args)
    print(kwargs)
    for arg in args:
        print(f"The positional argument: {arg}")
    for k, v in kwargs.items():
        print(f"The keyword argument: {k}={v}")


my_function(3, 5, name="Bora", age=39)
