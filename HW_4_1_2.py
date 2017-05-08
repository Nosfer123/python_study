col = (input('Number of columns: '))
row = (input('Number of lines: '))
text = (input('What do you want to print? '))

def print_text():
    for dummy_n in range (int(row)):
        print (text*(int(col)))


print_text()