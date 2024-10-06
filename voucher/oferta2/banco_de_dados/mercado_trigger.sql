-- Active: 1725635299265@@127.0.0.1@3306@auto_mercado
create DATABASE auto_mercado;
use auto_mercado;


CREATE Table religiao(
    id_religiao int PRIMARY KEY AUTO_INCREMENT,
    tipo_religiao VARCHAR(30)
);


create table estado (
	id_estado int auto_increment primary key,
    estado varchar(30)
);

create table cidade (
	id_cidade int auto_increment primary key,
    cidade varchar(40),
    id_estado int,
    foreign key (id_estado) references estado(id_estado)
);

create table genero (
	id_genero int auto_increment primary key,
    tipo varchar(20)
);

create table raca (
	id_raca int auto_increment primary key,
    raca varchar(30)
);

create table estado_civil (
	id_estado_civil int auto_increment primary key,
    estado_civil varchar(30)
);

CREATE Table endereco (
    id_endereco INT PRIMARY KEY AUTO_INCREMENT,
    rua VARCHAR(100),
    numero_endereco VARCHAR(10),
    bairro VARCHAR(100),
    id_cidade INT,
    Foreign Key (id_cidade) REFERENCES cidade(id_cidade)
);

CREATE Table agencia (
    id_agencia int PRIMARY KEY AUTO_INCREMENT,
    numero_agencia VARCHAR(20) UNIQUE,
    id_cidade INT,
    id_endereco INT,
    Foreign Key (id_cidade) REFERENCES cidade(id_cidade),
    Foreign Key (id_endereco) REFERENCES endereco(id_endereco)
);

create table cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome varchar(100),
	cpf char(15) UNIQUE,
    rg char(15),
    fone char(15),
    data_nascimento date,
    saldo FLOAT,
    conta_numero VARCHAR(20) UNIQUE,
    id_cidade int,
    id_genero int,
    id_raca int,
    id_estado_civil int,
    id_religiao int,
    id_agencia INT,
    id_endereco INT,
    foreign key (id_cidade) references cidade(id_cidade),
    foreign key (id_genero) references genero(id_genero),
    foreign key (id_raca) references raca(id_raca),
    foreign key (id_estado_civil) references estado_civil(id_estado_civil),
    Foreign Key (id_religiao) REFERENCES religiao(id_religiao),
    Foreign Key (id_agencia) REFERENCES agencia(id_agencia),
    Foreign Key (id_endereco) REFERENCES endereco(id_endereco)
);

CREATE Table saque(
    id_saque INT PRIMARY KEY AUTO_INCREMENT,
    valor FLOAT,
    id_agencia INT,
    conta_numero VARCHAR(20),
    Foreign Key (id_agencia) REFERENCES agencia(id_agencia),
    Foreign Key (conta_numero) REFERENCES cliente(conta_numero)
);

DELIMITER $
CREATE Trigger insert_saque_update BEFORE INSERT ON saque
    FOR EACH ROW BEGIN
        IF NEW.valor < 0 OR
            NEW.valor > (SELECT saldo from cliente where conta_numero=NEW.conta_numero)
                THEN
                    SIGNAL SQLSTATE '45000';
        ELSE
            UPDATE cliente SET saldo = saldo - NEW.valor WHERE conta_numero = NEW.conta_numero;
        END IF;
    END$

-- DROP Trigger insert_saque_update;
DELIMITER ;

CREATE Table deposito(
    id_deposito INT PRIMARY KEY AUTO_INCREMENT,
    valor FLOAT,
    id_agencia INT,
    conta_numero VARCHAR(20),
    Foreign Key (id_agencia) REFERENCES agencia(id_agencia),
    Foreign Key (conta_numero) REFERENCES cliente(conta_numero)
);

DELIMITER $
CREATE Trigger insert_deposito_update BEFORE INSERT ON deposito
    FOR EACH ROW BEGIN
        IF NEW.valor < 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Valor do deposito não pode negativo!';
        ELSE
            UPDATE cliente SET saldo = saldo + NEW.valor WHERE conta_numero = NEW.conta_numero;
        END IF;
    END$
 -- DROP TRIGGER insert_deposito_update;
DELIMITER ;

INSERT INTO religiao (tipo_religiao) VALUES
('Catolicismo'),
('Protestantismo'),
('Espiritismo'),
('Umbanda'),
('Budismo');


insert into genero (tipo) values
('Masculino'),
('Feminino'),
('Outro');

insert into raca (raca) values
('Branco'),
('Negro'),
('Amarelo'),
('Pardo'),
('Indígina');

insert into estado_civil (estado_civil) values
("Solteiro(a)"),
("Casado(a)"),
("Viúvo(a)"),
("Separado(a)"),
("Divorciado(a)");

insert into estado (estado) values 
('Acre'),
('Alagoas'),
('Amapá'),
('Amazonas'),
('Bahia'),
('Ceará'),
('Distrito Federal'),
('Espírito Santo'),
('Goiás'),
('Maranhão'),
('Mato Grosso'),
('Mato Grosso do Sul'),
('Minas Gerais'),
('Pará'),
('Paraíba'),
('Paraná'),
('Pernambuco'),
('Piauí'),
('Rio de Janeiro'),
('Rio Grande do Norte'),
('Rio Grande do Sul'),
('Rondônia'),
('Roraima'),
('Santa Catarina'),
('São Paulo'),
('Sergipe'),
('Tocantins');

INSERT INTO cidade (cidade, id_estado) VALUES
-- Acre (AC)
('Rio Branco',1),          
('Maceió',2),                                
('Coari',4),           
('Ilhéus',5),  
('Campo Grande',12),                
('Betim',13),           
('Castanhal',14),                        
('Ariquemes',22),                
('São João da Baliza',23),   
('Porto Nacional',27);

INSERT INTO endereco (rua, numero_endereco, bairro, id_cidade) VALUES
('Rua das Flores', '123', 'Jardim das Rosas', 5),
('Avenida Brasil', '456', 'Centro', 2),
('Rua dos Pinheiros', '789', 'Bairro Alto', 3),
('Travessa do Sol', '32', 'São Jorge', 7),
('Rua das Acácias', '45A', 'Parque Verde', 10);

INSERT INTO agencia (numero_agencia, id_cidade, id_endereco) VALUES
('123', 5, 1),
('456', 3, 3),
('789', 7, 2),
('321', 6, 4),
('654', 9, 5);

INSERT INTO cliente (nome, cpf, rg, fone, data_nascimento, saldo, conta_numero, id_cidade, id_genero, id_raca, id_estado_civil, id_religiao, id_agencia, id_endereco) VALUES
('Ana Silva', '123.456.789-00', '12.345.678-9', '987654321', '1990-05-15', 1500.75, '0001', 1, 1, 1, 1, 1, 1, 1),
('Carlos Souza', '234.567.890-01', '23.456.789-0', '876543210', '1985-08-20', 2500.50, '0002', 2, 2, 2, 2, 2, 2, 2),
('Maria Oliveira', '345.678.901-02', '34.567.890-1', '765432109', '1992-12-30', 1800.00, '0003', 3, 1, 3, 1, 1, 3, 3),
('João Santos', '456.789.012-03', '45.678.901-2', '654321098', '1988-03-10', 3000.25, '0004', 4, 2, 1, 2, 2, 4, 4),
('Lucia Mendes', '567.890.123-04', '56.789.012-3', '543210987', '1995-07-22', 2200.90, '0005', 5, 1, 2, 1, 1, 5, 5);

INSERT INTO saque VALUES (NULL, 100.25, 3,'0001');
INSERT INTO saque VALUES (NULL, -100.25, 3,'0001');
INSERT INTO saque VALUES (NULL, 20000.25, 3,'0001');

INSERT INTO deposito VALUES (NULL, 300.3, 2, '0004');

INSERT INTO deposito VALUES (NULL, -300.3, 2, '0004');