
def divide_by_three (x):
    print("{} divided by {} equals {}".format(x, 3, x/3))
    return x%3 == 0


def max_of_three (a, b, c):
    return max(a, b, c)

def max2 (a,b):
    if a > b:
        return a
    else:
        return b

def max3 (a,b,c):
    return max2(c, max2(a,b))
