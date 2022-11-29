/* 

* Criar um banco de dados com uma tabela funcionário com os campos id, nome, profissão e data de nascimento;

* Criar uma tabela de auditoria da tabela funcionário com os campos id, nome e data;

* Criar uma trigger para registrar o id, nome e a hora que um registro foi inserido na tabela funcionário;

* Demonstrar o funcionamento da trigger.

*/

-- criação das tabelas;

create table funcionario (
    funcionarioid int primary key,
    nome varchar(50),
    profissao varchar(50),
    data_nascimento date 
);

create table funcionario_log (
    funcionarioid int,
    foreign key (funcionarioid) references funcionario(funcionarioid),
    nome varchar(50),
    data timestamp
);

-- criação da função;

create or replace function func_log_funcionario()
    returns trigger
    language plpgsql
    as
$$
begin
	insert into	funcionario_log (funcionarioid, nome, data)
	values (new.funcionarioid, new.nome, current_timestamp);
return new;
END;
$$;

-- criação da trigger;

create trigger trigger_log_funcionario
    after insert on funcionario
        for each row 
            execute procedure func_log_funcionario();

-- funcionamento da trigger;

insert into funcionario(funcionarioid, nome, profissao, data_nascimento) 
values
      (1, 'Lucas Canella', 'Analista de dados', '2001-05-10'),
      (2,'Luiza Sampaio', 'Analista de dados', '2000-07-07'),
      (3,'Rosângela Farias','Cientista de dados','1995-09-27');
      
select * from funcionario;
select * from funcionario_log;
