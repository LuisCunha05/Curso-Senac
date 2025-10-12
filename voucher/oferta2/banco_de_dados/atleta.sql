create database sprint;
use sprint;

create table atleta (
	id_atleta int primary key auto_increment,
    nome varchar(40),
    modalidade varchar(40),
    qtd_medalha smallint
);

INSERT INTO atleta (nome, modalidade, qtd_medalha) VALUES
('João Silva', 'Futebol', 3),
('Carlos Santos', 'Futebol', 2),
('Maria Oliveira', 'Natação', 5),
('Ana Costa', 'Natação', 4),
('Pedro Almeida', 'Atletismo', 6),
('Lucas Pereira', 'Atletismo', 1),
('Fernanda Lima', 'Vôlei', 2),
('Juliana Martins', 'Vôlei', 3),
('Roberto Fernandes', 'Judô', 7),
('Paulo Souza', 'Judô', 4);

set sql_safe_updates = 0;
select * from atleta; -- 1
update atleta set qtd_medalha = 5 where id_atleta = 1; -- 2
update atleta set qtd_medalha = 5 where id_atleta  between 2 and 3; -- 3
update atleta set nome='Ana Costa da Silva' where id_atleta = 4; -- 4
alter table atleta add dt_nasc date; -- 5
update atleta set dt_nasc = (current_date()); -- 6
update atleta set dt_nasc = (replace(dt_nasc, '2024', '1980')); -- 6
delete from atleta where id_atleta = 5; -- 7
select * from atleta where modalidade != 'Natação'; -- 8
select * from atleta where qtd_medalha >= 3; -- 9
alter table atleta modify column modalidade varchar(60);
describe atleta;
truncate atleta;



