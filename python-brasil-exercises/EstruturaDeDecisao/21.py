'''
Faça um Programa para um caixa eletrônico:

- O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
- As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
- O valor mínimo é de 10 reais e o máximo de 600 reais. 
- O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

# input
saque = int(input("Informe o valor do saque (Min => R$ 10,00 Max => R$ 600,00): "))

if 10 < saque > 600:
    print("Valor inválido!")
    exit(0)
else:
    notas_100 = saque // 100
    saque %= 100
    
    notas_50 = saque // 50
    saque %= 50
    
    notas_10 = saque // 10
    saque %= 10
    
    notas_1 = saque
    
mensagem = "Saque realizado com sucesso!"

print(mensagem.center(34,"#"))

if notas_100 > 0:
    print(f"- {notas_100} notas(s) de R$ 100,00")
    
if notas_50 > 0:
    print(f"- {notas_50} notas(s) de R$ 50,00")
    
if notas_10 > 0:
    print(f"- {notas_10} notas(s) de R$ 10,00")

if notas_1 > 0:
    print(f"- {notas_1} notas(s) de R$ 1,00")