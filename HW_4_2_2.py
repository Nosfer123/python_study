text = 1

def print_line():
    global text
    for dummy_n in range(5):
        print (text, end=' ')
        text += 1

def two_time():
    print_line()
    print()
    print_line()
    print()

def four_time():
    two_time()
    two_time()

four_time()