
from functools import lru_cache

from string import ascii_lowercase 

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

def gcd(Num1,Num2):

    if Num1 < Num2:

        Num1, Num2 = Num2, Num1
 
    Rmndr = Num1 % Num2
 
    if Rmndr == 0:

        return Num2
 
    return gcd(Num2,Rmndr)

Lwr = 1

Upr = 1000

FrstPrmNmbr = secrets.choice(prmntrvls(Lwr, Upr))

ScndPrmNmbr = secrets.choice(prmntrvls(Lwr, Upr))

FrstPubKey = FrstPrmNmbr*ScndPrmNmbr

UprNmbr = phi(FrstPrmNmbr,ScndPrmNmbr)

CoPrimesList = []

for i in range(1,UprNmbr + 1):

    if gcd(UprNmbr,i) == 1:

        CoPrimesList.append(i)

ScndPubKey = max(CoPrimesList)

print(f'El intervalo seleccionado es: [{Lwr},{Upr}].')

print(f'Los números primos aleatorios son: {FrstPrmNmbr} y {ScndPrmNmbr}.')

print(f'La clave pública es: ({FrstPubKey},{ScndPubKey})')

for j in range(1,UprNmbr + 1):

    if (j * ScndPubKey) % UprNmbr == 1:

        PrivKey = j

print(f'La clave privada es: {PrivKey}')

mapping = dict(zip(ascii_lowercase, range(1, 27)))

Strng = input('Message: ')

NmbrsMsg = [str(mapping[char]) for char in Strng if char in mapping]

print(f'La lista de números asociados al mensaje es: {NmbrsMsg}')

NmbrsMsgFull = int(''.join(NmbrsMsg))

print(f'El número asociado al mensaje es: {NmbrsMsgFull}')

CddMsg = (NmbrsMsgFull**ScndPubKey) % FrstPubKey

print(f'El mensaje codificado es: {CddMsg}')

DcdMsg = (CddMsg**PrivKey) % FrstPubKey

print(f'El mensaje decodificado es: {DcdMsg}')