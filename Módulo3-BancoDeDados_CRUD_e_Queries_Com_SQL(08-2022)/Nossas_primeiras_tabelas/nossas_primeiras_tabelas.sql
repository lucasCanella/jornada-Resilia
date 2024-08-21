/* Vamos criar duas tabelas:
facilitadores: id, nome,cpf, frente;
resilientes: id, nome, cpf, turma;

* inserir valores
* atualizar a "frente" de todos os facilitadores pra 'TECH'
* esvazie as tabelas por meio do delete
* apague as tabelas
*/

create table facilitadores (
    id int primary key,
    nome varchar(100),
    cpf varchar(14),
    frente varchar(4)
);

create table resilientes (
    id int primary key,
    nome varchar(100),
    cpf varchar(14),
    turma int
);

insert into facilitadores(id, nome, cpf, frente)
values
(1,'Davi Lucca Pereira','452.123.441-07','SOFT'),
(2,'Vitoria Albuquerque','157.162.761-80','SOFT'),
(3,'Dra. Feliciano Costa','206.071.336-60','SOFT'),
(4,'Marcia Oliveira Neto','886.417.584-96','SOFT'),
(5,'Enzo Gabriel Xavier','061.365.051-42','SOFT'),
(6,'Sara Nogueira','036.301.263-08','SOFT'),
(7,'Lucas Santos','371.500.626-95','SOFT'),
(8,'Deneval Souza','402.846.368-86','TECH'),
(9,'Benjamin Moraes','118.428.324-92','TECH'),
(10,'Joaquim Martins','814.457.831-77','SOFT');

select * from resilientes;

update facilitadores set frente = 'TECH';

delete from facilitadores;

drop table facilitadores;
