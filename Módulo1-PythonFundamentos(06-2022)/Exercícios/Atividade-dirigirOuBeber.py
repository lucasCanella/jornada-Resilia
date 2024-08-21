'''
* Crie uma função que verifica se a pessoa já pode dirigir e beber, sua função deve:

Receber uma idade
Caso a idade seja maior que 18, retorne "já pode dirigir ou beber"
Caso contrário, retorne "Não pode nem dirigir nem beber"
'''


def dirigirOuBeber(idade):
    if idade >= 18:
        return print(f'Uma pessoa com {idade} anos já pode dirigir ou beber.')
    else:
        return print(f'Uma pessoa com {idade} anos não pode nem digir nem beber.')


idade_usuário = int(input('Qual a sua idade? '))

dirigirOuBeber(idade_usuário)