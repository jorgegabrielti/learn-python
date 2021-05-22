'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
print('********** LOJA DE TINTAS - SEU LAR, SUA CARA **********')
area = float(input('Digite a área de ser pintada: '))

# Condição
if area % 54 == 0:
    latas = int(area / 54)
else:
    latas = int(area / 54) + 1

# Cálculo de custo total
total = latas * 80.00

print(
    f'Área a ser pintada: {area: .0f}m²\n'
    f'Latas de tintas   : {latas}\n'
    f'------------------------------\n'
    f'Total             : R$ {total}'
)