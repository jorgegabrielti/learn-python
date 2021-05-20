'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, utilizando as seguintes fórmulas: 
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''
print('********** O peso ideal para você! **********')
altura = float(input('Digite sua altura: '))

# Calculo
h = (72.7 * altura) - 58   # Homens
m = (62.1 * altura) - 44.7 # Mulheres

# Peso ideal para homens e mulheres
print(
    '----------------------------------------\n'
    f'Peso ideal para homens   : {h: .2f}kg\n'
    f'Peso ideal para mulheres : {m: .2f}kg'
)
