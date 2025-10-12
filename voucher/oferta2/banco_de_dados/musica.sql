create database sprint;
use sprint;

create table musica (
	id_musica int primary key auto_increment,
    titulo varchar(40),
    artista varchar(40),
    genero varchar(40)
);

INSERT INTO musica (titulo, artista, genero) VALUES
('Bad Guy', 'Billie Eilish', 'Pop'),
('Ocean Eyes', 'Billie Eilish', 'Pop'),
('When the Party\'s Over', 'Billie Eilish', 'Pop'),
('Everything I Wanted', 'Billie Eilish', 'Pop'),
('Garota de Ipanema', 'Tom Jobim', 'Bossa Nova'),
('Aquarela', 'Toquinho', 'MPB'),
('Tropicália', 'Caetano Veloso', 'Tropicalia'),
('Mas, que Nada!', 'Jorge Ben Jor', 'Samba');

select * from musica; -- a
alter table musica add curtidas int;-- b
update musica set curtidas = (floor(rand() * 99));-- c
alter table musica modify column artista varchar(80);-- d
update musica set curtidas = 3000 where id_musica = 1;-- e
update musica set curtidas = 2999 where id_musica between 2 and 3;-- f
update musica set titulo = 'Saudade do Brazil' where id_musica = 5;-- g
delete from musica where id_musica = 4;-- h
select * from musica where genero != 'Funk'; -- i
select * from musica where curtidas >= 20; -- j
describe musica;-- k
truncate musica; -- l



