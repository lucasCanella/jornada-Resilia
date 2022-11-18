'''
* Crie uma tupla a partir de uma lista de nomes e exiba em tela uma mensagem de saudações para cada uma delas;

* Tente alterar um ou mais itens das tuplas e demonstre a imutabilidade das tuplas;

* Experimente alguns métodos aprendidos em listas aplicados a tuplas; 

'''
lista = ['Lucas','João','Bárbara', 'Ives', 'Carol']

tupla = tuple(lista)

for pessoa in tupla:
    print(f'Olá, {pessoa}!')


# Tentando aplicar alguns métodos na tupla:

try:
    tupla.append('Maria')
    del tupla[0]
    tupla.pop()
    tupla.remove("Lucas")
except:
    print("A tupla é imutável!")    

print(tupla)

# Aplicando os mesmos métodos na lista:

print("A lista é mutável!")

lista.append('Maria')
del lista[0]
lista.pop()
lista.remove("Ives")


print(lista)     
