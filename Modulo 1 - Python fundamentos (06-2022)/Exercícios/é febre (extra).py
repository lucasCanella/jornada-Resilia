'''
É febre? extra (opcional):

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

'''

contador = 0
num = int(input("Digite um número para saber se ele é primo:"))

for i in range(1, num + 1, 1):
    if num % i == 0:
        contador+=1
if contador == 2:
    print(f"{num} é um número primo.")        
else:
    print(f"{num} não é um número primo.")