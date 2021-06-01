'''
# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
# dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
   - 326 = 3 centenas, 2 dezenas e 6 unidades 
   - 12 = 1 dezena e 2 unidades 
Testar com: 
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
print('********* < 1000 *********')
n = input('Digite um número > 1000: ')

# Validação
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

if (n in alfabeto) != False:
    print(f'### O item precisam ser um número ###')
    exit(0)

n = int(n)

if n > 1000:
    print('O número dever ser > 1000')
    exit(0)

centena = 'centena' 
dezena = 'dezena'
unidade = 'unidade'

if str(len(str(n))) == '3':
    c = int(str(n)[0:1])
    d = int(str(n)[1:2])
    u = int(str(n)[2:3])
    if c > 1:
        centena = 'centenas'
    if d > 1:
        dezena = 'dezenas'
    if u > 1:
        unidade = 'unidades'
    mensagem = f'{c} {centena}, {d} {dezena} e {u} {unidade}'
elif str(len(str(n))) == '2':
    d = int(str(n)[0:1])
    u = int(str(n)[1:2])
    if d > 1:
        dezena = 'dezenas'
    if u > 1:
        unidade = 'unidades'
    mensagem = f'{d} {dezena} e {u} {unidade}'
else:
    u = int(str(n)[0:1])
    if u > 1:
        unidade = 'unidades'
    mensagem = f'{u} {unidade}'

print(
    f'{mensagem}'
)