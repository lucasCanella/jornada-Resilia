'''
* Faça uma lista de suas pizzas favoritas;
* Faça uma cópia chamanda friend_pizzas;

* Adicione uma nova pizza a lista original;
* Adicione uma pizza diferente a lista friend_pizzas;
* Prove que as duas listas são diferentes:
    -> Exiba a mensagem "Minhas pizzas favoritas são:"; em seguida, exiba a primeira lista;
    -> Exiba a mensagem "As pizzas favoritas do meu amigo são:"; em seguida, exiba a segunda lista;

Certifique-se de que cada pizza nova esteja armazenada na lista apropriada;  
   
'''


pizzas = ["Calabresa", "Quatro-queijos", "Margherita"]
friend_pizzas = pizzas.copy()

pizzas.append("Portuguesa")
friend_pizzas.append("pepperoni")

print("As minhas pizzas favoritas são:", pizzas)
print("As pizzas favoritas do meu amigo são:", friend_pizzas)