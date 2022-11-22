/* Antes de verificar as consultas, é necessário rodar "Pizzaria-ScriptDeCriaçãoDeTabelas";
obs: no caso de dúvidas, consulte a modelagem do banco de dados
*/
-- QUERIES (consultas):

-- 24) Selecionar todos os cliente, os pedidos associados a eles, e verificar os clientes que já realizaram pedidos; 

select tb_cliente.id_cliente, tb_pedido.id_pedido,  
(case 
when tb_pedido.id_pedido is not null then true 
when tb_pedido.id_pedido is null then false 
end) as fez_pedido from tb_pedido 
right join  tb_cliente on tb_pedido.id_cliente = tb_cliente.id_cliente
order by tb_pedido.id_cliente

-- 25) Apresentar o número de pedidos feitos por cada cliente;

select tb_cliente.id_cliente, tb_cliente.nome, count(tb_pedido.id_pedido) from tb_cliente
inner join tb_pedido on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_cliente.id_cliente, tb_cliente.nome order by count(tb_pedido.id_pedido) desc;

-- 26) Apresentar o número de vezes que uma pizza foi pedida;

select tb_pizza.nome, count(id_pedido) from tb_pizza 
left join tb_pedido_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
group by tb_pizza.nome

-- 27) Apresentar qual a pizza favorita (mais pedida) do cliente 1;



-- 28) Apresentar uma lista das pizzas que são menos pedidas;



-- 29) Apresentar o acumulado de valor de pedido por endereço;



-- 30) Selecionar os pedidos e exibir a quantidade de pizzas em cada pedido;



-- 31) Apresentar os clientes e exibir a soma de valor dos pedidos realizados;



-- 32) Retornar os clientes que fizeram pedidos do tipo Delivery no banco da pizzaria (subquery); 



-- 33) Retornar somente as pizzas vendidas do tipo zero lactose (subquery);



-- 34) Criar uma view que retorne a data do ultimo pedido de cada pizza 
--     (deve retornar data, id da pizza, nome da pizza, a categoria e o preço);




