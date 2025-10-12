create database mercado;
use mercado;

create table fornecedores (
	cod_forne char(10) primary key,
    nome varchar(100),
    cidade_sede varchar(50),
    grupo_cod_fornecedor char(10),
    foreign key fk_forne(grupo_cod_fornecedor) references fornecedores(cod_forne)
);

create table material (
	cod_material char(9) primary key,
    cod_fornecedor char(10),
    nome varchar(100),
    descricao varchar(200),
    foreign key fk_forne_mat(cod_fornecedor) references fornecedores(cod_forne)
);

insert into fornecedores values 
('ABC', 'ABC Materiais Eletricos', 'Vitória', null),
('Hix', 'HidraX Materiais ElÈtricos e Hidraulicos', 'São Paulo', null),
('XYZ', 'XYZ Materiais de Escritorio', 'Rio de Janeiro', 'Hix'),
('Hidra', 'Hidra Materiais Hidraulicos', 'São Paulo', 'Hix');

insert into material values 
('123', 'ABC', 'Tomada eletrica 10A Nova', 'Tomada eletrica 10A padrao novo'),
('234', 'ABC', 'Disjuntor 25A ', 'Disjuntor eletrico 25A '),
('345', 'XYZ', 'Resma Papel A4', 'Resma papel branco A4'),
('456', 'XYZ', 'Toner Imp HR5522 ', 'Toner impressora HR5522 '),
('678', 'Hidra', 'Cano PVC 1/2 ', 'Cano PVC 1/2 pol'),
('679', 'Hidra', 'Cano PVC 3/4', ' Cano PVC 3/4 pol'),
('680', 'Hidra', 'Medidor hidr 1/2 ', 'Medidor hidraulico 1/2 pol'),
('681', 'Hidra', 'Joelho 1/2 ', ' Conector Joelho 1/2 pol '),
('682', 'Hidra', 'Junta 1/2', 'Cano PVC 1/2 pol '),
('1234', 'ABC', 'Tomada eletrica 20A Nova', 'Tomada eletrica 20A padrao novo '),
('2345', 'XYZ', 'Caneta Azul ', 'Caneta esferografica azul '),
('4567', 'XYZ', 'Grapeador', 'Grampeador mesa pequeno '),
('4568', 'XYZ', ' Caneta Marca Texto Amarela', 'Caneta Marca Texto Amarela '),
('4569', 'XYZ', 'Lapis HB', 'Lapis Preto HB');

select material.cod_material,
	material.cod_fornecedor,
    material.nome,
    material.descricao,
    fornecedores.nome,
    fornecedores.cidade_sede,
    fornecedores.grupo_cod_fornecedor
from material 
join fornecedores on material.cod_fornecedor = fornecedores.cod_forne where cod_fornecedor = 'ABC' ;

select material.cod_material,
	material.cod_fornecedor,
    material.nome,
    material.descricao,
    fornecedores.nome,
    fornecedores.cidade_sede,
    fornecedores.grupo_cod_fornecedor
from material 
join fornecedores on material.cod_fornecedor = fornecedores.cod_forne where cod_fornecedor = 'XYZ';

select material.cod_material,
	material.cod_fornecedor,
    material.nome,
    material.descricao,
    fornecedores.nome,
    fornecedores.cidade_sede,
    fornecedores.grupo_cod_fornecedor
from material 
join fornecedores on material.cod_fornecedor = fornecedores.cod_forne where cod_fornecedor = 'Hidra';




