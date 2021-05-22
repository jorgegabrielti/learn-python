'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da 
área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que 
custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
print('********** LOJA DE TINTAS - SEU LAR, SUA CARA **********')
area = float(input('Digite a área de ser pintada: '))

# Quantidade de litros necessários
# Cobertura de 1lt => 6mt
litros = area / 6 
litros_folga = litros + (litros * 0.10)

# Condição p/ lata de 18lt
# Lata: 18lt => 108m²
latas = litros // 18 + 1
latas_folga = litros_folga // 18 + 1

# Condição p/ galão de tinta de 3.6lt
# Galão: 3.6lt => 21.6m²
galoes = litros // 3.6 + 1
galoes_folga = litros_folga // 3.6 + 1

# Condição para latas e galões misturados
lata_combinada = litros // 18
galao_combinado = (litros % 18) // 3.6 + 1
custo_combinado = lata_combinada * 80 + galao_combinado * 25

print(
    f'\nÁrea a ser pintada      : {area: .2f} m²\n\n'
    f'Litros necessários      : {litros: .2f} lt\n'
    f'Litros necessários +10% : {litros_folga: .2f}lt\n\n'
    f'********************* CONDIÇÕES *********************\n'
    f'--- Galões de 3.6lt --- \n'
    f'Quant       : {galoes}\n'
    f'Quant +folga: {galoes_folga}\n'
    f'Custo       : R$ {galoes * 25: .2f}\n'
    f'Custo +folga: R$ {galoes_folga * 25: .2f}\n\n'
    f'--- Latas de 18lt --- \n'
    f'Quant       : {latas}\n'
    f'Quant +folga: {latas_folga}\n'
    f'Custo       : R$ {latas * 80: .2f}\n'
    f'Custo +folga: R$ {latas_folga * 80: .2f}\n\n'
    f'--- Latas de 18lt + galões de 3.6lt --- \n'
    f'Quant.lata  : {lata_combinada}\n'
    f'Quant.galão : {galao_combinado}\n'
    f'Custo       : R$ {custo_combinado: .2f}'
)