""" 04.252.011/0001-10  40.688.134/0001-61  71 506.168/0001-11   12-544.992/0001-05

 0 4  2  5  2  0 1 1 0  0  0  1
 5 4  3  2  9  8 7 6 5  4  3  2
 0 16 6  10 18 0 7 6 0  0  0  2 = 65

 Fórmula -> 11 - (65 % 11)=1
Primeiro dígito = 1(Se o dígito for maior que 9, ele se torna 0

 0 4  2  5  2  0 1 1 0  0  0  1     x
 6 4  3  2  9  8 7 6 5  4  3  2
 0 20 8  15 4  8 7 0 0  0  3  2 = 65
 Fórmula -> 11 - (67 % 11)=10 (Como o resultado é maioor que 9, então é 00
 Segundo dígito = 0

 Novo CPNJ + Digitos = 04.252.011/0001-10
 CNPJ Original =   04.252.011/0001-10

 recap.
 54329875432 -> Primeiro digito
 6543298765432 -> Segundo digito
 """

import CNPJ
cnpj2 = input('Digite seu cnpj: ')
cnpj1 = '04.252.011/0001-10'

if CNPJ.valida(cnpj1):
    print(f'{cnpj1} é valido')
else:
    print(f'{cnpj1} é invalido')

if CNPJ.valida(cnpj2):
    print(f'{cnpj2} é valido')
else:
    print(f'{cnpj2} é invalido')