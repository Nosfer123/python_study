text = input('Write your number: ')
text = (int(text))

def text_plus1():
    global text
    text += 1

def print_line():
    n=0
    global text
    text_print = text
    while True:
        print (text_print, end=' ')
        text_print += 1
        n += 1
        if n == 5:
            break


def one_time():
    print_line()
    print()
    text_plus1()

def four_time():
    for dummy_y in range(4):
        one_time()

four_time()