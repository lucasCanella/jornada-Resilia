'''
Olha o loop 2 extra (opcional):

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 

'''

fatorial = 1
entrada = int(input('Digite um número para saber seu fatorial: '))
calculo = entrada
for i in range(entrada, 0, -1):
    fatorial = fatorial * i
    while calculo != 0:
        if calculo == entrada:
            print(f'{entrada}! = {entrada} x', end = ' ')
        elif calculo == 1:
            print(f'{calculo} =', end = ' ')
        else:
            print(calculo, end = ' x ')
        calculo = calculo - 1
print(f'{fatorial}')