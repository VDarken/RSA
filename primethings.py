
from functools import lru_cache

@lru_cache()


def prmntrvls(Lwr,Upr):

    PrimeList = []

    NumList = [x for x in range(Lwr,Upr+1)]

    for Num in NumList:

        if is_prime(Num) == True:

            PrimeList.append(Num)

    return PrimeList

def is_prime(Num):
    
    if Num <= 1:

        return False

    control = 2

    while control <= Num**0.5:

        if Num % control == 0:

            return False

        control += 1

    return True

print(prmntrvls(1,150))