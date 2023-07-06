create database farmacia;
use clientes;

create table contatos(
codigo int primary key auto_increment,
nome varchar(100) not null,
cidade varchar(100) );

insert into contatos
values(1, "ana", "assu");

insert into contatos
values(2, "bianca", "areia branca");

# usando o auto_increment
insert into contatos
values(null, "catarina", "grossos");

# inserir mais de um registro
# com um único comando
insert into contatos values
(null,"damião","mossoró"),
(null, "elaine", "natal"),
(null, "fernando", "apodi");

#inserir apenas algumas colunas
insert into contatos (nome)
values("amorim");

insert into funcionario (nome, setor, salario)
values("katia","vendas", 5000);

# SELEÇÃO/LISTAGEM DE DADOS
select * from contatos;

# ORDENAR POR UMA COLUNA
select * from contatos order by nome;
select * from contatos order by cidade;

#ORDENAR DECRESCENTE
select * from contatos 
order by codigo desc;

insert into contatos values
(null,"carlos","apodi"),
(null,"miriam", "apodi"),
(null,"aline", "natal"),
(null,"sergio", "mossoro");

# ORDERNAR POR VÁRIAS COLUNAS
select * from contatos
order by cidade, nome;

# ordenar cada coluna com crescente ou decrescente
select * from contatos
order by cidade desc, nome;

# exibir apenas algumas colunas
select cidade, nome from contatos;

select cidade, nome from contatos
order by cidade;

#exibir apenas algumas linhas
select * from contatos
where nome = "fernando";

select * from contatos
where cidade = "apodi";  #igual

select * from contatos
where codigo < 4;  # menor que

select * from contatos
where codigo > 6; # maior que

select * from contatos
where codigo >= 6; # maior ou igual a

select * from contatos
where codigo <= 4; # menor ou igual a

select * from contatos
where cidade <> "apodi"; # diferente

# combinar tudo em um comando
select cidade, nome from contatos
where cidade = "apodi" order by nome desc;

