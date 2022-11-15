'''
Escreva um algoritmo que armazene a sua idade em uma variável A e a de algúem do grupo em uma variável B.
Em seguida, troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa.
Ao final, escreva os valores armazenados

* Faça o mesmo com seus nomes em variáveis distintas
'''

idade_A = 21
idade_B = 22
idade_A , idade_B = idade_B, idade_A
nome_A = 'Lucas'
nome_B = 'Luiza'
nome_A , nome_B = nome_B, nome_A
print(f'Idade A era 21 e agora é: {idade_A}\nidade B era 52 e agora é: {idade_B}')
print(f'Nome A era Lucas e agora é: {nome_A} \nnome B era Luiza e agora é: {nome_B}')