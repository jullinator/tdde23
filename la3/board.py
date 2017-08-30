def new_board():
    return {}

def isfree (board, x, y):
    """-> True or False"""
    return not (x,y) in board.keys()

def place_piece(board, x, y, spelare):
    """-> True or False"""
    can_place = isfree(board, x, y)
    if can_place:
        board[(x,y)] = spelare
    return can_place

def get_piece(board, x, y):
    """-> spelare or False"""
    piece_exists = not isfree(board, x, y)
    if piece_exists:
        return board[(x,y)]
    return piece_exists


def remove_piece(board, x, y):
    """-> True or False"""
    piece_exists = not isfree(board, x, y)
    if piece_exists:
        del board[(x,y)]
    return piece_exists

def move_piece(board, x, y, new_x, new_y):
    """True or ?False"""
    if not isfree(board, x, y):
        spelare = get_piece(board, x, y)
        remove_piece(board, x, y)
        place_piece(board, new_x, new_y, spelare)
        return True
    return False

def count(board, field, cord, spelare):
    """ column=x, row= y"""
    count=0
    for key in board.keys():
        place = 0
        if field == "row":
            place = 1
        if key[place] == cord and get_piece(board, key[0], key[1]) == spelare:
            count += 1
    return count

def nearest_piece(board, x, y):
    """ -> (500, 100) or False"""
    min_dist =0
    n_piece = False

    if not isfree(board, x, y):
        return (x,y)

    for key in board.keys():
        dist = (x- key[0]) **2 + (y - key[1]) **2
        if min_dist == 0:
            min_dist = dist
        if dist <= min_dist:
            min_dist = dist
            n_piece = key

    return n_piece
