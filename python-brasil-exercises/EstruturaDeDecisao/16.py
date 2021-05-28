'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve
    fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. 
    Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
print('********** Equação do 2º grau **********\n')
a = float(input('Digite o valor de (a): '))

# Validando coeficiente a
if a == 0:
    print('Coeficiente (a) precisa ser diferente de 0 => a ≠ 0')
    exit(0)

b = float(input('Digite o valor de (b): '))
c = float(input('Digite o valor de (c): '))

delta = (b**2) - 4 * a * c

if delta < 0:
    print('Equação não possui raízes reais')
    exit(0)
elif delta == 0:
    mensagem = 'Equação possui apenas uma raiz real'
else:
    mensagem = 'Equação possui duas raizes reais: '

# Validando tipo de equação (completa/incompleta)
# Completa => a ≠ 0, b ≠ 0 e c ≠ 0
if b != 0 and c !=0:
    tipo_equacao = 'Completa' # Aplicar fórmula de bhaskara
    x1 = (b + (delta ** (1/2))) / (2 * a)
    x2 = (b - (delta ** (1/2))) / (2 * a)
else:
    tipo_equacao = 'Incompleta'
    x1 = (b + (delta ** (1/2))) / (2 * a)
    x2 = (b - (delta ** (1/2))) / (2 * a)


print(
    '\n'
    f'Equação        : {int(a)}x² - {int(b)}x + {int(c)} = 0\n'
    f'Tipo de equação: {tipo_equacao}\n'
    f'{mensagem}\n' 
    f'x1 = {x1}\n'
    f'x2 = {x2}'
)





