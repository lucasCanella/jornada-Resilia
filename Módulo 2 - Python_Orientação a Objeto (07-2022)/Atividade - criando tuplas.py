'''
Elabore um algoritmo que cria duas tuplas de dez posições e faça a
multiplicação dos elementos de mesmo índice, colocando o resultado em uma
terceira tupla, que deve ser mostrada como saída.

'''

tupla1 = tuple(i for i in range(1,11))
tupla2 = tuple(i for i in range(10,0,-1))

tupla3 = tuple(tupla1[i] * tupla2[i] for i in range(10))

print(tupla1)

print(tupla2)

print(tupla3)
