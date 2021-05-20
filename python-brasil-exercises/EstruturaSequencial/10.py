# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# F = (C x 1.8) + 32
print('********** CONVERSOR DE GRAUS **********')
print('Celsius => Fahrenheit')
C = float(input('Digite a temperatura em grau Cº: '))

# Calculo
F = C * 1.8 + 32

# Resultado
print(
    '----------------------------------------\n'
    f'Temperatura informada : {C}Cº\n'
    f'Temperatura convertida: {F}Fº'
)