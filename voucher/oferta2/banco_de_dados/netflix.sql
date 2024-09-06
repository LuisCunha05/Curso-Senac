create table filme (film_id int primary key auto_increment, film_titulo varchar(100) not null, film_ano_prod smallint not null,
film_duracao smallint not null, film_sinopse varchar(500) not null);
 
 create table cliente (cliente_id int primary key auto_increment, cliente_email varchar(50) unique not null, cliente_senha varchar(70) not null,
 cliente_nome varchar(50) not null, cliente_telefone varchar(30), cliente_cpf varchar(20) unique not null, cliente_endereco varchar(100),
 cliente_cartao varchar(20) not null, cliente_estado_conta tinyint, cliente_conta_pendente bool);
 
 create table estado_conta (estado_conta_id tinyint auto_increment primary key, estado_conta_valor varchar(20));
 
 insert into estado_conta (estado_conta_valor) values 
 ("ativo"),
 ("suspenso"),
 ("inativo"),
 ("banido");
 
 alter table cliente add foreign key (cliente_estado_conta) references estado_conta(estado_conta_id);
 
create table tipo_video(tipo_v_id tinyint auto_increment primary key, tipo_v_valor varchar(20) not null);
insert into tipo_video (tipo_v_valor) values 
 ("filme"),
 ("série"),
 ("documentário");
 
 create table pais (pais_id smallint primary key auto_increment, pais_nome varchar(50) not null);
 
 create table cidade (cidade_id int primary key auto_increment, cidade_nome varchar(50) not null,
 cidade_pais_id smallint, foreign key (cidade_pais_id) references pais(pais_id));
 
 create table ator ( ator_id int primary key auto_increment, ator_nome varchar(50) not null, ator_data_nasc date,
 ator_cidade_id int, foreign key (ator_cidade_id) references cidade(cidade_id));
 
 create table serie (serie_id int primary key auto_increment, serie_nome varchar(100) not null, serie_ano_inicio smallint not null,
 serie_sinopse varchar(500) not null);
 
 create table documentario (doc_id int primary key auto_increment, doc_titulo varchar(100) not null, doc_duracao smallint,
 doc_ano smallint, doc_produtora varchar(100) not null, doc_sinopse varchar(500) not null);
 
 create table assistido (assist_id int primary key auto_increment, assist_cliente_id int, assist_avaliacao varchar(500), assist_tipo_v tinyint not null, assist_conteudo_id int,
 foreign key (assist_cliente_id) references cliente(cliente_id), foreign key (assist_tipo_v) references tipo_video(tipo_v_id));

 create table serie_ep (ep_id int primary key auto_increment, ep_titulo varchar(100) not null, ep_ano smallint not null,
 ep_duracao smallint not null, ep_temporada smallint not null, ep_numero smallint not null, ep_sinopse varchar(500),
 ep_serie_id int not null, foreign key (ep_serie_id) references serie(serie_id));
 
 create table part_ator (part_id int primary key auto_increment, part_ator_id int not null, part_tipo_v tinyint not null,
 part_content_id int not null, foreign key (part_ator_id) references ator(ator_id));