'''
Elabore um algoritmo em Python que execute os passos abaixo:

1. Receba 4 números (a, b, c, d)
2. Calcule a expressão (a*c - b*d)
3. Calcule a expressão (a + b + c + d)/4
4. Exiba os resultados na tela
'''

valorA = int(input('Digite o valor A: '))
valorB = int(input('Digite o valor B: '))
valorC = int(input('Digite o valor C: '))
valorD = int(input('Digite o valor D: '))
expressao1 = valorA*valorC - valorB*valorD
expressao2 = (valorA + valorB + valorC + valorD)/4
print(f'A primeira expressão resulta em {expressao1}')
print(f'A segunda expressão resulta em {expressao2}')
