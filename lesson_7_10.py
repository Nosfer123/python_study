import time


def get_time(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print("Time spent", t1-t0)
        return result
    return wrapper


@get_time
def long_count(n):
    a = 0
    for dummy_i in range(n):
        a = n ** n
    return a


print(long_count(5000))