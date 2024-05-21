# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print('********** CÁLCULOS TRABALHISTAS **********')

valor_hora = float(input('Digite o valor de sua hora: '))
horas_trabalhadas = int(input('Horas trabalhadas: '))

# Cálculo
salario = valor_hora * horas_trabalhadas

mensagem = f'''
SALÁRIO BRUTO

VALOR DA HORA    : R$ {valor_hora}
HORAS TRABALHADAS: R$ {horas_trabalhadas}
-------------------------------------------
SALÁRIO          : R$ {salario:.2f}
'''

print(mensagem)

'''
print('-------------------------------')
print('SALÁRIO BRUTO')
print(
    f'Valor da hora    : R$ {valor_hora}\n'
    f'Horas trabalhadas: {horas_trabalhadas}h\n'
    '---------------------------------\n'
    f'Salário          : R$ {salario}'
)
'''