# Faça um Programa que peça dois números e imprima o maior deles.
print('********** MAIOR DE DOIS *********')
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))

# Valor inicial
maior = n2

# Condição
if n1 > n2:
    maior = n1

print(
    f'Núméros digitados: \n'
    f'1º => {n1}\n'
    f'2º => {n2}\n\n'
    f'Maior => {maior}'
)