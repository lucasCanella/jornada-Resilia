'''
Requisitos para aplicação:

* Vamos criar as classes para Categorias e Eventos;

* As categorias tem título e uma breve descrição;

* Eventos devem ter título, data e categoria;

* Ao criar um evento, uma lista com as possíveis categorias deve aparecer para ajudar o usuário a saber quais opções ele tem;

* Cada evento vai ser inserido em um arquivo de texto que vai ficar com nosso log;

'''
from os import system
from time import sleep
class Categoria:
    def __init__(self, titulo, descricao):
        self.set_titulo(titulo)
        self.set_descricao(descricao)

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_descricao(self):
        return self.descricao


class Evento:
    def __init__(self, titulo, data, categoria):
        self.set_titulo(titulo)
        self.set_data(data)
        self.set_categoria(categoria)
        print()

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo    

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data       

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_categoria(self):
        return self.categoria

jornadacorporativa = Categoria("Jornada Corporativa", "Encontro com pessoas da área de tecnologia para tirada de dúvidas e network")
projeto = Categoria("Projeto", "Apresentação de projeto de módulo")
ser = Categoria("SER", "Semana de empregabilidade Resilia")
jogo = Categoria("Campeonato de jogos", "Campeonato de jogos da comunidade")
mentoria = Categoria("Mentoria", "Mentoria Tech para revisão e tirada de dúvidas") 

lista_categorias_objetos = [jornadacorporativa,projeto,ser,jogo,mentoria]

lista_categorias = [i.get_titulo() for i in lista_categorias_objetos]
lista_descricao = [i.get_descricao() for i in lista_categorias_objetos]
lista_eventos = []


while True:
    system('cls')
    Entrada = input("Deseja criar um novo evento? [1] Sim [Outra tecla] Não\n")
    if Entrada != '1':
        break
    else:
        print('')
        for i in range(0, len(lista_categorias)):
            print(f"{i + 1} - {lista_categorias[i]} : {lista_descricao[i]}")
        entrada_categoria = input("Selecione o número da categoria do evento que você deseja criar:")
        if entrada_categoria == '1':
            categoria = jornadacorporativa
        elif entrada_categoria == '2':
            categoria = projeto
        elif entrada_categoria == '3':
            categoria = ser
        elif entrada_categoria == '4':
            categoria = jogo
        elif entrada_categoria == '5':
            categoria = mentoria         
        else:
            print("Categoria inválida!")
            sleep(2)
            continue
        titulo = input("Qual o título do evento?")
        data = input("Qual a data do evento? ")
        evento = Evento(titulo, data, categoria)
        lista_eventos.append(evento)


arquivo = open('log_eventos.txt', 'a', encoding='utf-8')
for evento in lista_eventos:
    arquivo.write(f'{evento.titulo}, {evento.data}, {evento.categoria.titulo}\n')
arquivo.close() 