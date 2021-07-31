
from functools import lru_cache

@lru_cache()

def prmntrvls(Lwr,Upr):

    NumList = [nbr for nbr in range(Lwr,Upr+1)]

    Bin = []

    for Num in NumList:

        Control = 2

        while Control <= Num**0.5:

            if Num % Control == 0:

                Bin.append(Num)

            Control += 1

    PrimeList = [x for x in NumList if x not in Bin]

    return PrimeList 

print(prmntrvls(2,10))