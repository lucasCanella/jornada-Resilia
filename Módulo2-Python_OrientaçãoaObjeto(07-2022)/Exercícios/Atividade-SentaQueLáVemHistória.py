'''
Utilizando herança:

* Crie uma classe livro (atributos Titulo e isbn);

* Crie uma classe Ebook (atributo Link para Download);

* Fazer com que a classe Ebook herde a Classe Livro;

* Demonstrar o funcionamento da herança;

'''

class Livro():
    def __init__(self, titulo, isbn):
        self.setTitulo(titulo)
        self.setISBN(isbn)

    def setTitulo(self, titulo):
        self.titulo = titulo 

    def getTitulo(self):
        return self.titulo

    def setISBN(self, isbn):
        self.isbn = isbn 

    def getISBN(self):
        return self.isbn      

class Ebook(Livro):
    def __init__(self, titulo, isbn, link):
        Livro.__init__(self, titulo, isbn)
        self.setLink(link)

    def setLink(self, link):
        self.link = link

    def getLink(self):
        return self.link    


livro1 = Livro("Storytelling with data", "978-3-16-148410-0")

ebook1 = Ebook(titulo="Storytelling with data - EBOOK", isbn="978-3-16-148410-0", link="www.linkteste")

print(f"Livro = {livro1.getTitulo()}\nISBN = {livro1.getISBN()}")
print(f"Ebook = {ebook1.getTitulo()}\nISBN = {ebook1.getISBN()}")

print(f"Ebook link = {ebook1.getLink()}")

try:
    print(f"Ebook link = {livro1.getLink()}")
except:
    print("A classe mãe não herda da classe filha!")    