
from functools import lru_cache

@lru_cache()

def prmntrvls(Lwr,Upr):

    Bin = []

    NumList = [nbr for nbr in range(Lwr,Upr+1)]

    for Num in NumList:

        Control = 2

        while Control <= Num**0.5:

            if Num % Control == 0:

                Bin.append(Num)

            Control += 1

    return [x for x in NumList if x not in Bin]

print(prmntrvls(2,100))
