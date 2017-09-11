#coding = utf-8
import random

def f (k, a, b, p):
    """
    :param k: Antal kronor Matte har
    :param a: Antal kronor Matte hade från början
    :param b: Antal kronor Ida hade från början
    :param p: Sannolikhet att Matte vinner en slantsingling
    """
    if k >= a + b:
        return 1
    elif k <= 0:
        return 0
    else:
        return p * f(k+1, a, b, p) + (1-p) * f(k-1, a, b, p)


def sim(k, a, b, p):
    """uses random to simulate a game"""
    res = 0
    sims = 10**5
    for i in range(sims):
        money = k
        while money < a+b and money > 0:
            roll = random.randint(1, 6)
            money = money + 1 if roll == 1 else money -1
        res = res + 1 if money >= a+b else res
    odds = res / sims
    return odds


def formel(k,a,b ,p):
    qp = ((1-p)/p)
    return (qp**k - 1)/(qp**(a+b)-1)


#print(f(5, 5, 5, 1.0/6))
#print(i)
real, sim_res = formel(5,5,5, 1.0/6) ,sim(5,5,5, 1.0/6)
print(real, sim_res, real/sim_res if sim_res>0 else 0)
print()