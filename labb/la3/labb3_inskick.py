# Justus Karlsson - Laboration 3 - juska933

#LABB A

def new_board():
    return {}

def isfree (board, x, y):
    """Returns True if place is free, False if not."""
    return not (x,y) in board.keys()

def place_piece(board, x, y, player):
    """Places a piece belonging to player on coordinates, if it's free. Returns True or False based on result."""
    can_place = isfree(board, x, y)
    if can_place:
        board[(x,y)] = player
    return can_place

def get_piece(board, x, y):
    """ Returns the name of the player on the coordinates. Returns False if no piece exists there."""
    piece_exists = not isfree(board, x, y)
    if piece_exists:
        return board[(x,y)]
    return piece_exists


def remove_piece(board, x, y):
    """Removes a piece and return True if successfull, False if not."""
    piece_exists = not isfree(board, x, y)
    if piece_exists:
        del board[(x,y)]
    return piece_exists

def move_piece(board, x, y, new_x, new_y):
    """ Moves a piece and returns True if successfull, False if not."""
    if not isfree(board, x, y):
        player = get_piece(board, x, y)
        remove_piece(board, x, y)
        place_piece(board, new_x, new_y, player)
        return True
    return False

def count(board, field, cord, player):
    """ Returns the count of all pieces belonging to the player on either the:
        - row with the number of cord (if field is equal to 'row')
        - column with the number of cord (if field is equal to 'column')
    """
    count=0
    for key in board.keys():
        place = 0
        if field == "row":
            place = 1
        if key[place] == cord and get_piece(board, key[0], key[1]) == player:
            count += 1
    return count

def nearest_piece(board, x, y):
    """ Returns coordinates of the nearest piece to coordinates supplied (x,y) or False if no piece exists"""
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




def factorial (n):
    if n == 0:
        return 1
    return n* factorial(n-1)

def perm (n,k):
    """Recursive factorial, but stops when n is equal to k+1."""
    if n == k:
        return 1
    if n <= k+1:
        return k+1
    return n * perm(n-1, k)


def choose(n, k):
    """ Combinations if you choose k from n. Doesn't calculate each factorial independently. """
    q = n-k
    perm_res = 0

    if k >= q:
        perm_res = perm(n, k) // factorial(q)

    else:
        perm_res = perm(n, q) // factorial(k)

    return perm_res

