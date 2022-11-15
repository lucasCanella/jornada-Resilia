'''Escreva um algoritmo que declare o salário mensal atual de um funcionário em uma variável e o percentual de reajuste em outra. 
Calcule e exiba o valor do novo salário'''

salario = float(input('Qual o salário mensal do funcionário?'))
porcentagem = 1.15
reajuste = salario*porcentagem
print(f'O salário do funcionário era {salario} e foi reajustado para {reajuste:.1f}')
