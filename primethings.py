
from functools import lru_cache

@lru_cache()

def prmntrvls(Lwr,Upr):

    Bin = []

    NumList = [nbr for nbr in range(Lwr,Upr+1)]

    for Num in NumList:

        control = 2

        while control <= Num**0.5:

            if Num % control == 0:

                Bin.append(Num)

            control += 1

    return [x for x in NumList if x not in Bin]

print(prmntrvls(2,100))
