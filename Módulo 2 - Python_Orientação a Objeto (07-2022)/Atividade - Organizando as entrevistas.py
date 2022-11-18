'''
Utilizando Programação Orientada a Objeto (POO):

Desenvolve uma classe "Entrevistado" com os seguintes requisitos: 

* Tenha os atributos: idade, cidade, estado, salário atual e escolaridade;

* Tenha um método "Imprimir dados" que devolve as informação do entrevistado em uma
string com os atributos separados por vírgula (Ex: 20, Rio de Janeiro, RJ, 1000, Superior);

'''


class Entrevistado():
    nome = ''
    idade = 0
    cidade = ''
    estado = ''
    salario = ''
    escolaridade = ''

    def __init__(self, nome, idade, cidade, estado, salario, escolaridade):
        self.setnome(nome)
        self.setidade(idade)
        self.setcidade(cidade)
        self.setestado(estado)
        self.setsalario(salario)
        self.setescolaridade(escolaridade)

    def setnome(self, nome):
       self.nome = nome
       
    def setidade(self, idade):
       self.idade = idade
       
    def setcidade(self, cidade):
       self.cidade = cidade
       
    def setestado(self, estado):
       self.estado = estado
       
    def setsalario(self, salario):
       self.salario = salario
       
    def setescolaridade(self, escolaridade):
       self.escolaridade = escolaridade

    def imprimir_dados(self):
        print(f"{self.nome},{self.idade},{self.cidade},{self.estado},{self.salario},{self.escolaridade}")   


entrevistado1 = Entrevistado("Lucas", 21, "Rio de Janeiro", "RJ", "2500", "Superior Incompleto")

entrevistado1.imprimir_dados()