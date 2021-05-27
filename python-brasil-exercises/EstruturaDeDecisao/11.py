'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no 
salário atual:
    salários até R$ 280,00 : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
'''
print('********** ORGANIZAÇÕES TABAJARA **********\n')
print('### FOLHA DE PAGAMENTO\n')

salario = float(input('Digite o salário atual do colaborador: R$ '))
salario_reajuste = 0
print('')

if salario <= 0:
    print('Salário não pode ser menor que 0')
    exit(0)

if salario <= 280:
    salario_reajuste +=  + (salario * 0.20)
elif salario <= 700:
    salario_reajuste += + (salario * 0.15)
elif salario <= 1500:
    salario_reajuste += + (salario * 0.10)
else:
    salario_reajuste += + (salario * 0.05)

print(
    '--------------------------------------------------------\n'
    f'o salário antes do reajuste       : R${salario: .2f}\n'
    f'o percentual de aumento aplicado  : {int((salario_reajuste / salario) * 100)}%\n'
    f'o valor do aumento                : R${salario_reajuste: .2f}\n'
    f'o novo salário, após o aumento    : R${salario + salario_reajuste: .2f}'
)