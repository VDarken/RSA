
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

def phi(a,b):

    return (a - 1)*(b - 1)

Lwr = 1

Upr = 1000

FrstPrmNmbr = secrets.choice(prmntrvls(Lwr, Upr))

ScndPrmNmbr = secrets.choice(prmntrvls(Lwr, Upr))

NmbrVIP = FrstPrmNmbr*ScndPrmNmbr

EulerPhi = phi(FrstPrmNmbr,ScndPrmNmbr)

print(f'El intervalo seleccionado es: [{Lwr},{Upr}].')
print(f'Los números primos aleatorios son: {FrstPrmNmbr} y {ScndPrmNmbr}.')
print(f'El número VIP es: {NmbrVIP}.')
print(f'El número de Euler es: {EulerPhi}.')
