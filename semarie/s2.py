#encode = utf-8
from itertools import groupby
from collections import defaultdict



def min_max(seq):
    if not seq:
        return (None, None)
    if len(seq) == 1:
        return seq[0], seq[0]

    min, max = min_max(seq[1:])
    min = seq[0] if seq[0] < min else min
    max = seq[0] if seq[0] > max else max

    print("min: ", min, " max: ", max)

    return min, max



def find_uncut (seq):
    return [ (j,i) for i in range(len(seq)) for j in range(len(seq[i])) if seq[i][j] == False]


def find_uncut_2 (seq):
    res = []
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            if seq[i][j] == False:
                res.append((j,i))
    return res


def find_uncut_r (seq, y=0, x=0):
    if not seq:
        return []
    item = seq[0]
    if isinstance(item, list):
        return find_uncut_r(item, y, 0) + find_uncut_r(seq[1:], y+1, 0)
    elif item == False:
        return [(x, y)] + find_uncut_r(seq[1:], y, x+1)
    else:
        return find_uncut_r(seq[1:], y, x+1)


def palindrom (word = ""):
    return word[::-1] == word

def palindrom_r(word):
    if not word:
        return True
    return word[0] == word[-1] and palindrom_r(word[1:-1])




def dict_func(dictionary):
    result = defaultdict(list)
    for key in dictionary:
        result[dictionary[key]].append(key)
    return dict(result)


def dict_func_2(dict):
    result = {}

    for key in dict:
        if dict[key] in result:
            result[dict[key]].append(key)
        else:
            result[dict[key]] = [key]
    return result

def _test():
    cut_list = [
                [True,  False, True,  False],
                [True, True, True,  True],
                [False,  False, True, True],
                [False, True,  True,  False]
        ]
    print(find_uncut(cut_list))
    print(find_uncut_2(cut_list))
    print(find_uncut_r(cut_list))
    print("palindrom:",palindrom("anna"))
    print(palindrom_r("anna"))
    print(palindrom_r("hej"))
    dict = {
        "Barney":"Male",
        "Lily": "Female",
        "Ted":"Male",
        "Marshall":"Male",
        "Robin":"Female"
    }
    print(dict_func(dict))


    print(min_max([3,2,1]))
    #print(min_max([3, 1, "abc"]))
    print(min_max((1,2,3)))


_test()