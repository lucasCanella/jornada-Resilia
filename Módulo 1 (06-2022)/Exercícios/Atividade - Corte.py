'''
Escreva um loop que inicia no último caractere da string e caminha para o primeiro caractere,
imprimindo cada letra em uma linha separada.

'''


frase = input('Digite uma frase:')
for i in range(len(frase)-1, -1, -1):
    print(frase[i])
