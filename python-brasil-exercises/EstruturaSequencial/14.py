'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para
controlar o rendimento diário de seu trabalho. Toda vez que ele traz 
um peso de peixes maior que o estabelecido pelo regulamento de pesca 
do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e 
calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e 
na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa 
com as mensagens adequadas.
'''
# Papo de pescado
print('********** PESQUE-PAGE - PAPO DE PESCADOR **********')

# Constantes
limite_isento = 50
valor_multa_kg = 4.0

peso = float(input('Digite o peso do pescado: '))

# Calculos
excesso = peso - limite_isento
multa_excesso = excesso * valor_multa_kg

# Resultados da pescaria
print(
    '# Pescaria ----------------------\n'
    f'Kilos pescados        : {peso}kg\n'
    f'Kilos excedidos       : {excesso}kg\n'
    f'Multa por kg excedido : R$ {multa_excesso}\n'
    '-----------------------------------'
)