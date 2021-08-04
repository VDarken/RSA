
from functools import lru_cache     # Para que los datos se guarden en la caché.

from string import ascii_lowercase  # Para pasar a números el mensaje.

import secrets                      # Para elegir aleatoriamente los primos.

@lru_cache()

#################################################################################################################################

# Selección del intervalo de números y creación de la lista de números primos.

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

#################################################################################################################################

# Función que calcula el número "s" (cota superior). 

def phi(a,b):

    return (a - 1)*(b - 1)

#################################################################################################################################

# Función que calcula el máximo común divisor de dos números.

def gcd(Num1,Num2):

    if Num1 < Num2:

        Num1, Num2 = Num2, Num1
 
    Rmndr = Num1 % Num2
 
    if Rmndr == 0:

        return Num2
 
    return gcd(Num2,Rmndr)

#################################################################################################################################

# Establecimiento de las cotas superior e inferior del intervalo de números.

Lwr = 1

Upr = 1000

#################################################################################################################################

# Elección aleatoria de los números primos sobre los que se construye el codificado del mensaje.

FrstPrmNmbr = secrets.choice(prmntrvls(Lwr, Upr))

ScndPrmNmbr = secrets.choice(prmntrvls(Lwr, Upr))

#################################################################################################################################

# Primera parte de la clave pública (el producto de los dos números primos anteriores).

FrstPubKey = FrstPrmNmbr*ScndPrmNmbr

#################################################################################################################################

# Cálculo del número "s" (cota superior).

UprNmbr = phi(FrstPrmNmbr,ScndPrmNmbr)

#################################################################################################################################

# Segunda parte de la clave pública. Se elige el máximo número coprimo con UprNmbr (el número cota superior), en un intervalo 
# entre 1 y UprNmbr.

# Nota: el máximo común divisor entre dos números coprimos es igual a 1.

CoPrimesList = []

for i in range(1,UprNmbr + 1):

    if gcd(UprNmbr,i) == 1:

        CoPrimesList.append(i)

ScndPubKey = max(CoPrimesList)

#################################################################################################################################

# Impresión por pantalla de los datos calculados hasta el momento: el intervalo seleccionado, los números primos seleccionados 
# aleatorioamente y la clave pública.

print(f'El intervalo seleccionado es: [{Lwr},{Upr}].')

print(f'Los números primos aleatorios son: {FrstPrmNmbr} y {ScndPrmNmbr}.')

print(f'La clave pública es: ({FrstPubKey},{ScndPubKey})')

#################################################################################################################################

# Creación de la clave privada (PrivKey). 

for j in range(1,UprNmbr + 1):

    if (j * ScndPubKey) % UprNmbr == 1:

        PrivKey = j

print(f'La clave privada es: {PrivKey}')

#################################################################################################################################

# Introducción por pantalla del mensaje para codificar y asociación de este a un número.

Strng = input('Message: ')

mapping = dict(zip(ascii_lowercase, range(1, 27)))

NmbrsMsg = [int(mapping[char]) for char in Strng if char in mapping]        # Mensaje codificado por números en forma de lista. 

print(f'La lista de números asociados al mensaje es: {NmbrsMsg}',len(NmbrsMsg))

#################################################################################################################################

# Codificación del mensaje a partir de su número asociado. 

CddMsg = [(x**ScndPubKey) % FrstPubKey for x in NmbrsMsg]                      

print(f'El mensaje codificado es: {CddMsg}',len(CddMsg))

#################################################################################################################################

# Decodificación del mensaje a partir del número codificado.

DcdMsg = [(x**PrivKey) % FrstPubKey for x in CddMsg]         

print(f'El mensaje decodificado es: {DcdMsg}',len(DcdMsg))




