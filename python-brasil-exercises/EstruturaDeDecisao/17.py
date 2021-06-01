# Faça um Programa que peça um número correspondente a um determinado ano e em
# seguida informe se este ano é ou não bissexto.
print('********** ANO BISEXTO **********')
ano = int(input('Digite o ano [yyyy]: '))

bisexto = False

if ano % 4 == 0 and ano % 100 != 0:
    bisexto = True
elif ano % 400 == 0:
    bisexto = True

print(f'Ano de {ano} bisexto: {bisexto}')
