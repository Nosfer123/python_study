letter = 'X'
zipped = list(zip(board[0], board[1], board[2]))
zipped_list = []
for a in range(3):  # from tuple to list
    zipped_list.append(list(zipped[a]))
diag_lst = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
win_list = board + zipped_list + diag_lst

for lst in range(8):
    print(win_list[lst])
    if win_list[lst].count(letter) == 3:  # нету проверки по диагонали
        print('win')
