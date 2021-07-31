
from functools import lru_cache

import secrets
 

@lru_cache()

def prmntrvls(Lwr,Upr):

    PrimeList = []

    NumList = [x for x in range(Lwr,Upr+1)]

    for Num in NumList:

        if prm(Num) == True:

            PrimeList.append(Num)

    return PrimeList

def prm(Num):

    if Num <= 1:

        return False

    control = 2

    while control <= Num**0.5:

        if Num % control == 0:

            return False

        control += 1

    return True

Lwr = 1

Upr = 1000

FrstNmbr = secrets.choice(prmntrvls(Lwr, Upr))

ScndNmbr = secrets.choice(prmntrvls(Lwr, Upr))

print('El intervalo seleccionado es: [{},{}]. \nLos números primos aleatorios (clave privada) son: {} y {}. \nLa clave pública es: {}.'.format(Lwr,Upr,FrstNmbr,ScndNmbr,FrstNmbr*ScndNmbr))