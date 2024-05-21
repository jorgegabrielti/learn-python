# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
print('ACADEMIA FITNESS - Levando você ao ideal!')

altura = float(input('Digite sua altura: '))
peso_ideal = (72.7 * altura) - 58

# Peso ideal
print(f'Peso ideal: {peso_ideal: .2f}kg')