# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
print('********** + ou - **********')
valor = float(input('Digite um valor qualquer: '))

# Valor padrão
tipo = 'positivo'

# Validação
if valor < 0:
    tipo = 'negativo'

# Output
print(
    f'Valor digitado: [{valor}] => {tipo}'
)