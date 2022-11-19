'''
censo (extra):

Faça um programa que peça para n pessoas a sua idade,
ao final o programa deverá verificar se a média de idade da turma varia entre:

0 e 25 -> informar que a turma é jovem
26 e 60 -> informar que a turma é adulta
maior que 60 -> informar que a turma é idosa

'''

qnt = int(input('Quantas pessoas serão inserida?'))
total = 0
for i in range(1,qnt + 1 ):
    idade = int(input(f"Qual a idade da {i} pessoa? "))
    total += idade
if (total / qnt) <= 25:
    print(f'A média da idade da turma é {total / qnt}, ou seja, a turma é jovem')
elif (total / qnt) > 60:
    print(f'A média da idade da turma é {total / qnt}, ou seja, a turma é idosa')
else:
    print(f'A média da idade da turma é {total / qnt}, ou seja, a turma é adulta')