
from string import ascii_lowercase 

FrstPubKey = 33
ScndPubKey = 7
UprNmbr = 20
PrivKey = 3

Strng = input('Message: ')

mapping = dict(zip(ascii_lowercase, range(1, 27)))

NmbrsMsg = [str(mapping[char]) for char in Strng if char in mapping]
print(f'La lista de números asociados al mensaje es: {NmbrsMsg}')

NmbrsMsgFull = int(''.join(NmbrsMsg))         
print(f'El número asociado al mensaje es: {NmbrsMsgFull}',type(NmbrsMsgFull))

CddMsg = (NmbrsMsgFull**ScndPubKey) % FrstPubKey
print(f'El mensaje codificado es: {CddMsg}')

DcdMsg = (CddMsg**PrivKey) % FrstPubKey
print(f'El mensaje decodificado es: {DcdMsg}')
