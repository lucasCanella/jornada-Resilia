'''
Elabore um algoritmo que leia uma lista de quinze números, remova os 
elementos ímpares, ordene e exiba em tela o menor e o maior valor

'''


lista = [13,14,15,4,9,10,1,5,6,7,8,2,3,11,12]

for num in lista[:]:
    if num % 2 == 1:
        lista.remove(num)

lista.sort()

print(lista)
print("Menor número:", lista[0])
print("Maior número:", lista[-1])