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

-- Inserir dados na tabela cidade
INSERT INTO cidade (nome_cidade) VALUES ('São Paulo');
INSERT INTO cidade (nome_cidade) VALUES ('Rio de Janeiro');
INSERT INTO cidade (nome_cidade) VALUES ('Belo Horizonte');

-- Inserir dados na tabela endereco
INSERT INTO endereco (id_cidade, bairro, rua, numero) VALUES (1, 'Jardins', 'Avenida Paulista', 1578);
INSERT INTO endereco (id_cidade, bairro, rua, numero) VALUES (2, 'Copacabana', 'Avenida Atlântica', 2000);
INSERT INTO endereco (id_cidade, bairro, rua, numero) VALUES (3, 'Savassi', 'Rua Antônio de Albuquerque', 300);

-- Inserir dados na tabela raca
INSERT INTO raca (tipo) VALUES ('Labrador');
INSERT INTO raca (tipo) VALUES ('Poodle');
INSERT INTO raca (tipo) VALUES ('Bulldog');

-- Inserir dados na tabela perfil
INSERT INTO perfil (id_raca, idade, tipo_sangue) VALUES (1, 5, 'A+');
INSERT INTO perfil (id_raca, idade, tipo_sangue) VALUES (2, 3, 'B-');
INSERT INTO perfil (id_raca, idade, tipo_sangue) VALUES (3, 4, 'O+');

-- Inserir dados na tabela status_icms
INSERT INTO status_icms (tipo) VALUES ('Aprovado');
INSERT INTO status_icms (tipo) VALUES ('Pendente');
INSERT INTO status_icms (tipo) VALUES ('Rejeitado');

-- Inserir dados na tabela reg_tributacao
INSERT INTO reg_tributacao (tipo) VALUES ('Simples Nacional');
INSERT INTO reg_tributacao (tipo) VALUES ('Lucro Presumido');
INSERT INTO reg_tributacao (tipo) VALUES ('Lucro Real');

-- Inserir dados na tabela contato
INSERT INTO contato (numero, whatsapp, fax, instagram, email) VALUES ('123456789', '987654321', '555-0001', '@exemplo', 'contato@exemplo.com');
INSERT INTO contato (numero, whatsapp, fax, instagram, email) VALUES ('234567890', '876543210', '555-0002', '@outra', 'outra@exemplo.com');

-- Inserir dados na tabela vendedor
INSERT INTO vendedor (nome, telefone, cnpj, email) VALUES ('João da Silva', '11-98765-4321', '12.345.678/0001-90', 'joao.silva@vendas.com');
INSERT INTO vendedor (nome, telefone, cnpj, email) VALUES ('Maria Oliveira', '21-99876-5432', '23.456.789/0001-01', 'maria.oliveira@vendas.com');

-- Inserir dados na tabela extra
INSERT INTO extra (cor_favorita, altura, tamanho_pe) VALUES ('Azul', 1.75, 40.0);
INSERT INTO extra (cor_favorita, altura, tamanho_pe) VALUES ('Verde', 1.68, 38.0);

-- Inserir dados na tabela sexo
INSERT INTO sexo (tipo) VALUES ('Masculino');
INSERT INTO sexo (tipo) VALUES ('Feminino');
INSERT INTO sexo (tipo) VALUES ('Não-binário');

-- Inserir dados na tabela frete_padrao
INSERT INTO frete_padrao (tipo) VALUES ('Sedex');
INSERT INTO frete_padrao (tipo) VALUES ('PAC');
INSERT INTO frete_padrao (tipo) VALUES ('Frete Grátis');

-- Inserir dados na tabela tabela_de_preco
INSERT INTO tabela_de_preco (tipo) VALUES ('Atacado');
INSERT INTO tabela_de_preco (tipo) VALUES ('Varejo');
INSERT INTO tabela_de_preco (tipo) VALUES ('Promocional');

-- Inserir dados na tabela status_cadastro
INSERT INTO status_cadastro (tipo) VALUES ('Ativo');
INSERT INTO status_cadastro (tipo) VALUES ('Inativo');
INSERT INTO status_cadastro (tipo) VALUES ('Pendente');

-- Inserir dados na tabela dados_adicionais
INSERT INTO dados_adicionais (status_civil, tem_filho, id_endereco) VALUES ('Solteiro', 'n', 1);
INSERT INTO dados_adicionais (status_civil, tem_filho, id_endereco) VALUES ('Casado', 's', 2);
INSERT INTO dados_adicionais (status_civil, tem_filho, id_endereco) VALUES ('Divorciado', 'n', 3);

-- Inserir dados na tabela clientes_relacionados
INSERT INTO clientes_relacionados (data_criancao, id_outra_pessoa) VALUES ('2024-01-15', 1);
INSERT INTO clientes_relacionados (data_criancao, id_outra_pessoa) VALUES ('2024-02-20', 2);
INSERT INTO clientes_relacionados (data_criancao, id_outra_pessoa) VALUES ('2024-03-10', 3);

-- Inserir dados na tabela financeiro
INSERT INTO financeiro (conta, banco, operacao) VALUES ('123456-7', 'Banco do Brasil', 'Crédito');
INSERT INTO financeiro (conta, banco, operacao) VALUES ('234567-8', 'Bradesco', 'Débito');
INSERT INTO financeiro (conta, banco, operacao) VALUES ('345678-9', 'Itaú', 'Transferência');

-- Inserir dados na tabela tipo_user
INSERT INTO tipo_user (tipo) VALUES ('Administrador');
INSERT INTO tipo_user (tipo) VALUES ('Usuário');
INSERT INTO tipo_user (tipo) VALUES ('Gerente');

-- Inserir dados na tabela login_usr
INSERT INTO login_usr (id_tipo_user, email, senha) VALUES (1, 'admin@exemplo.com', 'senhaAdmin123');
INSERT INTO login_usr (id_tipo_user, email, senha) VALUES (2, 'usuario@exemplo.com', 'senhaUsuario456');
INSERT INTO login_usr (id_tipo_user, email, senha) VALUES (3, 'gerente@exemplo.com', 'senhaGerente789');

-- Inserir dados na tabela peca
INSERT INTO peca (ci, ordem, codigo, status_, custo_unitario, custo_total, variante, descricao, qtd_base, qtd, qt_fix_variavel) 
VALUES ('CI001', 'Ordem1', 'C1234', 'Novo', 150.00, 1500.00, 'Variante1', 'Descrição da peça 1', 10, 20, 5);
INSERT INTO peca (ci, ordem, codigo, status_, custo_unitario, custo_total, variante, descricao, qtd_base, qtd, qt_fix_variavel) 
VALUES ('CI002', 'Ordem2', 'C5678', 'Usado', 100.00, 1000.00, 'Variante2', 'Descrição da peça 2', 15, 30, 10);
INSERT INTO peca (ci, ordem, codigo, status_, custo_unitario, custo_total, variante, descricao, qtd_base, qtd, qt_fix_variavel) 
VALUES ('CI003', 'Ordem3', 'C6666', 'Novo', 45.00, 500.00, 'Variante1', 'Descrição da peça 3', 25, 50, 15);

-- Inserir dados na tabela nota_fiscal
INSERT INTO nota_fiscal (id_tabela_de_preco, id_vendedor, desconto, frete, aprovacao_cliente, hora_aprovacao, data_previsao, data_vencimento) 
VALUES (1, 1, 50.00, 20.00, 'Aprovado', '14:30:00', '2024-09-20', '2024-09-30');
INSERT INTO nota_fiscal (id_tabela_de_preco, id_vendedor, desconto, frete, aprovacao_cliente, hora_aprovacao, data_previsao, data_vencimento) 
VALUES (2, 2, 30.00, 15.00, 'Pendente', '10:00:00', '2024-09-25', '2024-10-05');

-- Inserir dados na tabela produtos_nf
INSERT INTO produtos_nf (id_nf, id_peca, quantidade) VALUES (1, 1, 5);
INSERT INTO produtos_nf (id_nf, id_peca, quantidade) VALUES (1, 2, 10);
INSERT INTO produtos_nf (id_nf, id_peca, quantidade) VALUES (2, 1, 3);

INSERT INTO pessoa (
    nome, ramal, rg, email, email_loja_virtual,
    email_danf, email_comercial, email_cobranca,
    inscricao_estadual, telefone_comercial, telefone_celular, cpf, transportadora1, transportadora2,
    inscricao_sufra, linha_pef, cnpj, imagem, data_nascimento,
    carga_tributaria, aliquota,
    id_sexo, id_tabela_de_preco, id_frete_padrao,
    id_status_cadastro, id_status, id_reg_tributacao,
    id_dados_adicionais, id_endereco, id_perfil,
    id_contato, id_vendedor, id_extra,
    id_financeiro, id_clientes_relacionados, fornecedor
) VALUES
(
    'Ana Souza', '1234', '12.345.678', 'ana.souza@example.com', 'loja.ana@example.com',
    'danf.ana@example.com', 'comercial.ana@example.com', 'cobranca.ana@example.com',
    '12345678', '(11) 1234-5678', '(11) 98765-4321', '123.456.789-00', 'TransLog', 'FastTrans',
    '1234-56', 'Linha PEF 1', '12.345.678/0001-99', 'imagem_ana.jpg', '1980-05-15',
    18.5, 12.0,
    1, 1, 1,
    1, 1, 1,
    1, 1, 1,
    1, 1, 1,
    1, 1, 's'
),
(
    'Pedro Oliveira', '5678', '87.654.321', 'pedro.oliveira@example.com', 'loja.pedro@example.com',
    'danf.pedro@example.com', 'comercial.pedro@example.com', 'cobranca.pedro@example.com',
    '87654321', '(21) 2345-6789', '(21) 91234-5678', '987.654.321-00', 'LogTrans', 'SpeedTrans',
    '5678-90', 'Linha PEF 2', '98.765.432/0001-88', 'imagem_pedro.jpg', '1990-08-20',
    15.0, 10.0,
    2, 2, 2,
    2, 2, 2,
    2, 2, 2,
    2, 2, 2,
    2, 2, 'n'
),
(
    'Maria Costa', '9101', '23.456.789', 'maria.costa@example.com', 'loja.maria@example.com',
    'danf.maria@example.com', 'comercial.maria@example.com', 'cobranca.maria@example.com',
    '34567890', '(31) 3456-7890', '(31) 93456-7890', '345.678.901-00', 'TransWorld', 'QuickTrans',
    '9101-23', 'Linha PEF 3', '34.567.890/0001-77', 'imagem_maria.jpg', '1975-12-10',
    20.0, 15.0,
    3, 3, 3,
    3, 3, 3,
    3, 3, 3,
    3, 3, 3,
    3, 3, 's'
);

INSERT INTO ordem_servico (
    id_nf, id_peca, id_pessoa, execucao, servico, data_emissao
) VALUES
(
    1, 1, 1, 'Executado', 'Reparação', '2024-09-01'
),
(
    2, 2, 2, 'Pendente', 'Manutenção', '2024-09-05'
),
(
    3, 3, 3, 'Executado', 'Instalação', '2024-09-10'
);

