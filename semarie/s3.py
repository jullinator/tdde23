from functools import reduce
import math


#Iterate over deck of 52 cards

def do_stuff():
    NUM_OF_CARDS = 52
    CARDS_PER_SUIT = 13
    SUITS = 'hsdc'
    suits = ('h', 's', 'd', 'c')

    for c in range(NUM_OF_CARDS):
        suit = suits[c//CARDS_PER_SUIT]
        val = c % CARDS_PER_SUIT
        print(val, suit)


    for suit in 'hsdc':
        for val in range(CARDS_PER_SUIT):
            print(suit, val)

    for (s,v) in zip(SUITS, range(CARDS_PER_SUIT)):
        print(s,v)

b=[1,5,3,2]

def a(b):
    c = b[0]
    for i in range(len(b)):
        c = b[i] if b[i] - c < 0 else c
    return c

def minimum(seq):
    num_iter = iter(seq)

    current_min = next(num_iter)
    for num in num_iter:
        if num < current_min:
            current_min=num

    return current_min
print(a(b))

def a (seq):
    return reduce(lambda min, x: x if x < min else min, seq)




leet = "Hello noob".lower().replace('e','3').replace('o','0')
sale = "!!!%s!!!" % "Super sale".upper()

snake = "from_snake_to_camel_case"
spl = snake.split("_")
camel = spl[0] + "".join(st.capitalize() for st in spl[1:])
#"hej".lstrip('h')

print(leet, sale, camel)

def biggest(seq):
    if not seq:
        return -math.inf
    if isinstance(seq[0], list):
        b1 = biggest(seq[0])
        b2 = biggest(seq[1:])
        return b1 if b1 > b2 else b2
    cur = seq[0]
    prev_b = biggest(seq[1:])
    return  cur if cur > prev_b else prev_b


def smallest(seq):
    # basfall
    if not seq:
        return math.inf
    # listfall
    if isinstance(seq[0], list):
        return min(smallest(seq[0]) ,smallest(seq[1:]))
    # annars
    prev_s = smallest(seq[1:])
    return seq[0] if seq[0] < prev_s else prev_s

print(biggest([1,2,[2,[3]], [9,5]]))
print(smallest([1,2,[2,[3]], [9,5]]))
