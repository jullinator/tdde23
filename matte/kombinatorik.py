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













