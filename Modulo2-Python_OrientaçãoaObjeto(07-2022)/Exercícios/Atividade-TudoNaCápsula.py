'''
Utilizando encapsulamento:

* Criar três classes que representem as entidades Casa, Fatura e Pessoa;

* Criar uma classe Pessoa com os atributos nome e CPF como privados;

* Criar os métodos para acessar e alterar o valor desses atributos com o intuito de reproduzir o conceito de encapsulamento;

'''
# Reutilizando código do último exercício

class Casa():
    def __init__(self, endereco):
        self.endereco = endereco

    def setLocatario(self, locatario):
        self.locatario = locatario   

    def getLocatario(self):
        print(f"Nome do locatário: {self.locatario.getNome()}")


class Pessoa():
    def __init__(self, nome, idade):
        self.setNome(nome)
        self.setIdade(idade)
        self.__CPF = ''
        self.contas = []

    def setCPF(self, cpf):
        self.__CPF = cpf

    def getCPF(self):
        return self.__CPF

    def setNome(self, nome):
        self.__nome = nome   

    def getNome(self):
        return self.__nome

    def setIdade(self, idade):
        self.idade = idade    

    def getIdade(self):
        return self.idade
    
    def inserirContas(self, nome_conta, preco):
        self.contas.append(Fatura(nome_conta, preco))

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
 
Pessoa1 = Pessoa("Lucas", 21)

casa1 = Casa("Avenida 3 rua 434")

casa1.setLocatario(Pessoa1)
casa1.getLocatario()

Pessoa1.setNome("Lucas Canella")

print(Pessoa1.getNome())

Pessoa1.setCPF("12345678910")
print(Pessoa1.getCPF())

