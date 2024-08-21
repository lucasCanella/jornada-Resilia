'''
Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo e salário.
Faça um algoritmo que leia esses dados coletados e informe:

a) A média de salário do grupo;
b) Maior e menor idade do grupo; 
c) Quantidade de homens e mulheres;
d) Quantidade de mulheres com salário até 1000;
 
* Encerre a entrada de dados quando for digitada uma idade negativa
'''

entradas = 0
idade = 1
idade_menor = 10000
idade_maior = 0
salario_media = 0
mulheres = 0
homens = 0
mulheres_salario = 0

while idade > 0:
    entradas = entradas +1
    print(f'PESSOA: {entradas}')
    idade = int(input('Qual a idade? '))
    if idade < 0:
        break
    elif idade > idade_maior:
        idade_maior = idade
    if idade < idade_menor:
        idade_menor = idade
    salario = float(input('Qual o salário?'))
    if salario > 0:
        salario_media += salario
    sexo = input('Qual o seu sexo? [M] ou [F] ')
    if sexo == 'F' or sexo == 'f':
        mulheres = mulheres +1
        if salario <= 1000:
            mulheres_salario += 1    
    elif sexo == 'M' or sexo == 'm':
        homens = homens + 1
print(f'A média de salário é: {salario_media/(entradas-1)}')
print(f'Maior idade: {idade_maior}')
print(f'Menor idade: {idade_menor}')
print(f'Quantidade de mulheres: {mulheres}')
print(f'Quantidade de homens: {homens}')
print(f'{mulheres_salario} mulheres recebem salário inferior ou igual a 1000')