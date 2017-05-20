def my_loop_fact(n):
    fact = 1
    counter = 1
    while counter <= n:
        fact *= counter
        counter += 1
        print(fact)
    return fact


my_loop_fact(5)