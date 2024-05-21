# Faça um Programa que leia três números e mostre o maior deles.
print('********** MAIOR DE 3 *********')

n1 = input('Digite o 1º número: ')
n2 = input('Digite o 2º número: ')
n3 = input('Digite o 3º número: ')

# Validação
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

if (n1 in alfabeto) or (n2 in alfabeto) or (n3 in alfabeto):
    print(f'### Os três (03) items precisam ser números ###')
    exit(0)

# Typecast para float
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

# Comparação
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print(
    '---------- RESULTADO ----------\n\n'
    'Números digitados: \n'
    f'1º: {n1}\n'
    f'2º: {n2}\n'
    f'3º: {n3}\n\n'
    f'Maior => {maior}\n'
)