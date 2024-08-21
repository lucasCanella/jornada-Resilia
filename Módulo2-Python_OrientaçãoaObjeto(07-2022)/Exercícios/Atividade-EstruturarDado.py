'''
* Reutilize a lista de nomes montada na atividade anterior;
* Crie uma nova lista com mais 3 nomes, concatene com a anterior e verifique se os nomes dos facilitadores estão continos nessas listas;

'''


nomes = ['lucas', 'joao', 'maria']
nomes_facilitadores = ['dayson', 'esli', 'marisa']

nomes_concat = nomes + nomes_facilitadores


while True:
    print('')
    entrada = input("Digite um nome: ").lower()

    if entrada in nomes_concat and entrada in nomes_facilitadores:
        print(entrada, "é um facilitador e está na lista!" )
        print('')

    elif entrada in nomes_concat and entrada not in nomes_facilitadores:
        print(entrada, "não é um facilitador, porém está na lista!" ) 
        print('')

    else:
        print(entrada, "não está na lista!" )
        print('')

    verifica = input("deseja inserir outro nome? \nSim [1] \nNão [outro botão]\n")
    if verifica != "1":
        break