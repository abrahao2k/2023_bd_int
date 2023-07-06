create database aula3;
use aula3;
create table livros(
codigo int primary key auto_increment,
titulo varchar(100),
autor varchar(100),
genero varchar(100),
preco float);

insert into livros values
(1, "O coração de Nanquim",
"Robert Galbraith", "Suspense", 71.16);

insert into livros values
(2, "Revelação Brutal", "Louise Penny",
"Suspense", 42.74);

insert into livros values
(3, "Na calada da noite", "Nora Roberts",
"Romance", 34.90);

# ATUALIZAR UM REGISTRO
UPDATE livros
SET preco = 29.90
WHERE codigo = 3;     # IMPORTANTÍSSIMO !!!!!!

update livros
set genero = "Policial"
where codigo = 2;

# atualizar várias colunas de uma vez
update livros
set genero = "Mistério",
    preco = 49.90
where codigo = 1;

# atualizar vários registros de uma vez
# definir um intervalo com between
update livros
set preco = 19.90
where codigo between 1 and 3;

# registros não sequenciais
# criar um conjunto usando IN
update livros
set preco = 34.90
where codigo IN (1, 3);

# atualizar por outra coluna que
# não seja o código
# vários registros poderão ser afetados
update livros
set preco = 9.90
where genero = "Policial";

# conjunto com palavras
update livros
set preco = 29.90
where genero IN ("Mistério", "Romance");


insert into livros values
(4, "Revelação Legal", "Louise Penny",
"Policial", 42.74);


# EXCLUIR UM REGISTRO (linha inteira)
delete from livros
where codigo = 3;

# BUSCA POR TEXTO
select * from livros
where genero = "Policial";


select * from livros
where autor = "Louise Penny";

# pesquisar com parte do texto
# o % substitui qualquer texto
# começa com Louise e qualquer texto depois
select * from livros
where autor LIKE "Louise%";

# começa com qualquer texto e termina com brutal
select * from livros
where titulo LIKE "%brutal";

# calada aparece em qualquer parte do texto
# (inicio, meio ou fim)
select * from livros
where titulo LIKE "%calada%";