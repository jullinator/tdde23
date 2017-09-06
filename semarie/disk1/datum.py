# encode = utf-8
from calendar import monthrange
from datetime import date

A = (30, 1)
B = (12, 12)
C = (4 ,9)
D = (1, 6)
E = (2,6)
BDAYS = [A, B, C, D, E]




def closest_bday(mon, day):
    """
    Givet en statisk uppsättning födelsedagar, returnerna namnet på den person som fyller år närmast mon, day.
    Exempel givet A 30/1 39,1 -> A; 1,1-> B; 1,6-> A(om lika, ta nästa)
    """
    date1= date(2017, mon, day)
    min_mdif = 20
    #list comprehens
    #sort, take first.
    for bday in range(len(BDAYS)):
        pass


closest_bday(1,2)