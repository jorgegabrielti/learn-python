# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
print('********** DAYS OF THE WEEK *********\n')
dia = input('Digite o dia da semana: ')

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

if (dia in alfabeto) != False:
    print(f'Um número é esperado')
    exit(0)

dia = int(dia)

if dia < 1 or dia > 7:
    print('Valor inválido!')
    exit(0)

dia = str(dia)

# Dicionário dos dias da semana
# Uso de dicionário é para evitar muitas condições if, elif e else
dias = {
    "1":"domingo", 
    "2":"segunda", 
    "3":"terça", 
    "4":"quarta",
    "5":"quinta", 
    "6":"sexta", 
    "7":"sábado"
}

# Obtendo o dia a partir da key
dia_semana = dias.get(dia)

print(f'{dia}-{dia_semana}')