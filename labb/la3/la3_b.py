
def factorial (n):
    if n == 0:
        return 1
    return n* factorial(n-1)

def perm (n,k):
    if n == k:
        return 1
    if n <= k+1:
        return k+1
    return n * perm(n-1, k)


def choose(n, k):
    """Doesn't calculate each factorial independently"""
    q = n-k
    perm_res = 0

    if k >= q:
        perm_res = perm(n, k) // factorial(q)

    else:
        perm_res = perm(n, q) // factorial(k)

    return perm_res



def choose_expensive(n,k):
    """Will fail for big values"""
    return factorial(n)//(factorial(k)*factorial(n-k))

#TESTER
def test():
    print(choose(99999999, 1), choose(5,3), choose(52,5))
    print(choose_expensive(99999999, 1), choose_expensive(5,3), choose_expensive(52,5))