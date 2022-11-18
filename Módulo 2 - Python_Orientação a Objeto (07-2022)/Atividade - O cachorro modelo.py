'''
Utilizando Programação Orientada a Objeto (POO):

Desenvolva uma página que "modela" um cachorro. Para isso, seu algoritmo deve:

* Perguntar o nome e a data de nascimento do cachorro ao ser acessada;

* Disponibilizar um método "latir", que exibe um alerta com o texto "O cachorro latiu";

* Disponibilizar um método "comer", que exibe um alerta com o texto "O cachorro comeu";

* Disponibilizar um método "objeto cachorro", que exibe no console o objeto cachorro;

*
'''

class cachorro():
    def __init__(self, nome, cor, raca, idade):
        self.setnome(nome)
        self.setcor(cor)
        self.setraca(raca)
        self.setidade(idade)

    def setnome(self, nome):
        self.nome = nome
        
    def setcor(self, cor):
        self.cor = cor

    def setraca(self, raca):
        self.raca = raca

    def setidade(self, idade):
        self.idade = idade  

    def latir(self):
        print("O cachorro latiu")

    def comer(self):
        print("O cachorro comeu")  
        
    def exibir_dados(self):
        print(f"O cachorro de nome {self.nome}, é um {self.raca} da cor {self.cor} que tem {self.idade} anos de idade.")



cachorro1 = cachorro("Marley", raca = "York" , idade = 16, cor = "Marrom")

while True:
    entrada = input('Digite a ação que o cachorro deve executar (Digite sair para finalizar): ').lower()
    if entrada == "comer":
        cachorro1.comer()
    elif entrada == "latir":
        cachorro1.latir()
    elif entrada == "sair":
        break
    elif entrada == 'dados':
        cachorro1.exibir_dados()
    else:
        print("O cachorro não faz isso!")