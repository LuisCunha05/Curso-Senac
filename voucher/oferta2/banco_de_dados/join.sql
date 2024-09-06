create database joines;
use joines;
create table estado(
	id_estado int primary key auto_increment,
	nome varchar(100)
);

create table cidade(
	id_cidade int primary key auto_increment,
	nome varchar(100)
);

create table pessoa(
	id int primary key auto_increment,
	nome varchar(100),
    id_estado int,
    id_cidade int,
    foreign key fk_cidade (id_cidade) references cidade(id_cidade),
    foreign key fk_estado (id_estado) references estado(id_estado)
);

insert into cidade(nome) values 
('Campo Grande'),
('Dourados'),
('Bonito'),
('Aquidauana'),
('Terenos');

insert into cidade(nome) values 
('Cuiabá'),
('Londrina'),
('São Paulo'),
('Araguari');

insert into estado(nome) values 
('Mato Grosso do Sul'),
('São Paulo'),
('Minas Gerais'),
('Mato Grosso'),
('Paraná');

insert into pessoa (nome, id_cidade, id_estado) values
('Ederson da Costa', 1, 2),
('Maria Aparecida', 2, 2),
('Pedro Correia', 1, 3),
('Michal Jackson', 2, 3),
('Fredie Mercury', 3, 5);

select pessoa.nome,cidade.nome,estado.nome from pessoa join cidade on pessoa.id_cidade = cidade.id_cidade join estado on pessoa.id_estado = estado.id_estado;
select pessoa.nome,cidade.nome,estado.nome from pessoa left join cidade on pessoa.id_cidade = cidade.id_cidade left join estado on pessoa.id_estado = estado.id_estado;
select pessoa.nome,cidade.nome,estado.nome from pessoa right join cidade on pessoa.id_cidade = cidade.id_cidade right join estado on pessoa.id_estado = estado.id_estado;
select pessoa.nome,cidade.nome,estado.nome from cidade left join pessoa on cidade.id_cidade = pessoa.id_cidade left join estado on pessoa.id_estado = estado.id_estado;
select pessoa.nome,cidade.nome,estado.nome from pessoa cross join cidade cross join estado;
select * from pessoa cross join cidade cross join estado;
select cidade.nome from cidade union select estado.nome from estado;
