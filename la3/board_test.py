#!/usr/bin/env python3
"""
Unit testing with asserts for lab 3

Note:
If you have downloaded the scripts from the website it might not
have the access right. To solve this run:
$ chmod +x <path_to_test_3.py>

Usage (case insensitive for parameters to --test):
$ ./test_3.py --test a <path_to_lab>
to test lab 3A
$ ./test_3.py --test b <path_to_lab>
to test lab 3B
to test whole lab 3

Initial version by Erik Hansson <erik.b.hansson@liu.se>
Updated for TDDE23 by Frans Skarman <frask812@student.liu.se>

Changelog:
 * 31/8-2016: Updated the printed traceback in case that the given file
   can not be imported.
"""

from argparse import ArgumentParser
from importlib.machinery import SourceFileLoader
from traceback import format_exc
import sys


def test_board():
    """
    Tests the board functions
    """
    extra_printout = "\nSee test code line 140 for which functions that " + \
                     "have been called before."
    board = lab3.new_board()
    assert lab3.place_piece(board, 500, 100, "spelare1") is True, \
        'place_piece(500, 100, "spelare1"): expected True got ' + \
        str(lab3.place_piece(board, 500, 100, "spelare1")) + extra_printout
    board = lab3.new_board()
    assert lab3.isfree(board, 500, 100) is True, \
        'isfree(500, 100): expected True got ' + \
        str(lab3.isfree(board, 500, 100)) + extra_printout
    res = lab3.place_piece(board, 500, 100, "spelare1")
    assert res is True, \
        'place_piece(500, 100, "spelare1"): expected True got ' + \
        str(res) + extra_printout
    res = lab3.place_piece(board, 1, 100, "spelare2")
    assert res is True, \
        'place_piece(1, 100, "spelare2"): expected True got ' + \
        str(res) + extra_printout
    res = lab3.place_piece(board, 500, 100, "spelare2")
    assert res is False, \
        'place_piece(500, 100, "spelare2"): expected False got ' + \
        str(res) + extra_printout
    res = lab3.place_piece(board, 500, 200, "spelare2")
    assert res is True, \
        'place_piece(500, 200, "spelare2"): expected True got ' + \
        str(res) + extra_printout
    assert lab3.nearest_piece(board, 500, 200) == (500, 200), \
        'nearest_piece(500, 200): expected (500, 200) got ' + \
        str(lab3.nearest_piece(board, 500, 200)) + extra_printout
    assert lab3.isfree(board, 500, 100) is False, \
        'isfree(500, 100): expected False got ' + \
        str(lab3.isfree(board, 500, 100)) + extra_printout
    assert lab3.get_piece(board, 500, 100) == "spelare1", \
        'get_piece(500, 100): expected "spelare1" got ' + \
        str(lab3.get_piece(board, 500, 100)) + extra_printout
    assert lab3.get_piece(board, 666, 666) is False, \
        'get_piece(666, 666): expected False got ' + \
        str(lab3.get_piece(board, 666, 666)) + extra_printout
    res = lab3.remove_piece(board, 500, 100)
    assert res is True, \
        'remove_piece(500, 100): expected True got ' + str(res) + \
        extra_printout
    res = lab3.remove_piece(board, 1, 1)
    assert res is False, \
        'remove_piece(1, 1): expected False got ' + str(res) + extra_printout
    assert lab3.isfree(board, 500, 100) is True, \
        'isfree(500, 100): expected True got ' + \
        str(lab3.isfree(board, 500, 100)) + extra_printout
    res = lab3.move_piece(board, 500, 200, 500, 100)
    assert res is True, \
        'move_piece(500, 200, 500, 100): expected True got ' + str(res) + \
        extra_printout
    assert lab3.get_piece(board, 500, 100) == "spelare2", \
        'get_piece(500, 100): expected "spelare2" got ' + \
        str(lab3.get_piece(board, 500, 100)) + extra_printout
    assert lab3.count(board, "column", 500, "spelare2") == 1, \
        'count("column", 500, "spelare2"): expected 1 got ' + \
        str(count("column", 500, "spelare2")) + extra_printout
    assert lab3.count(board, "row", 100, "spelare2") == 2, \
        'count("row", 100, "spelare2"): expected 2 got ' + \
        str(lab3.count(board, "row", 100, "spelare2")) + extra_printout
    assert lab3.nearest_piece(board, 500, 105) == (500, 100), \
        'nearest_piece(500, 105): expected (500, 100) got ' + \
        str(lab3.nearest_piece(board, 500, 105)) + extra_printout
    board = lab3.new_board()
    assert lab3.nearest_piece(board, 500, 100) in (False, ()), \
        'nearest_piece(500, 100): expected False or () got ' + \
        str(lab3.nearest_piece(board, 500, 100)) + extra_printout

def test_choose():
    """
    Tests the choose function
    """
    assert lab3.choose(5, 3) == 10, \
        "choose(5, 3): expected 10 got " + str(lab3.choose(5, 3))
    assert lab3.choose(1000, 1) == 1000, \
        "choose(1000, 1): expected 1000 got " + str(lab3.choose(1000, 1))
    assert lab3.choose(52, 5) == 2598960, \
        "choose(52, 5): expected 2598960 got " + str(lab3.choose(52, 5))
    assert lab3.choose(1000, 4) == 41417124750, \
        "choose(1000, 4): expected 41417124750 got " + str(lab3.choose(1000, 4))
    assert lab3.choose(1000, 800) == 661715556065930365627163346132458831897321703017638669364788134708891795956726411057801285583913163781806953211915554723373931451847059830252175887712457307547649354135460619296383882957897161889636280577155889117185,\
        "choose(1000, 800): expected 661715556065930365627163346132458831897321703017638669364788134708891795956726411057801285583913163781806953211915554723373931451847059830252175887712457307547649354135460619296383882957897161889636280577155889117185 got " + \
        str(lab3.choose(100, 800))
    assert lab3.choose(1000, 999) == 1000, \
        "choose(1000, 999): expected 1000 got " + str(lab3.choose(1000, 999))
    assert lab3.choose(5, 5) == 1, \
        "choose(5, 5): expected 1 got " + str(lab3.choose(5, 5))
    assert lab3.choose(0,0) == 1, \
            "choose(1, 1): expected 1 got " + str(lab3.choose(0,0))

if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--test", choices = ["a", "A", "b", "B"],
                            default="", required=False)
    arg_parser.add_argument("file")
    args = arg_parser.parse_args()
    if args.file.rfind("/") != -1:
        sys.path.append(args.file[:args.file.rfind("/")])
        potential_name = args.file[args.file.rfind("/")+1:]
    else:
        sys.path.append(".")
        potential_name = args.file
    if potential_name.rfind("."):
        name = potential_name[:potential_name.rfind(".")]
    else:
        name = potential_name
    try:
        lab3 = SourceFileLoader(name, args.file).load_module()
    except:
        print("Could not import lab: " + args.file)
        print("See traceback for further information:")
        print()
        stack_trace = format_exc().split("\n")
        importlib_has_started = False
        importlib_has_ended = False
        for line in stack_trace:
            if not importlib_has_ended and importlib_has_started and \
               line.lstrip().startswith("File") and "importlib" not in line:
                importlib_has_ended = True
            if importlib_has_ended:
                print(line)
            elif not importlib_has_started and \
                 line.lstrip().startswith("File") and "importlib" in line:
                importlib_has_started = True
        exit(1)
    if args.test.upper() == "A":
        test_board()
    elif args.test.upper() == "B":
        test_choose()
    elif args.test == "":
        test_board()
        test_choose()
    else:
        print("Unknown arguemnt for --test: " + args.test)
        exit(2)
    print("The code passed all the tests")