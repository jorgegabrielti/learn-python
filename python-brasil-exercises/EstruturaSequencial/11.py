'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
terceiro elevado ao cubo.
'''
print('********** CÁLCULOS MATEMÁTICOS **********')
print('Acertô miserávi!')

# Entrada de dados
i1 = int(input('Digite o 1º número inteiro: '))
i2 = int(input('Digite o 2º número inteiro: '))
f1 = float(input('Digite o 1º número real: '))

# Cálculo 1: produto do dobro do 1º com metade do 2º
calculo1 = i1 * (i2 / 2)

# Cálculo 2: soma do triplo do 1º com o 3º
calculo2 = (i1 * 3) + f1

# Cálculo 3: 3º elevado ao cudo
calculo3 = f1 ** 3

print('------------ RESULTADOS ------------')
print(
    f'Cálculo 1: produto do dobro do 1º com metade do 2º ==> {calculo1}\n'
    f'Cálculo 2: soma do triplo do 1º com o 3º ==> {calculo2}\n'
    f'Cálculo 3: 3º elevado ao cudo ==> {calculo3}\n'
    'Ah, miserávi !'
)