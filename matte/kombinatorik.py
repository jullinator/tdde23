# coding=utf-8
def fakultet (n = 1):
    """om n = 3 -> 3*2*1"""
    sum = 1
    for i in range(n, 1, -1):
        sum *= i
    return sum


def permutationer (n, k):
    """P(6,2) -> 6!/(6-2)!"""
    return fakultet(n)/fakultet(n-k)

def kombinationer (n, k):
    """n!/(k!(n-k)!)"""
    return fakultet(n)/(fakultet(k)*fakultet(n-k))



def dansa_q(w, l):
    dic={}
    for i in range(l):
        str = ''
        for c in w:
            str+=c
    pass


uppgifter = {}
uppgifter[(5,24)] = 2


def dansa (word="", new_word_length=3):
    """Hur många olika ord som är $new_word_length långa kan göras av $word"""
    l = new_word_length
    # Hitta repeat av $char in $word
    char_count = {}
    char_spec = {}
    for char in word:
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1

    #

    pass









