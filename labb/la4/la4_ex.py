#encode = utf-8
from numbers import Number

def show_wordlist(numbers):
    for key, value in numbers.items():
        print(key, " - ", value)

def all_pairs(list=[]):
    pairs = []
    for i in range(len(list)):
        for j in range(len(list)):
            pairs.append((list[i],list[j]))
    return pairs

def unorded_pairs(list=[]):
    """FAILS"""
    res = []
    for pair in all_pairs(list):
        res.append(sorted(pair))
    res.sort()
    for pair in res:
        while res.count(pair) > 1:
            res.remove(pair)
    return res

def distribute(dis, l_list):
    new_list = []
    for list in l_list:
        tl = [dis]
        for l in list:
            tl.append(l)
        new_list.append(tl)
    return new_list

def len2 (seq):
    """Dubbel rekursion, lista i lista"""
    if not seq:
        return 0
    elif isinstance(seq[0], list):
        return len2(seq[0]) + len2(seq[1:])
    else:
        return 1 + len2(seq[1:])

def remove(seq, x):
    """Removes all occurances of element x in list<any> (dubbelrekursion). Flattens list"""
    if not seq:
        return []
    elif isinstance(seq[0], list):
        return remove(seq[0],x) + remove(seq[1:],x)
    elif seq[0] == x:
        return remove(seq[1:], x)
    else:
        return [seq[0]] + remove(seq[1:], x)

def extend_each (x, seq=[]):
    """Tar en lista och lägger till x i varje list-list. Bara en lista djup."""
    for s in seq:
        s.insert(0, x)
    return seq

def push_strings(seq, prev_letter=False, new_list=[]):
    """Pushar alla strings i listan till nästa pos, första->0, sista försvinner"""
    for i in range(len(seq)):
        item = seq[i]
        if isinstance(item, str):
            if not prev_letter:
                new_list.insert(i, 0)

            else:
                new_list.insert(i, prev_letter)
            prev_letter = item
        else:
            new_list.insert(i, item)
    return new_list

def push_strings_r (seq, prev_letter = False):
    if not seq:
        return []
    item = seq[0]
    if isinstance(item, str):
        if not prev_letter:
            return [0] + push_strings_r(seq[1:], item)
        return [prev_letter] + push_strings_r(seq[1:], item)
    return [item] + push_strings_r(seq[1:], prev_letter)

def merge_list (seq):
    """Tar lista med två listor -> [stigande ordning] (ursp. listor är i stigande ordning), iterativ"""
    flat_list = [item for sublist in seq for item in sublist]
    flat_list.sort()
    return flat_list

def sum_all_numbers (seq):
    """flat list of all numbers, x-deep level lists"""
    if not seq:
        return []
    if isinstance(seq[0], list):
        return sum_all_numbers(seq[0]) + sum_all_numbers(seq[1:])
    if isinstance(seq[0], Number):
        return [seq[0]] + sum_all_numbers(seq[1:])
    return sum_all_numbers(seq[1:])

#TESTER
def test():
    deep_list = [1,3,2,[2,3,1,[1,3]],[2]]
    print(show_wordlist({"one": 1, "eight":8}))
    print(all_pairs([2,1,3]))
    print(unorded_pairs([2, 1, 3]))
    print(distribute("o", [["test"], ["fo"],[0]]))
    print("len2:", len2(deep_list))
    print("remove (1):", remove(deep_list, 1))
    print("extend_each:", extend_each("number",[[3],[2]]))
    print("push_strings: ", push_strings([1,4,"hej", 2, "s", "f"]))
    print("push_strings recursive: ", push_strings_r([1, 4, "hej", 2, "s", "f"]))
    print("merge list: ", merge_list([[1,2,3,4],[1,4,5,6]]))
    print("sum all numbers", sum_all_numbers([1,2,"f",[4,5, [5]], [2,3]]))
test()