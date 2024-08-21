'''
Faça uma função que retorne o reverso de um número inteiro informado.

Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.
 
'''


# Exercício 1

def numero_reverso(num):
    return str(num[::-1])

numero = input('Digite um número inteiro:')

print(numero_reverso(numero))

# Exercício 2

def contar_letra(letra, frase):
    return frase.count(letra)

frase = input('Digite a frase:')
letra = input('Qual letra deve ser contada? ')

print(contar_letra(letra, frase))