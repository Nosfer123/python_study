def func(*args):
    rez = 0
    for arg in args:
        rez += arg
    return rez

lst = list(range(1, 101))

print(lst)

print(func(*lst)) # func (1, 2, 3,...)
