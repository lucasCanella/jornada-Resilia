/* Antes de verificar as consultas, é necessário rodar "Pizzaria-ScriptDeCriaçãoDeTabelas.sql";
obs: no caso de dúvidas, consulte a modelagem do banco de dados
*/
-- QUERIES (consultas):

-- 1) Selecionar todos os clientes da pizzaria:

Select * from tb_cliente;

-- 2) Selecionar todas as pizzas da pizzaria:

Select * from tb_pizza;

-- 3) Selecionar todas as pizzas da categoria Zero Lactose:

Select * from tb_pizza where categoria = 'Zero Lactose';

-- 4) Selecionar as pizzas que não são da categoria Zero Lactose:

Select * from tb_pizza where categoria != 'Zero Lactose';

-- 5) Selecionar todos os pedidos feitos no dia 21/04/2021:

Select * from tb_pedido where data_pedido between '2021-04-21 00:00:00' and '2021-04-21 23:59:59';

-- 6) Selecionar todos os id dos clientes que realizaram pedidos acima de 100 reais:

select id_cliente, preco from tb_pedido where preco > 100;

-- 7) Selecionar todos os sabores de pizzas pedidas por Enzo Gabriel no dia 22/04/2021:

select tb_pedido.id_pedido, tb_cliente.nome, tb_pizza.nome as nome_pizza, tb_pedido.data_pedido from tb_pedido 
inner join tb_cliente on tb_cliente.id_cliente = tb_pedido.id_cliente
inner join tb_pedido_pizza on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
inner join tb_pizza on tb_pedido_pizza.id_pizza = tb_pizza.id_pizza
where tb_pedido.id_cliente = 11 and tb_pedido.data_pedido between '2021-04-22 00:00:00' and '2021-04-22 23:59:59';

-- 8) Selecionar todos os clientes que moram na Rua das Flores:

select * from tb_cliente where endereco ilike 'rua das flores%';

-- 9) Selecionar os emails de todos os clientes que possuem Maria no nome:

select email from tb_cliente where nome ilike '%Maria%';

-- 10) Selecionar todas as pizzas que possuem bacon:

select * from tb_pizza where nome ilike '%bacon%';

-- 11) selecionar as pizzas que possuem a letra 'a' como segundo caractere no seu nome

select * from tb_pizza where nome ilike '_a%';

-- 12) Selecionar o nome dos clientes que fizeram pedidos com valores de 45, 95 e 120:

select tb_cliente.nome, tb_pedido.preco from tb_cliente
inner join tb_pedido on tb_cliente.id_cliente = tb_pedido.id_cliente
where tb_pedido.preco = 45 or tb_pedido.preco = 95 or tb_pedido.preco = 120;

-- 13) Retornar a soma de todos os pedidos realizados:

select sum(preco) as soma_pedidos from tb_pedido;

-- 14) Retornar o valor do pedido mais caro:

select max(preco) as maior_pedido from tb_pedido;

-- 15) Retornar o preço médio das pizzas:

select to_char(avg(preco),'99.99') as media_pizzas from tb_pizza;

-- 16) Selecionar o preço médio por categoria de pizza:

select categoria, to_char(avg(preco), '99.99') as media_categoria from tb_pizza group by categoria;

-- 17) Selecionar o preço total dos pedidos agrupando-os por tipo de entrega:

select tipo_entrega, sum(preco) as preco_total from tb_pedido group by tipo_entrega;

-- 18) Selecionar o número de pedidos que cada cliente realizou na pizzaria em ordem crescente:

select id_cliente, count(id_pedido) as total_pedidos from tb_pedido group by id_cliente order by count(id_pedido);

-- 19) Selecionar os nomes dos clientes que realizaram mais de 2 pedidos:

select tb_cliente.nome, count(id_pedido) as total_pedidos from tb_pedido
inner join tb_cliente on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_cliente.nome having count(id_pedido) > 2 order by count(id_pedido); 

-- 20) Retornar a quantidade de pedidos de cada pizza:

select tb_pizza.id_pizza, tb_pizza.nome , count(id_pedido) as num_pedidos from tb_pedido_pizza
inner join tb_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
group by tb_pizza.id_pizza order by count(id_pedido) desc;

-- 21) Retornar a quantidade de pedidos de cada categoria de pizza:

select tb_pizza.categoria, count(tb_pedido_pizza.id_pedido) as categoria_pedidos from tb_pizza
inner join tb_pedido_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza group by categoria;

-- 22) Retornar a soma dos preços dos pedidos agrupados pelo nome da pizza:

select tb_pizza.nome, sum(tb_pedido.preco) as total_pedidos from tb_pizza 
inner join tb_pedido_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
inner join tb_pedido on tb_pedido_pizza.id_pedido = tb_pedido.id_pedido
group by tb_pizza.nome order by sum(tb_pedido.preco) desc;

-- 23) Retornar a soma dos preços dos pedidos agrupados pelo nome da pizza, filtrando pelas pizzas de categoria "Zero Lactose":

select tb_pizza.nome, sum(tb_pedido.preco) as total_pedidos from tb_pizza 
inner join tb_pedido_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
inner join tb_pedido on tb_pedido_pizza.id_pedido = tb_pedido.id_pedido
group by tb_pizza.nome, tb_pizza.categoria having tb_pizza.categoria ilike 'zero lactose' 
order by sum(tb_pedido.preco) desc;

