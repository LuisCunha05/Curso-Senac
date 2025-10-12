create database estrutura;
use estrutura;

create table cliente (
	cod_cliente int unsigned auto_increment primary key,
    nome varchar(100),
    datanascimento date,
    cpf char(15)
);

create table pedido(
	cod_pedido int unsigned auto_increment primary key,
    cod_cliente int unsigned not null,
    data_pedido date not null,
    nf char(9) not null,
    valor_total float not null,
    foreign key (cod_cliente) references cliente(cod_cliente)
);

create table produto (
	cod_produto int unsigned auto_increment primary key,
    descricao varchar(500),
    quantidade int unsigned not null
);

create table item_pedido (
	cod_pedido int unsigned,
    numero_item int unsigned not null,
    valor_unitario float,
    quantidade int unsigned not null,
    cod_produto int unsigned,
    constraint Item_PK primary key (cod_pedido, numero_item),
    foreign key (cod_pedido) references pedido(cod_pedido),
    foreign key (cod_produto) references produto(cod_produto)
);

create table log(
	cod_log int unsigned auto_increment primary key,
    data_log date not null,
    descricao varchar(500) not null
);

create table req_compra(
	cod_req_compra int unsigned auto_increment primary key,
    cod_produto int unsigned,
    data_req_compra date not null,
    quantidade int unsigned not null,
    foreign key (cod_produto) references produto(cod_produto)
);

insert into cliente (nome, datanascimento, cpf) values
	('Ana Silva', '1990-05-15', '123.456.789-00'),
	('João Oliveira', '1985-10-20', '234.567.890-11'),
	('Maria Santos', '2000-02-25', '345.678.901-22'),
	('Carlos Pereira', '1992-08-30', '456.789.012-33'),
	('Luciana Costa', '1988-11-05', '567.890.123-44'),
	('Felipe Almeida', '1995-03-14', '678.901.234-55'),
	('Patricia Souza', '1981-07-22', '789.012.345-66'),
	('Ricardo Lima', '1979-12-31', '890.123.456-77'),
	('Fernanda Rocha', '1993-06-11', '901.234.567-88'),
	('Eduardo Martins', '1987-09-18', '012.345.678-99');

insert into produto (descricao, quantidade) values 
	('Muito bom', 23),
	('Muito coisado', 13),
	('Coisado bom', 36),
	('Opa bom', 48),
	('Talvez bom', 82),
	('Talvez ruim', 43),
	('Muito bom', 44),
	('Muito ótimo', 69);
    
INSERT INTO pedido (cod_cliente, data_pedido, nf, valor_total) VALUES
(1, '2024-01-10', '234526789', 150.75),
(9, '2024-01-15', '876543321', 200.00),
(2, '2024-01-20', '122334445', 75.50),
(7, '2024-01-25', '566778489', 300.25),
(5, '2024-02-01', '988776635', 125.40);

insert into item_pedido (cod_pedido, numero_item, valor_unitario, quantidade, cod_produto) values
(2, 7, 19.99, 3, 4),
(1, 3, 29.99, 10, 2),
(3, 4, 99.99, 4, 3),
(4, 1, 69.99, 6, 7),
(5, 8, 49.99, 2, 8);


select * from item_pedido;
