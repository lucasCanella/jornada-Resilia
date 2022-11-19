'''
* Utilize o seguinte código em Python que guarda uma string:
    * dado = 'X-DSPAM-Confidence:0.8475'

* Extraia a porção da string depois do sinal de dois pontos, converta a string extraída em um número e multiplique por 100, exiba o resultado em tela. 
'''

dado = 'X-DSPAM-Confidence:0.8475'
numero_posicao = (dado.find(':') + 1)
numero = float((dado[numero_posicao:]))
print(numero * 100)