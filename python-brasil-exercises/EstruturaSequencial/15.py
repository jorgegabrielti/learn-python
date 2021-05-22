'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.

    calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

# Holerite
print('********** HOLERITE **********')
valor_hora = float(input('Digite o valor de sua hora: '))
horas_computadas = int(input('Digite o nº de horas trabalhas no mês: '))

# Porcentagem de descontos (%)
IR = 11
SD = 8
INSS = 5 

# Salário bruto
bruto = valor_hora * horas_computadas

# Salário liquido
liquido = bruto - (bruto * 0.11) - (bruto * 0.08) - (bruto * 0.05)

# Resultado final
print(
    '----------------------------------------\n'
    f'+ Salário Bruto   : R$ {bruto}\n'
    f'- IR (11%)        : R$ {bruto * 0.11}\n' 
    f'- INSS (8%)       : R$ {bruto * 0.08}\n'
    f'- Sindicato (5%)  : R$ {bruto * 0.05}\n'
    f'= Salário Liquido : R$ {liquido}\n'
)