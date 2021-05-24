# Faça um programa que pergunte o preço de três produtos e 
# informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
print('********** PRODUTO MAIS BARATO **********\n')

produto1 = float(input('Produto 1 - Informe o valor: R$ '))
produto2 = float(input('Produto 2 - Informe o valor: R$ '))
produto3 = float(input('Produto 3 - Informe o valor: R$ '))
print('')
# Produto mais barato
if produto1 < produto2 and produto2 < produto3:
    comprar = 'Produto 1: R$ ' + str(produto1)
elif produto2 < produto1 and produto2 < produto3:
    comprar = 'Produto 2: R$ ' + str(produto2)
else:
    comprar = 'Produto 3: R$ ' + str(produto3)

print(
    f' --- Produto +barato ---\n\n'
    f'{comprar}'
)