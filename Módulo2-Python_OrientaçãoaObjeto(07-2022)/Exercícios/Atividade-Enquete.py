'''

* Crie uma lista de pessoas que devem participar de uma enquete sobre sua linguagem favorita;

* Monte um dicionário com as pessoas que responderam ou não a essa enquete;

* Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem
respondido a enquete, mostre uma mensagem agradecendo-lhes por responder. 
Se ainda não participaram da enquete, apresente uma mensagem convidando-as a responder.

'''

pessoas_lista = ["Lucas", "João", "Ally", "Carol", "Lee", "Luiza"]

pessoas = {
    'Lucas'   : 'N',
    'João' : 'Python',
    'Ally'    : 'N',
    'Carol'   : 'PHP',
    'Lee'     : 'N',
    'Luiza'   : 'html'}

for pessoa in pessoas_lista:

    if pessoas[pessoa] == 'N':
        resposta = input(f'Olá! {pessoa}, você ainda não respondeu a enquete, gostaria de responder?\n[1] Sim\n[2] Não \n')

        if resposta == '1':
            linguagem = input('Qual a sua linguagem de programação preferida?')
            pessoas[pessoa] = linguagem
            print(f"Muito obrigado, {pessoa}!")

        elif resposta == '2':
            print(f'Tudo bem, {pessoa}!')
    else:
        print(f'{pessoa}, Você já respondeu a enquete, {pessoas[pessoa]} é uma ótima linguagem!')

print(pessoas)
