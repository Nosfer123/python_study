board = [[str(a+1+(b*3)) for a in range(3)] for b in range(3)]


def draw_board():
    num_of_lst = 0
    end = '-----------'
    is_end_board = 0
    for dummy_n in range(3):
        print('   |   |')
        print(' ' + board[num_of_lst][0] + ' | ' + board[num_of_lst][1] + ' | ' + board[num_of_lst][2])
        print('   |   |')
        print(end)
        num_of_lst += 1
        is_end_board += 1
        if is_end_board == 2:
            end = '\n'


zipped = list(zip(board[0], board[1], board[2]))
zipped_list = []
for a in range(3):  # from tuple to list
    zipped_list.append(list(zipped[a]))

diag_lst = [[board[0][0], board[1][1], board [2][2]], [board[0][2], board[1][1], board[2][0]]]
print(board)
print(zipped_list)
print(diag_lst)
all_lst = board + zipped_list + diag_lst
print(all_lst)


def is_win():
    global letter  # is it ok to use global in this situation, or better to have local argument?

    zipped = list(zip(board[0], board[1], board[2]))
    zipped_list = []
    for a in range(3):  # from tuple to list
        zipped_list.append(list(zipped[a]))

    for i in range(3):
        if board[i].count(letter) == 3 or zipped_list[i].count(letter) == 3:  # нету проверки по диагонали
            if letter == 'X':
                print('Player 1 win')
            else:
                print('Player 2 win')
