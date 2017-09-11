# Justus Karlsson - Laboration 4 - juska933
import string

#LABB A


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


#LABB B

lowercase = string.ascii_lowercase+"åäö"
uppercase = string.ascii_uppercase+"ÅÄÖ"
case1 = lowercase+"_"+"."
case2 = uppercase+ " " + "|"

def split_rec(string):
    """Splits a string into two messages recursively (in their original order):
        - msg1 can only contain lowercased letters (Swedish), underscores and dots
        - msg2 can only contain uppercased letters (Swedish), spaces and pipes (|)
    """

    if not string:
        return ("", "")
    c = string[0]
    msg1, msg2 = split_rec(string[1:])
    msg1 = c + msg1 if c in case1 else msg1
    msg2 = c + msg2 if c in case2 else msg2
    return msg1, msg2



def split_it(str):
    """Splits a string into two messages iteratively (in their original order):
        - msg1 can only contain lowercased letters (Swedish), underscores and dots
        - msg2 can only contain uppercased letters (Swedish), spaces and pipes (|)
    """
    str1 = str2 = ""
    for char in str:
        if char in case1:
            str1+= char
        if char in case2:
            str2+= char
    return (str1, str2)
