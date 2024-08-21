'''
Reajuste extra (opcional): 

Faça um Programa que leia três números e mostre-os em ordem decescente.
'''

valor1 = int(input('Qual o primeiro valor? '))
valor2 = int(input('Qual o segundo valor? '))
valor3 = int(input('Qual o terceiro valor? '))


if valor1>valor2>valor3:
    print(f'O menor valor é {valor3}, seguido de {valor2} e {valor1}')
elif valor1>valor3>valor2:
    print(f'O menor valor é {valor2}, seguido de {valor3} e {valor1}')
elif valor2>valor1>valor3:
    print(f'O menor valor é {valor3}, seguido de {valor1} e {valor2}')
elif valor2>valor3>valor1:
    print(f'O menor valor é {valor1}, seguido de {valor3} e {valor2}')
elif valor3>valor1>valor2:
    print(f'O menor valor é {valor2}, seguido de {valor1} e {valor3}')
elif valor3>valor2>valor1:
    print(f'O menor valor é {valor1}, seguido de {valor2} e {valor3}')
elif valor1==valor2>valor3:
    print(f'{valor1} e {valor2} são valores iguais e é maior que o {valor3}')
elif valor1==valor2<valor3:
    print(f'{valor1} e {valor2} são iguais e menor que {valor3}')
elif valor1==valor3>valor2:
    print(f'{valor1} e {valor3} são valores iguais e é maior que {valor2}')
elif valor1==valor3<valor2:
    print(f'{valor1} e {valor3} são iguais e é menor que {valor2}')
elif valor2==valor3>valor1:
    print(f'{valor2}e {valor3} são iguais e maior que {valor1}')
elif valor2==valor3<valor1:
    print(f'{valor2} e {valor3} são iguais e menor que {valor1}')
else:
    print(f'Os 3 valores são iguais')
