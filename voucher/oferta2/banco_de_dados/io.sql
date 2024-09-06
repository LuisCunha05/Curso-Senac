create database escola;
show character set;
show collation where charset='latin1';
use escola;
create table funcionario(cod_func integer);
alter table funcionario add cpf varchar(15);
insert into funcionario (cod_func, cpf) values (001, '123.456.789-11');
create table luis(id int not null, nome varchar(20) not null, idade tinyint not null, ano int default 2024);
insert into luis (id, nome, idade, ano) values (0001, 'luis cunha', 26, 2024);
alter table luis add unique (id);
alter table luis add primary key (id);
describe luis;
alter table luis change id id int auto_increment;
describe luis;
create table corno (id int primary key auto_increment not null, estado varchar(10));
select * from corno;
insert into corno (id, estado) values (0,'NÂO');
select * from luis;
alter table luis add corno int not null default 0;
alter table corno add 

alter table luis drop column corno;
alter table luis add foreign key (corno) references corno(id);






