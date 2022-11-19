'''
Crie um algoritmo que deve:

* Receber um número positivo.

* Retornar uma sequencia de números, em ordem crescente, na qual exiba em tela
apenas os números múltiplos de 3 até aquele número.

'''

numero = int(input('Digite um número: '))
for i in range (0, numero +1, 1):
    if i % 3 == 0:
        print(i)