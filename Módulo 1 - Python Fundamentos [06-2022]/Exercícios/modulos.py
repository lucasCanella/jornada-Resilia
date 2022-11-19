'''
Módulos para o exercício modularize-se:
'''

def FahrenheittoC(F):
    C = (F - 32) * (5/9)
    return f'{F} graus Fahrenheit são {C} graus Celsius'

def CelsiustoF(C):
    F = C*(9/5) + 32
    return f'{C} graus Celsius são {F} graus Fahrenheit'
