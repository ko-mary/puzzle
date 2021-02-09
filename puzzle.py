'''
https://github.com/ko-mary/puzzle
'''

def check_lines(board: list) -> bool:
    '''
    '''
    for line in range(board):
        for check_number, check_element in enumerate(line):
            if check_element != '*' and check_element != ' ':
                for number, element in enumerate(line):
                    if check_element == element and check_number!= number:
                        return False
    return True


def check_columns(board: list) -> bool:
    '''
    '''
    turned_board = []
    size = len(board)
    for number, line in enumerate(board):
        if number == 0:
            for element in line:
                turned_board.append(element)
            continue
        for pointer in range(size):
            turned_board[pointer] += line[pointer]
    return check_columns(turned_board)


def check_colour(board: list) -> bool:
    '''
    '''
    start_line = 4
    finish_line = 8
    start_column = 0
    for amount in range(5):
        colour = []
        for number, line in enumerate(board):
            if number < start_line:
                continue
            current = line[start_column]
            if current in colour:
                return False
            if current != ' ':
                colour.append(current)
            if number == finish_line:
                for num in range(1, 5):
                    if line[num] in colour:
                        return False
                    if line[num] != ' ':
                        colour.append(line[num])
        start_line -= 1
        finish_line -= 1
        start_column +=1
    return True


def validate_board(board: list) -> bool:
    '''
    '''
    if check_lines(board) == False:
        return False
    if check_columns(board) == False:
        return False
    if check_colour(board) == False:
        return False
    return True