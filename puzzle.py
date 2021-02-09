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
    pass


def check_colour(board: list) -> bool:
    '''
    '''
    pass


def validate_board(board: list) -> bool:
    '''
    '''
    pass