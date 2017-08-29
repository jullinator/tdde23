import math
def check_pnr (pnr=[]):
    """
    Kollar om kontrollnumret i ett personnummer stämmer.
    """
    sum = 0
    for x in range(pnr):
        mult = 1
        if x % 2 == 0:
            mult = 2
        tempsum = mult * pnr[x]
        rest = tempsum % 10
        sum += (tempsum - rest)/10
        sum += rest
        print(sum)





"""
Uppgift 2 - Personnummer

Skriv en funktion check_pnr som tar ett personnummer i form av en lista med tio siffror på formen [å, å, m, m, d, d, x, x, x, k] och kontrollerar att kontrollsiffran, den sista siffran, är korrekt. Dela upp uppgiften i flera mindre funktioner som du kan testköra för sig. Om funktionerna utför någon form av upprepning får du själv välja metod, iteration eller rekursion.

Metoden för att räkna ut kontrollsiffran i personnummer är enligt följande. Multiplicera alla siffror utom den sista med omväxlande 2 och 1. Summera de enskilda siffrorna i produkterna (dvs om produkten är 2*5 = 10 så summerar vi 1 och 0). Kontrollsiffran är skillnaden mellan nästa högre (eller samma) tiotal och summan av siffrorna.

Personnummer: 7 2 0 1 2 3 1 2 3
Viktsiffror:  2 1 2 1 2 1 2 1 2
-------------------------------------
Produkt:     14 2 0 1 4 3 2 2 6
Siffersumma: 1+4+2+0+1+4+3+2+2+6 = 25
Närmast högre tiotal: 30
Kontrollsiffra: 30-25 = 5


>>> check_pnr([7, 4, 0, 2, 1, 7, 4, 8, 2, 0])
True
>>> check_pnr([7, 4, 0, 2, 1, 7, 4, 8, 2, 1])
False

Testning För att se till att din funktion klarar av uppgiften finns det ett pythonprogram som kör automatisk testning på din kod. Programmet kan antingen hämtas (test_2.py) om du inte befinner dig på datorerna i SU-salarna eller köras direkt från filsystemet (~TDDE23/www-pub/labbar/tester/test_2.py) om du befinner dig på en av datorerna i ovannämnda salar. Öppna filen och läs instruktionerna för hur man för att se hur man kör programmet och kör det sedan för att testa labb 1B.


"""