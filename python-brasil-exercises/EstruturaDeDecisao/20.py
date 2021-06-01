'''
Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

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
nota3 = float(input('Digite a nota nº 3: '))

media = (nota1 + nota2 + nota3) / 3

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
    f'3ª: {nota3}\n'
    '------------\n'
    f'Média final: {media} => ### {situacao} ###'
)