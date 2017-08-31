#encode = "utf-8"
import math, numbers

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
    """Anropar inga externa funktioner, rörigt"""
    p_list =[]
    for i in range(9):
        mult = (i%2)*-1 +2
        p_list.append(list[i]*mult)
    sum = 0
    for item in p_list:
        ten = (item - item%10)//10
        one = item%10
        sum += ten + one
    sum_up = 0
    if sum % 10 == 0:
        sum_up = sum
    else:
        sum_up = (sum - sum%10) + 10
    return (sum_up - sum) == list[9]

"""TESTER"""

#print(sum_ten(5), sum_ten(15))
