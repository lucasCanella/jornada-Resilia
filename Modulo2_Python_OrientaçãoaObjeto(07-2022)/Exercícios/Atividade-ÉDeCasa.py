'''
Utilizando agregação e composição:

* Crie três classes que representem as entidades Casa, Fatura e Pessoa;

* Com base nelas, aplique os conceitos de agregação, e composição;

* Dica: As pessoas que moram na casa pagam faturas

'''

class Casa():
    def __init__(self, endereco):
        self.endereco = endereco

    def setLocatario(self, locatario):
        self.locatario = locatario   

    def getLocatario(self):
        print(f"Nome do locatário: {self.locatario.nome}")


class Pessoa():
    def __init__(self, nome, idade):
        self.setNome(nome)
        self.setIdade(idade)
        self.contas = []

    def setNome(self, nome):
        self.nome = nome   

    def setIdade(self, idade):
        self.idade = idade    
    
    def inserirContas(self, nome_conta, preco):
        self.contas.append(Fatura(nome_conta, preco)) # Composição

    def lista_contas(self):
        for conta in self.contas:
            print(f"{conta.nome_conta} - {conta.preco}")

    def soma_contas(self):
        soma = 0
        for conta in self.contas:        
            soma += conta.preco
        print("Soma de contas:", soma)    


class Fatura():
    def __init__(self, nome_conta, preco):
        self.setnome_conta(nome_conta)
        self.setPreco(preco)

    def setnome_conta(self, nome_conta):
        self.nome_conta = nome_conta

    def setPreco(self, preco):
        self.preco = preco    
 
pessoa1 = Pessoa("Lucas", 21)

casa1 = Casa("Avenida 3 Número 434")
casa1.setLocatario(pessoa1)   # Agregação

casa1.getLocatario()

pessoa1.inserirContas("Luz", 300)
pessoa1.inserirContas("Carro", 600)
pessoa1.inserirContas("Casa", 1000)

pessoa1.lista_contas()
pessoa1.soma_contas()
