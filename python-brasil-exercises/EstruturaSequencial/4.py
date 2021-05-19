# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# Entrada de dados para as notas
n1 = float(input('Digite a nota nº1: '))
n2 = float(input('Digite a nota nº2: '))
n3 = float(input('Digite a nota nº3: '))
n4 = float(input('Digite a nota nº4: '))

# Soma dos valores de entradas
media = (n1 + n2 + n3 + n4) / 4

print('********** RESULTADO **********')
print(
    f'Notas bimestrais: \n'
    f'n1 => {n1}\n'
    f'n1 => {n2}\n'
    f'n1 => {n3}\n'
    f'n1 => {n4}\n'
    '--------------------------------\n'
    f'Média final => {media}', 
)