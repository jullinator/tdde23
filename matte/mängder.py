# coding = utf-8

def union (mgd_arr=[]):
    arr = []
    for mgd in mgd_arr:
        for i in mgd:
            add = True
            for j in arr:
                if i == j:
                    add = False
            if add:
                arr.push(i)
    return arr