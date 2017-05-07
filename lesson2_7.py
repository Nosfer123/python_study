def show_matrix(rows, cols, symb=3):
    for dummy_row in range(rows):
        my_str = ""
        for dummy_col in range(cols):
            my_str += symb
        print(my_str)

show_matrix(5,4, 'R')