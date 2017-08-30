import math, numbers

def unit (a):
    """12 -> 2"""
    return a % 10

def ten (a):
    """12 -> 1"""
    return (a-unit(a))//10

def power(x, n):
    ans = 1
    for i in range(n):
        ans = ans * x
    return ans

def sum_first(x):
    """6 -> 6+5+...+1"""
    sum=0
    for i in range(1, x+1):
        sum += i
    return sum

def is_number(x):
    return isinstance(x, numbers.Number)


def sum_numbers (list=[]):
    sum = 0
    for item in list:
        if (is_number(item)):
            sum+=item
    return sum

def find_letter (letter, list=[]):
    for item in list:
        if letter == item:
            return True
    return False


def is_vowel(letter):
    return find_letter(letter, ["a","e","i","o","u"])

def remove_vowels (list=[]):
    new_list = []
    for item in list:
        if not is_vowel(item):
            new_list.append(item)
    return new_list

"""TESTER"""

def test_1():
    print(unit(12), ten(12))
    print(power(2,3))
    print("sum first:", sum_first(6)) #21
    print("sum numbers:", sum_numbers(["a", 1, 4])) #5
    print("consonants ", remove_vowels(["h", "e", "j"]) ) #h j



test_1()