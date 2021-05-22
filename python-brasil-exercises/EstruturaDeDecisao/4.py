# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
print('********** VOGAL ou CONSOANTE **********')
l_original = str(input('Digite uma letra: ')) # letra original digitada pelo usuário
l_tratamento = l_original.lower()             # utilizada para tratamento no código.

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

# Validacao
if (l_tratamento in alfabeto) == False:
    print(f'Não é letra: [{l_tratamento}]')
    exit(0)


if l_tratamento in 'aeiou':
    print(f'É vogal: [{l_original}]')
else:
    print(f'É consoante: [{l_original}]')
