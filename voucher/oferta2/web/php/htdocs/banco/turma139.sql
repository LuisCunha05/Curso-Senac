-- Active: 1725968277993@@10.28.2.34@3306@turma139

use turma139;

show tables;

create table if not exists usuario(
    id_usuario int PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) UNIQUE,
    senha VARCHAR(100)
);

CREATE Table cliente(
    id_cliente int PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30),
    sobrenome VARCHAR(30),
    telefone VARCHAR(20),
    endereco VARCHAR(30),
    email VARCHAR(30),
    sexo VARCHAR(30)
);

alter Table usuario add COLUMN setor int DEFAULT 0; --0 usuario comun, 1 admin

insert into usuario(nome,senha,setor) values ('luiscunha','senha321', 0);
insert into usuario(nome,senha,setor) values ('admiro', 'senha123', 1);

INSERT into cliente(nome,sobrenome,telefone,endereco,email,sexo) values ('Luís', 'Cunha', '0800666666', 'Rua Casa', 'cunha@email.com','Masculino');

insert into cliente(nome,sobrenome,telefone,endereco,email,sexo) values ('teste', 'sobretest', '123', 'casa', 'teste@email.com', 'Masculino');

CREATE Table produto(
    id_produto int PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    descricao VARCHAR(50),
    preco VARCHAR(20)
);

INSERT INTO produto VALUES 
    (NULL, "teclado", 'usado para teclar', "129.99"),
    (NULL, "mouse", 'usado para mausar', "229.99"),
    (NULL, "fone", 'usado para fonar', "599.99");

alter table cliente MODIFY nome varchar(30) UNIQUE;
alter table cliente MODIFY email varchar(30) UNIQUE;

DESCRIBE cliente;
    

select * from usuario;

DESCRIBE usuario;