import modulos as temp

temperatura = int(input('Digite uma temperatura para converte-la: '))
escala = int(input('É Celsius [1] ou Fahrenheit [2]? '))

if escala == 1:
    print(temp.CelsiustoF(temperatura))
elif escala == 2:
    print(temp.FahrenheittoC(temperatura))    
else:
    print('Por favor, selecione uma opção válida')    