def print_square(n):
    for i in range(n):
        for k in range(n):
            print('*', end='')
        print()

while True:
    num = int(input('N: '))
    print_square(num)
    print()

    is_done = input('One more?')
    if is_done:
        break