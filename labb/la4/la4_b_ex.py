# encode = utf-8
from tree import create_tree, is_empty_tree, is_leaf, left_subtree, right_subtree



def key(tree):
    return tree[1]

def is_treelik(tree):
    return isinstance(tree, list) and len(tree) == 3

def is_proper_tree (tree):

    if is_leaf(tree):
        return True

    if is_empty_tree(tree):
        pass

    item = tree[0]
    if isinstance(item. list):
        return is_proper_tree(tree[1:])

def test():
    t_tree = [[1, 3, []], 5, 6]
    print("key:", key(t_tree))