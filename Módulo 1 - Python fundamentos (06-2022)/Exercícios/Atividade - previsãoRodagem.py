'''
* Crie uma função para verificar o quanto será possível rodar sem abastecer. Sua função deve:

Receber a quantidade de litros de gasolina no tanque do carro;
Receber a quilometragem média por litro;
Retornar a estimativa de Km que podem ser rodados nas circustâncias fornecidas;
'''


def previsaoRodagem(combustivel, kmL):
    return combustivel * kmL

gasolina = float(input('Quantos litros de gasolina restantes? '))
km_litro = float(input('Quantos Km/L o carro faz? '))

print(f'Poderão ser rodados mais {previsaoRodagem(gasolina, km_litro):.2f} Km.')