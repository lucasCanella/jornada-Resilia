'''
Elabore um algoritmo em Python que peça 2 números inteiros e um número decimal.
Faça uma função para calcular cada item e apresente as respostas:

1. O produto do dobro do primeiro com a metade do segundo.
2. A soma do triplo do primeiro com o terceiro.
3. O terceiro elevado ao cubo.

'''

valorI1 = int(input('Digite um número inteiro: '))
valorI2 = int(input('Digite mais um número inteiro: '))
valorf = float(input('Digite um número decimal: '))

def calculo1(valorI1, valorI2):
    return (valorI1*2) * (valorI2/2)

def calculo2(valorI1, valorf):
    return (valorI1*3) + valorf

def calculo3(valorf):
    return (valorf)**3

resultado1 = calculo1(valorI1, valorI2)
resultado2 = calculo2(valorI1, valorf)
resultado3 = calculo3(valorf)
print(f'O primeiro resultado é: {resultado1}')
print(f'O segundo resultado é: {resultado2}')
print(f'O terceiro resultado é: {resultado3}')