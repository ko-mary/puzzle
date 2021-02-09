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
    pass


def validate_board(board: list) -> bool:
    '''
    '''
    pass