'''
Crie um algoritmo que deve:

* Receber um número positivo
* Exiba em tela uma sequência de números, em ordem decrescente, que vai daquele número até zero
'''

numero = int(input('Digite um número positivo: '))
if numero < 0:
    print('Valor inválido, o valor deve ser positivo.')
else:
    for i in range(numero, -1, -1):
        print(i, end = ' ')
