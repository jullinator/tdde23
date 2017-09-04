#encode = utf-8

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



#TESTER
def test():
    print(show_wordlist({"one": 1, "eight":8}))
    print(all_pairs([2,1,3]))
    print(unorded_pairs([2, 1, 3]))
    print(distribute("o", [["test"], ["fo"],[0]]))


test()