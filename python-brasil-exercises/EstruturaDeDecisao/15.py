'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser
    um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
'''
print('********* TRIÂNGULO **********')

l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

# Valida triângulo
if (l1 < l2  +l3) or (l2 < l1 + l3) or (l3 < l1 + l2):
    print('É UM TRIANGULO!')
else:
    print('NÃO É UM TRIÂNGULO!')

# Tipo de triângulo
if (l1 == l2) and (l1 == l3):
    print('TRIÂNGULO EQUILÁTERO!')
elif (l1 == l2) or (l1 ==l3) or (l2 == l3):
    print('TRIÂNGULO ISÓSCELES')
else:
    print('TRIÂNGULO ESCALENO')
