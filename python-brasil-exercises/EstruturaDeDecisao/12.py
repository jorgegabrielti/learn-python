'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do 
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário
Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas 
trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
print('********** FOLHA DE PAGAMENTO **********')
valor_hora = float(input('Valor de sua hora: R$ '))
horas_trabalhadas = int(input('Horas trabalhadas: '))

bruto = valor_hora * horas_trabalhadas

# Descontos
desc_ir = 0
sind = 0.03
fgts = 0.11
inss = 0.10

if bruto <= 900:
    desc_sind = bruto * sind
    desc_fgts = bruto * fgts
    desc_inss = bruto * inss
elif bruto <= 1500:
    desc_ir = bruto * 0.5
    desc_sind = bruto * sind
    desc_fgts = bruto * fgts
    desc_inss = bruto * inss
elif bruto <= 2500:
    desc_ir = bruto * 0.10
    desc_sind = bruto * sind
    desc_fgts = bruto * fgts
    desc_inss = bruto * inss
else:
    desc_ir = bruto * 0.20
    desc_sind = bruto * sind
    desc_fgts = bruto * fgts
    desc_inss = bruto * inss

descontos = desc_ir + desc_sind + desc_inss 
liquido = bruto - descontos 

print(
    f'Salário Bruto                   : R$ {bruto}\n'
    f'(-) IR (5%)                     : R$ {desc_ir}\n' 
    f'(-) SINDICATO                   : R$ {desc_sind}\n'
    f'(-) INSS ( 10%)                 : R$ {desc_inss}\n'
    f'FGTS (11%)                      : R$ {desc_fgts}\n'
    f'Total de descontos              : R$ {descontos}\n'
    f'Salário Liquido                 : R$ {liquido}'
)