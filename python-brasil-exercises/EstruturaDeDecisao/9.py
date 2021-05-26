# Faça um Programa que leia três números e mostre-os em ordem decrescente.
print('********** ORDEM DECRESCENTE **********\n')

n1 = input('Número 1: ')
n2 = input('Número 2: ')
n3 = input('Número 3: ')
print('')

# Validação
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

if (n1 in alfabeto) != False or (n2 in alfabeto) != False or (n3 in alfabeto) != False:
    print(f'### Os três (03) items precisam ser números ###')
    exit(0)

# Typecast para float
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

if n1 < n3:
    n1, n3 = n3, n1

if n1 < n2:
    n1, n2 = n2, n1

if n2 < n3:
    n2, n3 = n3, n2

print(f'Ordem decrescente é [{n1}], [{n2}] e [{n3}]')
