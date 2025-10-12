---- criar o BD ecommerce
create database ecommerce; -- #1 database estava escrito errado
use ecommerce; -- #2 use estava escrito errado

---------------------------------------------

create table  produtos ( -- #3 Faltando ( 
    id_prod int(5) auto_increment not null, -- #4 auto_increment estava escrito errado
    nome_prod varchar(100) not null,
    descricao text, -- #5 Faltando uma virgula nessa linha após text
    modelo varchar(50),
    id_categoria int(5), -- #6 falta uma virgula nessa linha
    id_fabricante int(5),
    constraint primary key (id_prod)-- #7 faltava uma primary key nessa tabela
);

   
create table clientes ( -- #8 table estava escrito errado
    id_cli int(5) auto_increment not null, -- #9 nome da coluna continha caractere ' ' que é invalido. #13 tipo de dado da coluna era invalido para auto_increment
    nome varchar(100) not null,
    cpf int(11),
    telefone varchar(50),
    sexo enum('F','M'), -- #10 Faltava uma virgula nessa linha
    cadastro datetime, -- #11 datetime estava escrito errado
    constraint primary key (id_cli) -- #12 primary key estava escrio errado
);

create table pedidos(
	num_pedido int(5) auto_increment not null,
	data datetime,
	status_pedido varchar(50), -- #14 caluna estava nome para identificador com palavra reservada
	id_cli int(5),
	constraint primary key (num_pedido),
	constraint foreign key (id_cli) references clientes(id_cli)
);

   
create table pedido_item( -- #15 table estava escrito errado
	idtem_pedido int(5) auto_increment not null,
	num_pedido int(5) not null,
    qtde int(5) not null,
    valor_unit decimal(10,2),
    total decimal(10,2),
    id_prod int(5),
    constraint primary key (idtem_pedido),
    constraint foreign key (num_pedido) references pedidos(num_pedido), -- #16 foreign key estava escrito errado
    constraint foreign key (id_prod) references produtos(id_prod)  -- #17 foreign key estava escrito errado
);

create table estoque_produtos(
	id_estoque int(5) auto_increment, -- #34 primary key não era auto_increment
	quantidade int(5) not null,
	quant_min int(5),
	id_prod int(5), -- #18 faltava um ) em int(5)
	constraint primary key (id_estoque),
	constraint foreign key (id_prod) references produtos(id_prod)
);
select * from clientes;
insert into clientes values (null,'João','02102202324','6799999999','M',now()); -- #19 nome da tabela estava incorreto 
insert into clientes values (null,'Tadeu','02102202366','6799999999','M',now()); -- #20 insert estava escrito errado e o comando estava após outro comando
insert into clientes values (null,'Francisco','02102202399','6799999999','M',now());
insert into clientes values (null,'Maria','02102202377','6799999999','F',now());
insert into clientes values (null,'Antonia','02102202388','6799999999','F',now());
   
insert into produtos values (null,'Notebook Dell','Core i5,8GB,SDD 240GB','Inspirion 1500',null,null);
insert into produtos values (null,'Notebook Acer','Core i5,8GB,SDD 240GB','Aspire T',null,null);
insert into produtos values (null,'Notebook Asus','Core i5,8GB,SDD 240GB','A95Z',null,null);
insert into produtos values (null,'Notebook Apple','Core i7, 16GB, SDD 512GB','BookPRo',null,null);
insert into produtos values (null,'Notebook Positivo','Celerom,4GB,HD 1TB','POS8080',null,null);
   
insert into produtos values (null,'Placa-Mãe ASUS','Onboard','P',null,null);
insert into produtos values (null,'Processador AMD','4.2Ghz','Ryzen5',null, null); -- #21 uma string faltava os ' e faltava uma virgula depois do primero null


insert into produtos values (null,'Placa de Vídeo RADEON','8GB','RX5500',null,null);
insert into produtos values (null,'Fonte Corsair','Selo 80plus','CX1200W',null, null); -- #22 uma string faltava os ' e faltava uma virgula depois do primero null

   
select * from produtos; -- #23 from estava escrito errado
describe estoque_produtos; -- #24 describe estava escrito errado

insert into estoque_produtos values (null,80,10,1);
insert into estoque_produtos values (null,44,5,9); -- #25 into e values estavam escritos errados. o nome da tabela tambem estava errado
insert into estoque_produtos values (null,55,5,8);-- #26 into e values estavam escritos errados. o nome da tabela tambem estava errado
insert into estoque_produtos values (null,36,5,7);-- #27 into e values estavam escritos errados. o nome da tabela tambem estava errado
insert into estoque_produtos values (null,49,5,6);-- #28 into e values estavam escritos errados. o nome da tabela tambem estava errado
insert into estoque_produtos values (null,100,5,1);-- #29 into e values estavam escritos errados. o nome da tabela tambem estava errado
insert into estoque_produtos values (null,100,5,2);-- #30 into e values estavam escritos errados. o nome da tabela tambem estava errado
insert into estoque_produtos values (null,100,5,3);-- #31 into e values estavam escritos errados. o nome da tabela tambem estava errado
insert into estoque_produtos values (null,100,5,4);-- #32 into e values estavam escritos errados. o nome da tabela tambem estava errado
insert into estoque_produtos values (null,100,5,5);-- #33 into e values estavam escritos errados. o nome da tabela tambem estava errado
 