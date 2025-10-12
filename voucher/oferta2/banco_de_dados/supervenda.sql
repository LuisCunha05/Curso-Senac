-- Active: 1725635299265@@127.0.0.1@3306@supervenda
create database supervenda;
use supervenda;

create table produto(
    referencia VARCHAR(3) PRIMARY KEY,
    descricao VARCHAR(50),
    estoque int not NULL DEFAULT 0
);

create table item_venda (
    venda int,
    produto VARCHAR(3),
    quantidade int,
    Foreign Key (produto) REFERENCES produto(referencia)
);

INSERT into produto VALUES 
('001', 'Feijão', 10),
('002', 'Arroz', 5),
('003', 'Farinha', 15);

INSERT into item_venda VALUES 
(1, '001', 4),
(2, '002', 2),
(3, '003', 7);

SELECT * from item_venda;

SELECT venda,produto,quantidade,descricao from item_venda JOIN produto on item_venda.produto=produto.referencia;

DELIMITER $
CREATE TRIGGER trg_item_venda_insert AFTER INSERT
    on item_venda
        for each ROW
            begin
                update produto set estoque = estoque - NEW.quantidade
            where referencia = NEW.produto and estoque >= NEW.quantidade;
end$

DELIMITER ;
SELECT * from produto;

INSERT into item_venda VALUES 
(1, '002', -3);

-- drop Trigger if EXISTS trg_item_venda_insert;
DELIMITER $

create trigger trg_item_venda_delete after DELETE
    on item_venda
        for each ROW
            begin
                update produto set estoque = estoque + old.quantidade
            where referencia = OLD.produto;
end$

DELIMITER ;

SELECT * from item_venda;
DELETE from item_venda where venda=1;