/* Antes de verificar as consultas, é necessário rodar "Pizzaria-ScriptDeCriaçãoDeTabelas.sql";
obs: no caso de dúvidas, consulte a modelagem do banco de dados
*/
-- QUERIES (consultas):

-- 35) Selecionar o nome de todos os clientes, associar com seus pedidos, os nomes das pizzas escolhidas e verificar quem nunca fez um pedido;
create view clientes_pedidos as
    select tb_cliente.id_cliente, tb_cliente.nome, tb_pedido.id_pedido, tb_pizza.nome as nome_pizza from tb_cliente
    left join tb_pedido on tb_pedido.id_cliente = tb_cliente.id_cliente
    left join tb_pedido_pizza on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
    left join tb_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
    order by id_cliente;

-- Rodar view
select * from clientes_pedidos;

-- Cliente que nunca fizeram pedido
select * from clientes_pedidos where id_pedido is null;

-- 36) Selecionar o nome de todos os clientes que fizeram pedidos e mostrar qual o valor gasto por cada um até hoje na pizzaria; 

select tb_cliente.id_cliente, tb_cliente.nome, sum(preco) from tb_cliente
inner join tb_pedido on tb_pedido.id_cliente = tb_cliente.id_cliente
group by tb_cliente.id_cliente, tb_cliente.nome
order by tb_cliente.id_cliente;


-- 37) Selecionar o valor em vendas de todas as pizzas zero existentes;


select tb_pizza.id_pizza, tb_pizza.nome, sum(
case
    when quantidade = 'Meia' then tb_pizza.preco/2
    when quantidade = 'Inteira' then tb_pizza.preco
end) as preco
from tb_pedido
inner join tb_pedido_pizza on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
full outer join tb_pizza on tb_pedido_pizza.id_pizza = tb_pizza.id_pizza
group by tb_pizza.id_pizza, tb_pizza.nome, tb_pizza.preco
having tb_pizza.id_pizza in (select id_pizza from tb_pizza where categoria = 'Zero Lactose')
order by tb_pizza.id_pizza;

-- 38) Selecionar o valor e quantidade em vendas de todas as pizzas zero existentes;

select tb_pizza.id_pizza, tb_pizza.nome, sum(
case
    when quantidade = 'Meia' then tb_pizza.preco/2
    when quantidade = 'Inteira' then tb_pizza.preco
end) as preco, count(tb_pedido_pizza.id_pizza) as qtd_vendas from tb_pedido
inner join tb_pedido_pizza on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
full outer join tb_pizza on tb_pedido_pizza.id_pizza = tb_pizza.id_pizza
group by tb_pizza.id_pizza, tb_pizza.nome
having tb_pizza.id_pizza in (select id_pizza from tb_pizza where categoria = 'Zero Lactose')
order by tb_pizza.id_pizza;

-- 39) Selecionar o nome de todas as pizzas, associar com os pedidos, os nomes dos clientes que as escolheram e verificas quais pizzas nunca foram pedidas;

select tb_pizza.nome, tb_pedido.id_pedido, tb_cliente.nome from tb_pizza
left join tb_pedido_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
left join tb_pedido on tb_pedido_pizza.id_pedido = tb_pedido.id_pedido
left join tb_cliente on tb_pedido.id_cliente = tb_cliente.id_cliente;


-- Pizzas que nunca foram pedidas:

select * from (
select tb_pizza.nome, tb_pedido.id_pedido, tb_cliente.nome from tb_pizza
left join tb_pedido_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
left join tb_pedido on tb_pedido_pizza.id_pedido = tb_pedido.id_pedido
left join tb_cliente on tb_pedido.id_cliente = tb_cliente.id_cliente
) as ex_39
where id_pedido is null;

-- 40) Selecionar o preço médio de venda das categorias de pizza;

select categoria, to_char(avg(tb_pizza.preco),'99.99') from tb_pedido_pizza 
inner join tb_pedido on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
inner join tb_pizza on tb_pedido_pizza.id_pizza = tb_pizza.id_pizza
group by categoria;

-- 41) Selecionar todas as pizzas que possuem preço maior ou igual a 45 e menor ou igual a 55 de duas formas diferentes;

select * from tb_pizza where 45 <= preco and preco <=  55;


select * from tb_pizza where preco between 45 and 55;

-- 42) Mostrar todas as pizzas existentes no cardápio com nome, descrição, preço e com uma coluna adicional que indique se a pizza possui ou não presunto;

select id_pizza, nome, descricao, preco, 
(case
    when descricao ilike '%presunto%' then true
    else false
end) as tem_presunto
from tb_pizza;

-- 43) Selecionar de forma ordenada o nome e o valor das 5 pizzas mais baratas do cardápio em ordem crescente;

select nome, preco from tb_pizza order by preco asc limit 5;

-- 44)  Selecionar em ordem decrescente as 10 pizzas mais pedidas entre todas as pizzas com id, nome e quantidade de pedidos;

select tb_pedido_pizza.id_pizza, tb_pizza.nome, count(id_pedido) num_pedidos from tb_pedido_pizza
inner join tb_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
group by tb_pedido_pizza.id_pizza, tb_pizza.nome order by count(id_pedido) desc limit 10;

-- 45) Selecionar os 3 clientes que pediram menos pizzas nos bairros Liberdade e do Centro;

select tb_cliente.id_cliente, tb_cliente.nome, count(id_pedido) from tb_cliente 
inner join tb_pedido on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_cliente.id_cliente, tb_cliente.nome 
having endereco ilike '%Liberdade' or endereco ilike '%Centro' 
order by count(id_pedido) limit 3;

