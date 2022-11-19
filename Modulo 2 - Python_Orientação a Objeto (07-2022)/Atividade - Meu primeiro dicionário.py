'''

* Pense em 5 palavras relacionadas a programação. 
Use essas palavras como chaves em seu glossário e
armazene seus significados como valores;

* Leia do usuário palavras a seres buscadas no seu glossário e 
exiba em tela seu significado.

'''


dicionario = { 

"Algoritmo": "conjunto de passos para realizar certa tarefa.",
"Backup"   : "cópia de arquivos em um outro dispositivo com objetivo de guardar informações.",
"Big Data" : "armazenamento de grande quantidade de dados.",
"SQL"      : "linguagem de banco de dados relacional.",
"Paradigma": "modelo de estrutura utilizado pela linguagem de programação."

}

while True:
    chave = input("Qual palavra deseja buscar?")
    if chave in dicionario:
        print(f'{chave} : {dicionario[chave]}')
    else:
        print("Essa palavra não está no dicionário.")    