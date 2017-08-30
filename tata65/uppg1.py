#coding = utf-8

i = 0

def f (k, a, b, p):
    """
    :param k: Antal kronor Matte har
    :param a: Antal kronor Matte hade från början
    :param b: Antal kronor Ida hade från början
    :param p: Sannolikhet att Matte vinner en slantsingling
    """
    global i
    i+=1
    if i >= 1000:
        return 0
    if k >= a + b:
        return 1
    elif k <= 0:
        return 0
    else:
        return p * f(k+1, a, b, p) + (1-p) * f(k-1, a, b, p)


def sim(k, a, b, p):
    """ 5, 5, 5, 1/6 -> 1/6^5 + 5/6 * 1/6^6"""
    q = 1-p
    return p**b +q * p**(b+1) + q*p*q*(p**(b+1))

def formel(k,a,b ,p):
    qp = ((1-p)/p)
    return (qp**k - 1)/(qp**(a+b)-1)


#print(f(5, 5, 5, 1.0/6))
#print(i)
print(formel(5,5,5,1.0/6))
print(sim(5,5,5, 1.0/6))