'''
* Escrever um algoritmo que lê as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação.
Calcular a média de aproveitamento, usando a fórmula:

* MA = (Nota1 + Nota2 x 2 + nota3 x 3 + ME)/7 

Atribuição de conceitos:
> 9       - A
7,5 e < 9 - B
6 e < 7,5 - C
4 e < 6   - D
< 4       - E 

Ao fim informar:

* O conceito do aluno
* Se ele foi aprovado (A, B, C ) ou reprovado (D e E)
'''

nota_1 = float(input('Qual foi a nota 1: '))
nota_2 = float(input('Qual foi a nota 2: '))
nota_3 = float(input('Qual foi a nota 3: '))
me     = float(input('Qual foi a média dos exercícios: '))
conceito = ''

def ma(nota_1, nota_2, nota_3, me):
    return (nota_1 + nota_2* 2 + nota_3 * 3 + me)/7

resultado = ma(nota_1, nota_2, nota_3, me)

if resultado >= 9 and resultado <= 10:
    conceito = 'A'
elif resultado >= 7.5 and resultado < 9:
    conceito = 'B'
elif resultado >= 6 and resultado < 7.5:
    conceito = 'C'
elif resultado >= 4 and resultado < 6:
    conceito = 'D'
elif resultado >= 0 and resultado < 4: 
    conceito = 'E'
else:
    print('Ocorreu um erro, por favor, realize o processo novamente!')

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print(f'Parabéns! Você passou com media {resultado:.2}, Conceito: {conceito}')
elif conceito == 'D' or conceito == 'E':
    print(f'Estude mais! Você foi reprovado! Sua media foi {resultado:.2}, Conceito: {conceito}')
