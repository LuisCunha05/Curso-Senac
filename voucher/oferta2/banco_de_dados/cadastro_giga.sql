create database cadastro;
use cadastro;

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

create table sexo (
	id_sexo int auto_increment primary key,
    sexo varchar(20)
);

create table nacionalidade (
	id_nacionalidade int auto_increment primary key,
    nacionalidade varchar(30)
);

create table raca (
	id_raca int auto_increment primary key,
    raca varchar(30)
);

create table escolaridade (
	id_escolaridade int auto_increment primary key,
    escolaridade varchar(30)
);

create table cliente (
	cpf char(15) primary key,
    nome varchar(100),
    rg char(10) unique,
    id_cidade int,
    id_sexo int,
    id_nacionalidade int,
    fone char(15),
    id_raca int,
    id_escolaridade int,
    foreign key (id_cidade) references cidade(id_cidade),
    foreign key (id_sexo) references sexo(id_sexo),
    foreign key (id_nacionalidade) references nacionalidade(id_nacionalidade),
    foreign key (id_raca) references raca(id_raca),
    foreign key (id_escolaridade) references escolaridade(id_escolaridade)
);

insert into nacionalidade (nacionalidade) values
('Brasileira'),
('Estrangeira');

insert into sexo (sexo) values
('Masculino'),
('Feminino'),
('Outro');

insert into raca (raca) values
('Branco'),
('Negro'),
('Amarelo'),
('Pardo'),
('Indígina');

insert into escolaridade (escolaridade) values
('Educação infantil'),
('Fundamental'),
('Médio'),
('Médio-Incompleto'),
('Graduação'),
('Graduação-Incompleta'),
('Mestrado'),
('Doutorado');

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
('Cruzeiro do Sul',1),     
('Sena Madureira',1),      
('Tarauacá',1),            
('Feijó',1),

-- Alagoas (AL)
('Maceió',2),               
('Arapiraca',2),            
('Palmeira dos Índios',2),  
('São Miguel dos Campos',2),
('Penedo',2), 

-- Amapá (AP)
('Macapá',3),               
('Santana',3),              
('Laranjal do Jari',3),     
('Oiapoque',3),             
('Mazagão',3),              

-- Amazonas (AM)
('Manaus',4),               
('Parintins',4),            
('Itacoatiara',4),          
('Tefé',4),                 
('Coari',4), 

-- Bahia (BA)
('Salvador',5),             
('Feira de Santana',5),     
('Vitória da Conquista',5),
('Camaçari',5),             
('Ilhéus',5),  

-- Ceará (CE)
('Fortaleza',6),            
('Caucaia',6),              
('Maracanaú',6),            
('Sobral',6),               
('Crato',6), 

-- Distrito Federal (DF)
('Brasília',7),             
('Taguatinga',7),           
('Ceilândia',7),            
('Samambaia',7),            
('Planaltina',7),

-- Espírito Santo (ES)
('Vitória',8),             
('Vila Velha',8),          
('Serra',8),               
('Cariacica',8),           
('Linhares',8),

-- Goiás (GO)
('Goiânia',9),              
('Aparecida de Goiânia',9), 
('Anápolis',9),             
('Luziânia',9),             
('Catalão',9),

-- Maranhão (MA)
('São Luís',10),             
('Imperatriz',10),           
('Caxias',10),               
('Timon',10),                
('Bacabal',10),

-- Mato Grosso (MT)
('Cuiabá',11),              
('Várzea Grande',11),       
('Rondonópolis',11),        
('Sinop',11),               
('Tangará da Serra',11),  

-- Mato Grosso do Sul (MS)
('Campo Grande',12),        
('Dourados',12),            
('Três Lagoas',12),         
('Corumbá',12),             
('Ponta Porã',12), 

-- Minas Gerais (MG)
('Belo Horizonte',13),       
('Uberlândia',13),           
('Juiz de Fora',13),         
('Contagem',13),            
('Betim',13), 

-- Pará (PA)
('Belém',14),                
('Ananindeua',14),           
('Santarém',14),             
('Marabá',14),               
('Castanhal',14),            

-- Paraíba (PB)
('João Pessoa',15),         
('Campina Grande',15),      
('Santa Rita',15),          
('Patos',15),               
('Bayeux',15), 

-- Paraná (PR)
('Curitiba',16),             
('Londrina',16),             
('Maringá',16),              
('Ponta Grossa',16),         
('Campo Largo',16), 

-- Pernambuco (PE)
('Recife',17),               
('Olinda',17),               
('Jaboatão dos Guararapes',17),
('Caruaru',17),              
('Paulista',17),             

-- Piauí (PI)
('Teresina',18),             
('Parnaíba',18),             
('Picos',18),                
('Floriano',18),             
('São Raimundo Nonato',18),

-- Rio de Janeiro (RJ)
('Rio de Janeiro',19),       
('Niterói',19),              
('Duque de Caxias',19),      
('São Gonçalo',19),          
('Volta Redonda',19),

-- Rio Grande do Norte (RN)
('Natal',20),                
('Mossoró',20),              
('Caicó',20),                
('Currais Novos',20),        
('Parnamirim',20),              

-- Rio Grande do Sul (RS)
('Porto Alegre',21),         
('Caxias do Sul',21),        
('Pelotas',21),              
('Santa Maria',21),          
('Gravataí',21), 

-- Rondônia (RO)
('Porto Velho',22),          
('Ji-Paraná',22),            
('Humaitá',22),              
('Cacoal',22),               
('Ariquemes',22),            

-- Roraima (RR)
('Boa Vista',23),            
('Rorainópolis',23),         
('Caracaraí',23),            
('Pacaraima',23),            
('São João da Baliza',23),   


-- Santa Catarina (SC)
('Joinville',24),
('Florianópolis',24),
('Blumenau',24),
('São José',24),
('Itajaí',24),
              
-- São Paulo (SP)
('São Paulo',25),            
('Campinas',25),             
('Santos',25),               
('São Bernardo do Campo',25),
('São José dos Campos',25),  

-- Sergipe (SE)
('Aracaju',26),              
('Lagarto',26),             
('Itabaiana',26),           
('Nossa Senhora do Socorro',26),
('São Cristóvão',26),       

-- Tocantins (TO)
('Palmas',27),              
('Araguaína',27),           
('Guaraí',27),              
('Paraíso do Tocantins',27),
('Porto Nacional',27);

-- ALTER TABLE cidade AUTO_INCREMENT = 1;
-- delete from cidade where id_cidade < 300;

INSERT INTO cliente (cpf, nome, rg, id_cidade, id_sexo, id_nacionalidade, fone, id_raca, id_escolaridade) VALUES
('123.456.789-01', 'Ana Silva', '605328041', 12, 1, 1, '(11) 98765-4321', 3, 2),
('234.567.890-12', 'Carlos Oliveira', '338962790', 23, 2, 1, '(21) 97654-3210', 1, 4),
('345.678.901-23', 'Maria Santos', '274481712', 34, 1, 2, '(31) 96543-2109', 2, 5),
('456.789.012-34', 'João Pereira', '016466243', 45, 3, 1, '(41) 95432-1098', 4, 6),
('567.890.123-45', 'Patrícia Costa', '802484849', 56, 2, 2, '(51) 94321-0987', 5, 7),
('678.901.234-56', 'Roberto Lima', '742380159', 67, 1, 1, '(61) 93210-9876', 1, 8),
('789.012.345-67', 'Fernanda Alves', '709208051', 78, 3, 2, '(71) 92109-8765', 3, 1),
('890.123.456-78', 'Ricardo Martins', '136524168', 89, 2, 1, '(81) 91098-7654', 2, 3),
('901.234.567-89', 'Juliana Souza', '198070659', 90, 1, 2, '(91) 90987-6543', 4, 4),
('012.345.678-90', 'Eduardo Ferreira', '335117549', 101, 2, 1, '(11) 89876-5432', 5, 5),
('123.456.789-10', 'Isabela Rocha', '268138165', 112, 3, 2, '(21) 88765-4321', 1, 6),
('234.567.890-21', 'Gustavo Andrade', '446518363', 123, 1, 1, '(31) 87654-3210', 2, 7),
('345.678.901-32', 'Tatiane Lima', '077746230', 94, 3, 2, '(41) 86543-2109', 3, 8),
('456.789.012-43', 'Felipe Cardoso', '526135838', 115, 2, 1, '(51) 85432-1098', 4, 1),
('567.890.123-54', 'Aline Martins', '041326868', 76, 1, 2, '(61) 84321-0987', 5, 2),
('678.901.234-65', 'Marcelo Alves', '924366064', 67, 2, 1, '(71) 83210-9876', 1, 3),
('789.012.345-76', 'Camila Nunes', '390323371', 58, 3, 2, '(81) 82109-8765', 2, 4),
('890.123.456-87', 'Pedro Almeida', '956347792', 89, 1, 1, '(91) 81098-7654', 3, 5),
('901.234.567-98', 'Sofia Lima', '000579129', 20, 2, 2, '(11) 80987-6543', 4, 6),
('012.345.678-09', 'Lucas Costa', '706867486', 41, 3, 1, '(21) 79876-5432', 5, 7);

describe cliente;

select cliente.nome,cidade.cidade from cliente join cidade on cliente.id_cidade = cidade.id_cidade; -- 1

select cliente.nome,estado.estado from cliente join cidade on cliente.id_cidade = cidade.id_cidade join estado on cidade.id_estado = estado.id_estado; -- 2

select cliente.nome,cliente.cpf,raca.raca from cliente join raca on cliente.id_raca = raca.id_raca; -- 3

select cliente.nome,nacionalidade.nacionalidade from cliente join nacionalidade on cliente.id_nacionalidade = nacionalidade.id_nacionalidade; -- 4

select cliente.nome,escolaridade.escolaridade from cliente join escolaridade on cliente.id_escolaridade = escolaridade.id_escolaridade; -- 5

select cliente.nome,cidade.cidade,estado.estado from cliente join cidade on cliente.id_cidade = cidade.id_cidade join estado on cidade.id_estado = estado.id_estado; -- 6

select cliente.nome,cidade.cidade,estado.estado,cliente.fone,cliente.rg,sexo.sexo,nacionalidade.nacionalidade,raca.raca,escolaridade.escolaridade from cliente
	join cidade on cliente.id_cidade = cidade.id_cidade
    join estado on cidade.id_estado = estado.id_estado
    join sexo on cliente.id_sexo = sexo.id_sexo
    join nacionalidade on cliente.id_nacionalidade = nacionalidade.id_nacionalidade
    join raca on cliente.id_raca = raca.id_raca
    join escolaridade on cliente.id_escolaridade = escolaridade.id_escolaridade;
