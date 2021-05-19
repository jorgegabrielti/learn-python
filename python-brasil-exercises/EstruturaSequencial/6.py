# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# Formula: A = pi * r(2)
'''
Onde:
  A    => area;
  pi   => 3.14;
  r(2) => raio ao quadrado
'''
print('********** ÁREA DE UMA CIRCUNFERÊNCIA **********')
r = float(input('Digite o raio do círculo: '))

# Calculo
pi = 3.1415926535898
a = pi * (r ** 2)

# Resultado
print(
    f'* Detalhes do circulo\n'
    f'Raio: {r}m\n'
    f'Área: {a:.2f}m²\n'
)

# Observacao
print('# O programa considera metros como medidada padrão')