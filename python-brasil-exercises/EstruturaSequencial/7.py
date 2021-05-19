# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# Fórmula: A = b.h 
'''
Onde:
   A => área do quadrado;
   b => base;
   h => altura.
'''
print('********** ÁREA DO QUADRADO **********')
l = float(input('Digite a medida de um dos lados: '))

# Cálculo
a = l ** 2

# Resultado
print(
    f'Lados do quadrado: {l} x {l}m²\n'
    f'Área do quadrado: {a}m²'
)