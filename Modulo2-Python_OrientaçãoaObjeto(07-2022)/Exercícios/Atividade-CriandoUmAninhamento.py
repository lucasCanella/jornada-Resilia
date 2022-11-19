'''

* Crie um dicionário de dicionários de cidades em que as chaves são o nome da cidade e o estado a que ela pertence;

* Armazene a população, se há praia, região em que está inserida e o gentílico da cidade;

* Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela;

'''

cidadeRJ = {"População": "6,748 milhões", "Praia": "Sim", "Região":"Sudeste", "Gentílico": "Carioca"}
cidadeSP = {"População": "12,33 milhões", "Praia": "Sim", "Região":"Sudeste", "Gentílico": "paulistano"}
cidadeCWB = {"População": "1,9 milhão", "Praia": "Não", "Região":"Sul", "Gentílico": "curitibano"}
cidadeRCF = {"População": "1,6 milhão", "Praia": "Sim", "Região":"Nordeste", "Gentílico": "recifense"}

Cidades_dicionario = {
    ("Rio de Janeiro", "RJ") : cidadeRJ,
    ("São Paulo", "SP")      : cidadeSP,
    ("Curitiba", "PR")       : cidadeCWB,
    ("Recife", "PE")         : cidadeRCF,
 }

for cidade in Cidades_dicionario:
    print(f"{cidade} - {Cidades_dicionario[cidade]}")