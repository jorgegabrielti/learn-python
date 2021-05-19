# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
print('********** CONVERSOR DE GRAUS **********')
print('Fahrenheit => Celsius')
F = float(input('Digite a temperatura em grau Fº: '))

# Calculo
C = 5 * (F - 32) / 9

# Resultado
print(
    '----------------------------------------\n'
    f'Temperatura informada : {F}Fº\n'
    f'Temperatura convertida: {C}Cº'
)