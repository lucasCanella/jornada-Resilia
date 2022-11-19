'''
* Leia a entrada com temperatura do usuário até que ele digite 'sair'.

* Exiba na tela: 

"você está com febre. Tome um remédio e repouse" quando a temperatura estiver entre 38 e 39 graus;
"Você está com febre. Tome um remédio e procure um médico." para qualquer temperatura acima disso;
e "Nada de febre" caso contrário

'''

while True:    
    febre = input('Qual a sua temperatura?')
    if febre == 'sair':
        break
    elif 38 <= int(febre) < 39:
        print('você está com febre. Tome um remédio e repouse')
    elif int(febre) >= 39:
        print('Você está com febre. Tome um remédio e procure um médico')
    elif int(febre) < 38:
        print('Nada de febre')

print('FIM')