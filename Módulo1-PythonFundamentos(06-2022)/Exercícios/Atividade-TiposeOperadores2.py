'''
Escreva um algoritmo que declare um valor em metros em uma variável e converta o valor para centímetros;
'''

metros = float(input('Qual o valor em metros?'))
cm = metros * 100
print(f'{metros:.0f} metros são {cm:.0f} centímetros')