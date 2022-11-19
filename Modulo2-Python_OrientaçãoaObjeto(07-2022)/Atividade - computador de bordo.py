'''
Utilizando Programação Orientada a Objeto (POO):

Desenvolva uma página que "emula" um computador de bordo de automovel. Para isso, seu algoritmo deve:

-> Possuir um método que represente um carro com as característica: cor, capacidade 
do tanque, quantidade de combustível no tanque, consumo médio (Km/Litro);

-> O carro deve possuir métodos que:

* Forneçam a previsão de quantos KM espera-se rodar com a quantidade de
 combustível e o consumo médio;

* Ande uma determinada quantidade em KM (argumento) e diminua a quantidade de 
gasolina no tanque a partir de quantidade de km rodados e a média de consumo;

* Getters e Setters para: cor, capacidade do tanque e consumo médio; 

* Construtor com modelo e cor; 

'''

class Computador():
    cor = ''
    modelo = '' 
    capacidade_tanque = 0
    qnt_combustivel = 0.0
    consumo_medio = 0.0

    def __init__(self, modelo, cor):
         self.setmodelo(modelo)
         self.setcor(cor)

    def getmodelo(self):
        return self.modelo

    def setmodelo(self, modelo):
        self.modelo = modelo

    def getcor(self):
        return self.cor

    def setcor(self, cor):
        self.cor = cor    
    
    def getcapacidade(self):
        return self.capacidade_tanque

    def setcapacidade(self,capacidade):
        self.capacidade_tanque = capacidade

    def getconsumo(self):
        return self.consumo_medio

    def setconsumo(self, consumo):
        self.consumo_medio = consumo  

    def setcombustivel(self, combustivel):
        self.qnt_combustivel = combustivel

    def getcombustivel(self):
        return self.qnt_combustivel           
    
    def previsao(self):
        return f"Com consumo médio de {self.consumo_medio} km/L, o carro pode andar mais {self.qnt_combustivel * self.consumo_medio} KM ({self.qnt_combustivel} litros restantes)"

    def andar(self, km):
            if km  > (self.qnt_combustivel * self.consumo_medio): 
                print(f"O carro andou {self.qnt_combustivel * self.consumo_medio} KM e ficou sem combustível!")
                self.qnt_combustivel = 0
            else:
                self.qnt_combustivel = self.qnt_combustivel - (km/self.consumo_medio)
                print(f"O carro andou {km} km, gastando um total de {km/self.consumo_medio} gasolina, o tanque que antes estava em {self.qnt_combustivel + (km/self.consumo_medio)} Litros agora está com {self.qnt_combustivel} Litros restantes")

    def abastecer(self, gasolina):
        self.qnt_combustivel += gasolina
        if self.qnt_combustivel > 55:
            self.qnt_combustivel = 55
            print(f'A capacidade máxima é {self.capacidade_tanque}, como não é possível colocar {gasolina} litros, o tanque foi cheio até a capacidade máxima.')
        else:
            print(f'O tanque foi abastecido com {gasolina} Litros!')    
            
carro1 = Computador("preto", "civic")

carro1.setcapacidade(55)
carro1.setconsumo(10)
carro1.setcombustivel(20)

while True:
    entrada = input("O que deseja fazer? ")
    if entrada == "previsao":
        print(carro1.previsao())
    elif entrada == "andar":
        entrada2 = float(input("quantos km deseja andar? "))
        carro1.andar(entrada2)
    elif entrada == "abastecer":
        entrada3 = float(input("quantos litros deseja abastecer? "))
        carro1.abastecer(entrada3)
    elif entrada == "sair":
        break
    else:
        print("O carro não realiza essa função.")    