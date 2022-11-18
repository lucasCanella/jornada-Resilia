'''
Implemente as funções abaixo:

-> Uma função que acrescenta uma quantidade X de elementos a fila;
-> Uma função que verifica a quantidade de elementos na fila;
-> Uma função que verifica se a fila está vazia ou não;

'''

def adicionarNaFila(fila, incremento):
    for x in range(incremento):
        elemento = input("Qual o próximo elemento?")
        fila.append(elemento)

def qtd_Fila(fila):
    return f"A fila possui {len(fila)} elementos."


def Fila_Vazia(fila):
    if len(fila) == 0:
        return "A fila está vazia."
    else:
        return "A fila não está vazia."    

def removerDaFila(fila):
    del fila[0]

fila = []


print(qtd_Fila(fila))

print(Fila_Vazia(fila))

adicionarNaFila(fila, 3)

print(fila)

removerDaFila(fila)

print(fila)

print(qtd_Fila(fila))

print(Fila_Vazia(fila))

