'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média 
alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
print('********** MÉDIA DE NOTAS **********')
nota1 = float(input('Digite a nota nº 1: '))
nota2 = float(input('Digite a nota nº 2: '))

media = (nota1 + nota2) / 2

if media < 7:
    situacao = 'Reprovado'
elif media >= 7 and media < 10:
    situacao = 'Aprovado'
else:
    situacao = 'Aprovado com distinção'

print(
    f'******* RESULTADO *******\n\n'
    f'Notas: \n'
    f'1º: {nota1}\n'
    f'2º: {nota2}\n'
    '------------\n'
    f'Média final: {media} => ### {situacao} ###'
)