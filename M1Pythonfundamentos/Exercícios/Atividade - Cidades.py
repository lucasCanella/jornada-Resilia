'''
Escreva uma função que aceite o nome de uma cidade e seu país.
A função deve exibir uma frase simples, como "Brasília está localizada no país Brasil."
Forneça um valor default ao parâmetro que representa o país. 
Chame sua função para três cidades diferentes em que pelo menos uma delas não esteja no país default.

'''

def cidades(cidade, pais = 'Brasil'):
    print(f'{cidade} está localizada no país: {pais}')


cidades('Rio de Janeiro')
cidades('São Paulo')
cidades(pais = 'Inglaterra', cidade = 'Londres')
