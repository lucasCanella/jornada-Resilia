'''
* Altere os valores do dicionário usando os métodos de alteração;

* Exclua três valores usando os comandos del, pop, popitem;

* Esvazie todo o dicionário e exiba em tela o resultado final;

'''

dicionario = { 

"Algoritmo": "conjunto de passos para realizar certa tarefa.",
"Backup"   : "cópia de arquivos em um outro dispositivo com objetivo de guardar informações.",
"Big Data" : "armazenamento de grande quantidade de dados.",
"SQL"      : "linguagem de banco de dados relacional.",
"Paradigma": "modelo de estrutura utilizado pela linguagem de programação."

}

print('')
print('Dicionário inicial:')
print(dicionario)

dicionario["Algoritmo"] = "sequência de instruções ou comandos (VALOR ALTERADO)"


dicionario.update({'Python':'Linguagem de programação'})

print('')
print('Valor 1 alterado e valor adicionado:')
print(dicionario)

dicionario.popitem()


dicionario.pop('Big Data')


del dicionario['Backup']

print('')
print('3 valores removidos:')
print(dicionario)

print('')
print('Dicionário vazio:')
dicionario.clear()
print(dicionario)