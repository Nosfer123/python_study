def func(*args): #args
    rez = 0
    for arg in args:
        rez += arg
    return rez

print(func(1, 2, 3, 4, 5, 100))


def func(**kwargs): #set
    for key in kwargs.keys():
        print(kwargs[key])
    return kwargs

print(func(y=4, x=7, z=5))