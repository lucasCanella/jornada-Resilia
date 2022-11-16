'''
Faça um script em python que solicite um número inteiro positivo ao usuário, n.
Então, exiba todos os termos da seqûencia Fibonacci até o n-ésimo termo. 
'''
# Fibonacci:(0,1,1,2,3,5,8,12,21,34,55,...)

numero = int(input('Digite um número para saber a seqûencia Fibonacci até os dois número mais próximos: '))

a1 = 0
a2 = 1
a3 = a1 + a2
fibonacci = [0,1]

# a3 = a2 + a1 = 1 + 1 = 2
# a4 = a3 + a2 = 2 + 1 = 3
# a5 = a4 + a3 = 3 + 2 = 5
# a6 = a5 + a4 = 5 + 3 = 8
# a7 = a6 + a5 = 8 + 5 = 13
# a8 = a7 + a6 = 13 + 8 = 21
# a9 = a8 + a7 = 21 + 13 = 34


while a3 < numero:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    fibonacci.append(a3)
print(fibonacci)
if a3 > numero:
    print(f'{numero} está entre dois números fibonacci: {fibonacci[-2]} e {a3}. \nRespectivamente, posição: {fibonacci.index(fibonacci[-2])} e posição: {fibonacci.index(fibonacci[-1])}')
