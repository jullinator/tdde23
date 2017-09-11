# encode = utf-8
from calendar import monthrange
from datetime import date

A = (30, 1)
B = (12, 12)
C = (4 ,9)
D = (1, 6)
E = (2,6)
BDAYS = [A, B, C, D, E]
YEAR = 2017

def closest_generator (seq,date):
    min_dif = 365
    for i in seq:
        min_dif = min(i, min_dif)
        yield min_dif

def closest_bday(mon, day):
    """
    Givet en statisk uppsättning födelsedagar, returnerna namnet på den person som fyller år närmast mon, day.
    Exempel givet A 30/1 39,1 -> A; 1,1-> B; 1,6-> A(om lika, ta nästa)
    """
    date1= date(YEAR, mon, day)
    min_dif=365
    min_dif_index = -1

    def calc_dif(d):
        date2 = date(YEAR, d[1], d[0])
        delta = (date1 - date2)
        return abs(delta.days)

    dif = [calc_dif(d) for d in BDAYS]
    for d in range(len(dif)):
        item = dif[d]
        if item <= min_dif:
            min_dif = item
            min_dif_index = d
    print(min_dif_index)
    print(dif)

    #sort, take first.

def closest_b_day_2 (mon, day):
    date1 = date(YEAR, mon, day)
    for d in range(len(BDAYS)):
        item = BDAYS[d]



closest_bday(1,2)