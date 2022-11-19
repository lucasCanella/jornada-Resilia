'''
* Implemente as funções abaixo:

-> Uma função que retire uma quantidade X de elementos da pilha;
-> Uma função que verifica a quantidade de elementos na pilha;
-> Uma função que verifica se a pilha está vazia ou não;

'''

def removerDaPilha(pilha, incremento):
    try:
        for x in range(incremento):
            del pilha[-1]
    except:
        return print("A pilha já está vazia")

def qtd_Pilha(pilha):
    return f"A pilha possui {len(pilha)} elementos."

def Pilha_Vazia(pilha):
    if len(pilha) == 0:
        return "A pilha está vazia."
    return "A pilha não está vazia."    

def adicionarNaPilha(pilha, incremento):
    for x in range(incremento):
        elemento = input("Digite o elemento que deseja inserir na pilha: ")
        pilha.append(elemento) 

pilha = []   


adicionarNaPilha(pilha, 5)


for x in range(6):
    print(pilha)

    print(qtd_Pilha(pilha))

    (Pilha_Vazia(pilha))

    removerDaPilha(pilha, 1)

