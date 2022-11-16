'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar:

* M (matutino) ou
* V (Vespertino) ou
* N (Noturno)

Imprima a mensagem "Bom Dia!", "Boa Tarde!", ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

'''

turno = input('Que turno vc estuda?\n[M] matutino\n[V] vespertino\n[N] noturno\n')
if turno == 'M' or turno == 'm':
    print('Bom dia!')
elif turno == 'V' or turno == 'v':
    print('Boa tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa noite!')
else:
    print('Turno inválido! Escreva [M], [V] ou [N]')