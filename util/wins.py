win_index = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]  # diagonals
]


def check_win(buttons):
    for index in win_index:
        if buttons[index[0]].was_set and buttons[index[1]].was_set and buttons[index[2]].was_set:
            if buttons[index[0]].color == buttons[index[1]].color and buttons[index[1]].color == buttons[index[2]].color:
                return True
    return False
