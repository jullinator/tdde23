# encode = utf-8

OPERATORS = ["NOT", "OR", "AND"]
LOGIC = ["true", "false"]

def interpret (expression, table = {}):
    """return 'true' or 'false' """
    if expression[0] == "LOGIC": #BASFALL
        return expression[0]
    if not expression:
        return []
    item = expression[0]
    if isinstance(item, list):
        return interpret(item, table)
    elif item in OPERATORS:
        print(item)
    elif item in LOGIC:
        pass




def test ():
    #interpret(["cat_asleep", "OR", ["NOT", "cat_gone"]],{"door_open": "false", "cat_gone": "true", "cat_asleep": "true"})
    interpret(["true"], {})