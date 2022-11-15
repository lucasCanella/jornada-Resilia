'''
Olha o loop 1 extra (opcional): 

Faça um programa que peça um número, entre zero e dez.
Mostre uma mensagem ("Número aceito") em caso de valor válido. 
Caso o valor seja inválido, informe ao usuário e continue pedindo até que um valor válido seja inserido.
'''

while True:
    numero = int(input('Digite um número de 0 a 10: '))
    if -1 < numero <= 10:
        print('Numero aceito!')
        break
    else:
        print('Numero inválido, tente novamente!')
