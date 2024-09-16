create database Atividade_BD;
use Atividade_BD;



CREATE TABLE regime_tributação(
    idrgtri int primary key auto_increment,
    regime_tributação varchar(55) not null
);

CREATE TABLE icms(
    idicms int auto_increment primary key,
    icms varchar(55) not NULL
);


CREATE TABLE sexo(
    idsexo int primary key auto_increment,
    sexualidade varchar(55) NOT NULL);

CREATE TABLE modelo_frete_padrao(
    idmod_frete int primary key auto_increment,
    modelo_frete varchar(55) not null
);

CREATE TABLE tabela_de_preco(
    idtabela_preco int primary key auto_increment,
    tabela_preco varchar(255) not null
);

CREATE TABLE sit_do_cadastro(
    id_sit_cad int primary key auto_increment,
    sit_cad varchar(255) not null
);


CREATE TABLE cadastro_clientes(
    nome_cliente varchar(255) not null,
    idsexo int,
    idrgtri int,
    email varchar(255)not null,
    email_danfe varchar(255) not null,
    email_cobrança varchar(255) not null,
    email_lojavirtual varchar(255) not null,
    telefone_comercial varchar(15),
    telefone_residencial varchar(15),
    ramal int(4),
    telefone_cell varchar(15)not null,
    fax int,
    cpf varchar(11) not null primary key,
    rg int(7) not null, -- precisa ser unique
    insc_estadual int not null,
    insc_suframa int not null,
    data_nasc date not null,
    transportadora varchar(255) not null,
    transportadora_2 varchar(255),
    linha_pef varchar(255),
    alquota decimal not null,
    idmod_frete int,
    idtabela_preco int,
    id_sit_cad int,
    idicms int,

    Foreign key (idsexo) REFERENCES sexo(idsexo),
    Foreign key (idrgtri) REFERENCES regime_tributação(idrgtri),
    Foreign key (idicms) REFERENCES icms(idicms),
    Foreign key (idmod_frete) REFERENCES modelo_frete_padrao(idmod_frete),
    Foreign key (idtabela_preco) REFERENCES tabela_de_preco(idtabela_preco),
    Foreign key (id_sit_cad) REFERENCES sit_do_cadastro (id_sit_cad)

);

CREATE TABLE vendedor(
    idrgtri int,
    razao_social varchar(255) not null,
    nome_vendedor varchar(255) not null,
    email varchar(255)not null,
    email_danfe varchar(255) not null,
    email_cobrança varchar(255) not null,
    email_lojavirtual varchar(255) not null,
    telefone_comercial varchar(15),
    telefone_residencial varchar(15),
    ramal int(4),
    telefone_cell varchar(15)not null,
    fax int,
    cnpj varchar(55) not null, -- Precisa ser Unique, sem PK
    insc_estadual int not null,
    insc_suframa int not null,
    transportadora varchar(255) not null,
    transportadora_2 varchar(255),
    linha_pef varchar(255),
    alquota decimal not null,
    idmod_frete int,
    idtabela_preco int,
    id_sit_cad int,
    idicms int,

    Foreign key (idrgtri) REFERENCES regime_tributação(idrgtri),
    Foreign key (idicms) REFERENCES icms(idicms),
    Foreign key (idmod_frete) REFERENCES modelo_frete_padrao(idmod_frete),
    Foreign key (idtabela_preco) REFERENCES tabela_de_preco(idtabela_preco),
    Foreign key (id_sit_cad) REFERENCES sit_do_cadastro (id_sit_cad)
);



CREATE TABLE stats(
    id_status int auto_increment primary key,
    status varchar(55) not null
);


create table pecas(
cod_peca int primary key auto_increment,
descricao varchar (250), -- Not null
variante varchar(250),
p_s int,
qtd_base int,
qtde int,
UM int,
custo_unitario int,
custo_total int, -- not null
qtd_fix_var int,
ordem int,
c_i int,
origem int,
id_status int not null,
Foreign key (id_status) REFERENCES stats(id_status)
);


CREATE TABLE ordem_serv(
    doc int primary key auto_increment,
    emissao date not null,
    cpf varchar(11) not null,
    previsao date,
    descricao varchar(255),
    execucao varchar(55),
    servico varchar(55) not null, -- Sem id peça ou FK
    variante varchar(55),
    quantidade decimal not null,
    valor decimal,
    
    Foreign key (cpf) REFERENCES cadastro_clientes(cpf)
    
);

CREATE TABLE nota_fiscal(
    doc int, -- sem FK
    sequencia int not null,
    emissao date not null,
    vencimento date,
    previsao_fat date,
    aprovacao_cliente date not null,
    hora_aprovacao time not null,
    embarques int,
    prazo_entrega_dias int,
    n_pedido_compra int not null,
    nome_vendedor varchar(55),
    historico text,
    faturamento decimal,
    cpf varchar(11), -- not null
    end_entrega varchar(55),
    idtabela_preco int,
    transportadora int,
    transportadora_2 int,
    idmod_frete int,
    valor_frete decimal,
    valor_desconto_rateado decimal,
    contato varchar(55));