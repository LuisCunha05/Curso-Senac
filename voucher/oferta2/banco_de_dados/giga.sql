-- Active: 1725635299265@@127.0.0.1@3306@sprint
create DATABASE giga;
use giga;

create table cidade (
    id_cidade int PRIMARY key AUTO_INCREMENT,
    nome_cidade VARCHAR(50)
);

create table endereco (
    id_endereco int PRIMARY key AUTO_INCREMENT,
    id_cidade int,
    bairro VARCHAR(100),
    rua VARCHAR(100),
    numero int,
    Foreign Key (id_cidade) REFERENCES cidade(id_cidade)
);

create Table raca (
    id_raca int PRIMARY key AUTO_INCREMENT,
    tipo VARCHAR(20)
);

create Table perfil (
    id_perfil int PRIMARY key AUTO_INCREMENT,
    id_raca int,
    idade SMALLINT,
    tipo_sangue CHAR(2),
    Foreign Key (id_raca) REFERENCES raca(id_raca)
);

CREATE Table status_icms (
    id_status int PRIMARY key AUTO_INCREMENT,
    tipo VARCHAR(50)
);

CREATE Table reg_tributacao (
    id_reg_tributacao int PRIMARY key AUTO_INCREMENT,
    tipo VARCHAR(50)
);

CREATE Table contato (
    id_contato int PRIMARY key AUTO_INCREMENT,
    numero VARCHAR(20),
    whatsapp VARCHAR(20),
    fax VARCHAR(20),
    instagram VARCHAR(30),
    email VARCHAR(40)
);

CREATE Table vendedor (
    id_vendedor int PRIMARY key AUTO_INCREMENT,
    nome VARCHAR(50),
    telefone VARCHAR(20),
    cnpj VARCHAR(30),
    email VARCHAR(50)
);

CREATE table extra(
    id_extra int PRIMARY key AUTO_INCREMENT,
    cor_favorita varchar(30),
    altura float,
    tamanho_pe float
);

CREATE table sexo(
    id_sexo int PRIMARY key AUTO_INCREMENT,
    tipo VARCHAR(20)
);

CREATE table frete_padrao(
    id_frete_padrao int PRIMARY key AUTO_INCREMENT,
    tipo VARCHAR(20)
); 

CREATE Table tabela_de_preco(
    id_preco int PRIMARY key AUTO_INCREMENT,
    tipo VARCHAR(50)
);

CREATE table status_cadastro(
    id_status_cadastro int PRIMARY key AUTO_INCREMENT,
    tipo VARCHAR(50)
);

CREATE Table  dados_adicionais(
    id_dado_adc int PRIMARY key AUTO_INCREMENT,
    status_civil VARCHAR(20),
    tem_filho enum("s","n"),
    id_endereco int,
    Foreign Key (id_endereco) REFERENCES endereco(id_endereco)
);
CREATE Table clientes_relacionados(
    id_clientes_relacionados int PRIMARY key AUTO_INCREMENT,
    data_criancao date,
    id_outra_pessoa int
);

CREATE table financeiro(
    id_financeiro int PRIMARY key AUTO_INCREMENT,
    conta VARCHAR(30),
    banco VARCHAR(20),
    operacao VARCHAR(30)
);

create table tipo_user(
    id_tipo_user int PRIMARY key AUTO_INCREMENT,
    tipo VARCHAR(30)
);
CREATe Table login_usr(
    id_login int PRIMARY key AUTO_INCREMENT,
    id_tipo_user int,
    email VARCHAR(100),
    senha VARCHAR(100),
    Foreign Key (id_tipo_user) REFERENCES tipo_user(id_tipo_user)
);

create table peca(
    id_peca int PRIMARY key AUTO_INCREMENT,
    ci VARCHAR(50),
    ordem VARCHAR(50),
    codigo VARCHAR(20),
    status_ VARCHAR(50),
    custo_unitario float,
    custo_total float,
    variante VARCHAR(50),
    descricao VARCHAR(120),
    qtd_base int,
    qtd int,
    qt_fix_variavel int
);

CREATE table nota_fiscal(
    id_nf int PRIMARY key AUTO_INCREMENT,
    id_tabela_de_preco int,
    id_vendedor int,
    desconto FLOAT,
    frete FLOAT,
    aprovacao_cliente VARCHAR(20),
    hora_aprovacao time,
    data_previsao date,
    data_vencimento date,
    Foreign Key (id_tabela_de_preco) REFERENCES tabela_de_preco(id_preco),
    Foreign Key (id_vendedor) REFERENCES vendedor(id_vendedor)
);

CREATE Table produtos_nf (
    id_produto int PRIMARY key AUTO_INCREMENT,
    id_nf int,
    id_peca int,
    quantidade INT,
    Foreign Key (id_nf) REFERENCES nota_fiscal(id_nf),
    Foreign Key (id_peca) REFERENCES peca(id_peca)
);

CREATE Table pessoa (
    id_pessoa int PRIMARY key AUTO_INCREMENT,
    nome VARCHAR(40),
    ramal VARCHAR(40),
    rg VARCHAR(40),
    email VARCHAR(40),
    email_loja_virtual VARCHAR(40),
    email_danf VARCHAR(40),
    email_comercial VARCHAR(40),
    email_cobranca VARCHAR(40),
    inscricao_estadual VARCHAR(40),
    telefone_comercial VARCHAR(40),
    telefone_celular VARCHAR(40),
    cpf VARCHAR(40) unique,
    transportadora1 VARCHAR(40),
    transportadora2 VARCHAR(40),
    inscricao_sufra VARCHAR(40),
    linha_pef VARCHAR(40),
    cnpj VARCHAR(50) UNIQUE,
    imagem VARCHAR(100),
    data_nascimento date,
    carga_tributaria FLOAT,
    aliquota FLOAT,
    id_sexo int,
    id_tabela_de_preco INT,
    id_frete_padrao int,
    fornecedor ENUM('s', 'n'),
    id_status_cadastro int,
    id_status int,
    id_reg_tributacao int,
    id_dados_adicionais int,
    id_endereco int,
    id_perfil int,
    id_contato int,
    id_vendedor int,
    id_extra int,
    id_financeiro int,
    id_clientes_relacionados int,
    Foreign Key (id_sexo) REFERENCES sexo(id_sexo),
    Foreign Key (id_tabela_de_preco) REFERENCES tabela_de_preco(id_preco),
    Foreign Key (id_frete_padrao) REFERENCES frete_padrao(id_frete_padrao),
    Foreign Key (id_status_cadastro) REFERENCES status_cadastro(id_status_cadastro),
    Foreign Key (id_status) REFERENCES status_icms(id_status),
    Foreign Key (id_reg_tributacao) REFERENCES reg_tributacao(id_reg_tributacao),
    Foreign Key (id_dados_adicionais) REFERENCES dados_adicionais(id_dado_adc),
    Foreign Key (id_endereco) REFERENCES endereco(id_endereco),
    Foreign Key (id_perfil) REFERENCES perfil(id_perfil),
    Foreign Key (id_contato) REFERENCES contato(id_contato),
    Foreign Key (id_vendedor) REFERENCES vendedor(id_vendedor),
    Foreign Key (id_extra) REFERENCES extra(id_extra),
    Foreign Key (id_financeiro) REFERENCES financeiro(id_financeiro),
    Foreign Key (id_clientes_relacionados) REFERENCES clientes_relacionados(id_clientes_relacionados)
);

CREATE table ordem_servico(
    id_ordem_servico int PRIMARY key AUTO_INCREMENT,
    id_nf int,
    id_peca int,
    id_pessoa int,
    execucao VARCHAR(20),
    servico varchar(20),
    data_emissao date,
    Foreign Key (id_nf) REFERENCES nota_fiscal(id_nf),
    Foreign Key (id_peca) REFERENCES peca(id_peca),
    Foreign Key (id_pessoa) REFERENCES pessoa(id_pessoa)
);