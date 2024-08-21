/* Antes de verificar as consultas, é necessário rodar "Pizzaria-ScriptDeCriaçãoDeTabelas.sql";
obs: no caso de dúvidas, consulte a modelagem do banco de dados
*/
-- QUERIES (consultas):

-- 24) Selecionar todos os cliente, os pedidos associados a eles, e verificar os clientes que já realizaram pedidos; 

select tb_cliente.id_cliente, tb_cliente.nome, tb_pedido.id_pedido,  
(
case 
    when tb_pedido.id_pedido is not null then true 
    when tb_pedido.id_pedido is null then false 
end
) as fez_pedido from tb_pedido 
right join  tb_cliente on tb_pedido.id_cliente = tb_cliente.id_cliente
order by tb_pedido.id_cliente;

-- 25) Apresentar o número de pedidos feitos por cada cliente;

select tb_cliente.id_cliente, tb_cliente.nome, count(tb_pedido.id_pedido) as num_pedidos from tb_cliente
inner join tb_pedido on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_cliente.id_cliente, tb_cliente.nome order by tb_cliente.id_cliente;

-- 26) Apresentar o número de vezes que uma pizza foi pedida;

select tb_pizza.id_pizza, tb_pizza.nome, count(id_pedido) as num_pedidos from tb_pizza 
left join tb_pedido_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
group by tb_pizza.id_pizza,tb_pizza.nome order by count(id_pedido) desc;

-- 27) Apresentar qual a pizza favorita (mais pedida) do cliente 1;

-- Lista de pedidos referentes ao cliente 1
select id_pedido from tb_pedido where id_cliente = 1;

select tb_pizza.nome, tb_pedido_pizza.id_pizza, count(id_pedido) as num_pedidos from tb_pedido_pizza 
inner join tb_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
where id_pedido in (select id_pedido from tb_pedido where id_cliente = 1) 
group by tb_pizza.nome, tb_pedido_pizza.id_pizza order by count(id_pedido) desc;

-- 28) Apresentar uma lista das pizzas que são menos pedidas;

select tb_pizza.nome, tb_pizza.id_pizza, count(id_pedido) from tb_pedido_pizza
right join tb_pizza on tb_pedido_pizza.id_pizza =  tb_pizza.id_pizza
group by tb_pizza.nome, tb_pizza.id_pizza having count(id_pedido) < 5 order by count(id_pedido) asc;

-- 29) Apresentar o acumulado de valor de pedido por endereço;

select tb_cliente.endereco, sum(preco) from tb_cliente 
right join tb_pedido on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_cliente.endereco order by sum(preco) desc;

-- 30) Selecionar os pedidos e exibir a quantidade de pizzas em cada pedido;

select id_pedido, count(id_pizza) as qtd_pizza from tb_pedido_pizza
group by id_pedido order by id_pedido;  

-- 31) Apresentar os clientes e exibir a soma de valor dos pedidos realizados;

select tb_cliente.id_cliente, tb_cliente.nome, sum(preco) as total_pedidos from tb_cliente
left join tb_pedido on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_cliente.id_cliente, tb_cliente.nome order by tb_cliente.id_cliente;

-- 32) Retornar os clientes que fizeram pedidos do tipo 'Retirada no balcão' no banco da pizzaria (subquery);

-- lista com id dos clientes que retiraram no balcão
select id_cliente from tb_pedido where tipo_entrega = 'Retirada no balcão';

select * from tb_cliente where id_cliente in 
(select id_cliente from tb_pedido where tipo_entrega = 'Retirada no balcão')
order by id_cliente;

-- 33) Retornar somente as pizzas vendidas do tipo zero lactose (subquery);

-- Selecionando Pizzas zero lactose
select * from tb_pizza where categoria = 'Zero Lactose';

select tb_pedido_pizza.id_pizza, nome from tb_pedido_pizza
inner join (select * from tb_pizza where categoria = 'Zero Lactose') as pizzas_zero_lactose
on tb_pedido_pizza.id_pizza = pizzas_zero_lactose.id_pizza
group by tb_pedido_pizza.id_pizza, nome;

-- 34) Criar uma view que retorne a data do ultimo pedido de cada pizza 
--     (deve retornar data, id da pizza, nome da pizza, a categoria e o preço);

-- criando a view
create view vw_ultimo_pedido as
    select max(data_pedido) as data_pedido, tb_pizza.id_pizza, tb_pizza.nome, tb_pizza.categoria, tb_pizza.preco from tb_pedido
    inner join tb_pedido_pizza on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
    inner join tb_pizza on tb_pedido_pizza.id_pizza = tb_pizza.id_pizza
    group by tb_pizza.id_pizza, tb_pizza.nome, tb_pizza.categoria, tb_pizza.preco
    order by tb_pizza.id_pizza;

select * from vw_ultimo_pedido;
