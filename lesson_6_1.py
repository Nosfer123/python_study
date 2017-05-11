def func_name(x, y, z=1):
    return x + y + z


def two():
    return 2

print(func_name(two(), 3, 4))
print(func_name(two(), 3)) #if no z, it takes 'z=1'

