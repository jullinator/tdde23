#encode = "utf-8"
import math, numbers
from functools import reduce

def unit (a):
    """12 -> 2"""
    return a % 10

def ten (a):
    """12 -> 1"""
    return (a-unit(a))//10

def siffer_summa(x):
    """"""
    return ten(x)+unit(x)

def get_mult(i):
    """om jämt -> 2, udda -> 1"""
    mult = 1
    if i % 2 == 0:
        mult = 2
    return mult

def get_sum(list=[]):
    """Bara nio första (0-8), return sum"""
    sum=0
    for i in range(9):
        mult = get_mult(i)
        prod = mult * list[i]
        sum += siffer_summa(prod)
    return sum

def up_ten (x):
    """ 20-> 20, 24 -> 30"""
    if x%10 == 0:
        return x
    return (x-unit(x)+10)


#WORKED
def check_pnr (pnr_list=[]):
    """Kollar om kontrollnumret i ett personnummer stämmer."""
    sum = get_sum(pnr_list)
    sum_up = up_ten(sum)
    ctrl = sum_up - sum
    return ctrl == pnr_list[9]


#WORKED
def check_pnr_dirty(list):
    """Anropar inga externa funktioner"""
    mult = lambda x: 2 if x%2 == 0 else 1
    p_list = [ list[i]*mult(i) for i in range(9)]
    ten, one = lambda x: (x-x%10)//10, lambda x: x%10               # tiotal-siffran samt entalssiffran
    sum = reduce(lambda x,y: x + ten(y) + one(y), p_list, 0)        # 0 som initializer:ett måste, annars är sum i början värdet av l[0]
    sum_up = sum if ( sum%10 == 0 ) else ( sum- sum%10 + 10 )       # runda upp ett tiotal, om den inte redan är på en
    return (sum_up - sum) == list[9]                                # kalkylerade kontrollsiffran == givna kontrollsiffran?

"""TESTER"""
print(check_pnr_dirty([9,6,0,5,2,4,6,8,1,9]))
#print(sum_ten(5), sum_ten(15))
