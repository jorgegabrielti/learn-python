# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('********** VALIDAÇÃO DE TURNO DE TRABALHO **********')
print(
    'M-matutino\n'
    'V-Vespertino\n'
    'N-Noturno'
)
turno = input('Digite o turno de trabalho [M/m | V/v | N/n]: ').lower()
mensagem= 'Bom dia!'

# Validação
if turno != 'm' and turno != 'v' and turno != 'n':
    print(f'Turno inválido: [{turno}]')
    exit(0)

if turno == 'v':
    mensagem = 'Boa tarde!'
elif turno == 'n':
    mensagem = 'Boa noite!'

print(f'Mensagem: {mensagem}')