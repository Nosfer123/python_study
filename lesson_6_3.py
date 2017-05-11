def func(*args, **kwargs):
    for arg in args:
        print(arg)

    for key in kwargs.keys():
        print(kwargs[key])

    return args, kwargs

print(func(2, [77, 66], 4, a='abc', name='Tom', grades=[23, 56, 69]))
print(func(2, 4, 5, 6, 7))