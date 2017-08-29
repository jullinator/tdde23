def new_board():
    return {}

def is_free(board, x, y):
    return (x,y) in board.keys()

def place_piece(board, x, y, spelare):
    can_place = is_free(board, x, y)
    if can_place:
        board[(x,y)] = spelare
    return can_place

def get_piece(board, x, y):
    piece_exists = not is_free(board, x, y)
    if piece_exists:
        return board[(x,y)]
    return piece_exists


def remove_piece(board, x, y):
    piece_exists = not is_free(board, x, y)
    if piece_exists:
        del board[(x,y)]
    return piece_exists

def move_piece():

