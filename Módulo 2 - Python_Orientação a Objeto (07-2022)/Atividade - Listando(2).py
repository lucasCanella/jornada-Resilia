'''
Elabore um algoritmo que cria duas listas de dez posições e faça a 
multiplicação dos elementos de mesmo índice, colocando o resultado em uma
terceira lista, que deve ser mostrada como saída
 
 '''

lista1 = []
lista2 = []
lista3 = [] 

for num in range(1,11,1):
    lista1.append(num)

for num in range(10,0,-1):    
    lista2.append(num)

for num in range(0,10):
    lista3.append(lista1[num]*lista2[num])


print("Lista 1: ", lista1)    
print("lista 2: ", lista2)    
print("lista 3: ", lista3)    