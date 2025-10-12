-- Active: 1725635299265@@127.0.0.1@3306@fofoca
CREATE DATABASE titanic_base;
use titanic_base;

CREATE TABLE passageiros(
    id_passageiro INT PRIMARY KEY,
    sobreviveu INT,
    classe_passageiro INT,
    nome VARCHAR(100),
    sexo VARCHAR(20),
    idade varchar(10),
    sibling_sp INT,
    parent_child INT,
    ticket VARCHAR(20),
    fare FLOAT,
    cabine VARCHAR(20),
    embarque CHAR(1)
);

select * from passageiros order by idade;
select count(*) from passageiros where sobreviveu = 1;
select count(*) from passageiros where idade < 12;
select count(*) from passageiros where sobreviveu = 1 and sexo = 'female';
select count(*) from passageiros where sobreviveu = 1 and sexo = 'male';
