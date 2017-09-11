# encode = utf-8
from tree import left_subtree

# Generators (yield, current_max)

OPERATORS = ["OR", "AND"]
LOGIC = ["true", "false"]

def sub_trees(exp, table):
    """Recursive?"""
    keys = [item for item in exp if (item in OPERATORS and item not in table.keys())]
    return exp[0], keys, exp[2]

def interpret_old (exp, table):
    """return 'true' or 'false' """

    if isinstance(exp, str):
        if exp in LOGIC:
            return exp
        elif exp in table.keys():
            return table[exp]
    i=0
    results = []
    key="NONE"
    while i < len(exp):
        if exp[i] == "NOT":
            if "NOT" not in table.keys():
                results.append("false" if interpret(exp[i + 1], table) == "true" else "true")
            else:
                pass

            i += 2
        elif exp[i] in OPERATORS and exp[i] not in table.keys():
            key = exp[i]
            i+=1
        else:
            results.append(interpret(exp[i], table))
            i += 1
    if key == "AND":
        return "true" if results[0] == "true" and results[1] == "true" else "false"
    elif key == "OR":
        return "true" if results[0] == "true" or results[1] == "true" else "false"
    elif key == "NONE":
        #no key -> ["true"] , ["NOT", ["true"]]  (thus only one result since no OPERATOR
        return results[0]
        pass


def interpret (exp, table, left=""):
    """return 'true' or 'false' """

    if not exp:
        return left

    if isinstance(exp, str):
        if exp in table.keys():
            return table[exp]
        return exp

    item = exp[0]

    if len(exp) == 1:
        return interpret(item, table)

    if isinstance(item, list):
        left = interpret(item, table)
        return interpret(exp[1:], table, left)

    if item in OPERATORS:
        if not left:
            return interpret(exp[1:], table, item)
        elif item == "AND":
            return "true" if interpret(left, table) == "true" and interpret(exp[1:], table) == "true" else "false"
        elif item == "OR":
            return "true" if interpret(left, table) =="true" or interpret(exp[1:], table) == "true" else "false"

    elif item == "NOT":
        return interpret(exp[2:], table, "false" if interpret(exp[1:], table) =="true" else "true" )

    elif item in LOGIC or item in table.keys():
        return interpret(exp[1:], table, item)




def _test ():
    #interpret(["cat_asleep", "OR", ["NOT", "cat_gone"]],{"door_open": "false", "cat_gone": "true", "cat_asleep": "true"})
    print(interpret(["NOT","true", "AND", "true"], {}))                                              #false
    print(interpret(["NOT",["cat_happy", "OR", "false"], "AND", "true"], {"cat_happy":"false"}))     #true
    print(interpret(["NOT", "AND"], {"AND": "false"}))                                               #true
    print(interpret(["NOT", "AND", "true"], {"NOT":"true"}))                                         #true
    print(interpret(["true", "AND", "true", "AND", "false"], {}))                                    #false



#print(interpret(["NOT", "NOT"],{"NOT":"false", "AND":"false"}))
#print(interpret([["true", "AND", "false"], "AND", "true"],{})) #true

#_test()