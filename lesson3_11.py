def print_triangle (n):
    for i in range (1, n + 1):
        for k in range (n - 1):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        for j in range(i - 1):
            print ('*', end='')
        print()

print_triangle(6)