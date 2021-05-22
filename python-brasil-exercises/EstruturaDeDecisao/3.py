# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra, escrever: F - Feminino, M - Masculino, Sexo Inválido.
print('********** VALIDAÇÃO DO SEXO **********')
print(
    'F - Feminino\n'
    'M - Masculino'
)

sexo = input('Digite o sexo [F/f | M/m]: ').lower()
default_sexo = 'F - Feminino'

# Validação
if sexo != 'f' and sexo != 'm':
    print(f'Sexo inválido: [{sexo}]')
    exit(0)
elif sexo == 'm':
    default_sexo = 'M - Masculino'

print(f'Sexo: {default_sexo}')



