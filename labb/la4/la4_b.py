# encode = utf-8

# Generators ? (yield, current_max)

OPERATORS = ["OR", "AND"]
LOGIC = ["true", "false"]

def interpret(exp, table):
    """
    Interprets a logical expression. Returns a string; 'true' if the expression is correct, and 'false' if it's incorrect.
    """
    if isinstance(exp, str):
        if exp in table.keys():
            return table[exp]
        return exp

    elif len(exp) == 3:
        if exp[1] == "AND":
            return "true" if interpret(exp[0], table) == "true" and interpret(exp[2], table) == "true" else "false"
        elif exp[1] == "OR":
            return "true" if interpret(exp[0], table) == "true" or interpret(exp[2], table) == "true" else "false"

    elif len(exp) == 2 :
        return "false" if interpret(exp[1], table) == "true" else "true"

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
        return interpret(exp[2:], table, "false" if interpret(exp[1], table) =="true" else "true" )

    elif item in LOGIC or item in table.keys():
        return interpret(exp[1:], table, item)







def _test ():


    print(interpret(["NOT", "asleep", "OR", "true", "AND", "AND"], {"asleep":"true", "AND": "true"}))
    print(interpret(["NOT", "true", "OR", "true", "AND", "true"], {}))
    print(not True or True and True)
    print(interpret(["NOT", "false", "AND", "true", "AND", ["NOT","false", "AND", "true"]], {}))
    print(not False and True and (not False and True))

_test()