# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = str(input('Digite a data: '))

d = int(data[:2])
m = int(data[3:5])
a = int(data[6:10])

# Validação de dias possíveis em um mês e meses possíveis em um ano
# 1 - 31
if d < 1 or d > 31:
    print('Dia inválido !')
    exit(0)

if m < 1 or m > 12:
    print('Mês inválido !')
    exit(0)

# Dicionário meses com 30 dias.
dias_meses = {
    'fevereiro' : '28',
    'abril' : '30',
    'junho' : '30',
    'setembro' : '30',
    'novembro' : '30',
}

# Números dos meses com dias
meses_30 = ['04', '4', '06', '6', '09', '9', '11']

# Validação de ano bisexto
bisexto = False

if a % 4 == 0 and a % 100 != 0:
    bisexto = True
    dias_meses['fevereiro'] = "29"
elif a % 400 == 0:
    bisexto = True

d = str(d)
m = str(m)

data_valida = True

if (m == '02' or m == '2') and (bisexto == True) and ((d in dias_meses.get('fevereiro')) > 29) != True:
    data_valida = False
elif m in meses_30:
    dias_meses.pop('fevereiro')
    if d > dias_meses.get('abril') or d > dias_meses.get('junho') or d > dias_meses.get('setembro') or d > dias_meses.get('novembro'):
        data_valida = False

print(
    f'Data válida: {data_valida}\n\n'
    f'{d}/{m}/{a}\n'
    f'Ano bisexto: {bisexto}'
)