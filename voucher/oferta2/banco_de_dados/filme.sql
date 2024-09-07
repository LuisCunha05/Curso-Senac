create database sprint;
use sprint;

create table filme (
    id_filme int primary key auto_increment,
    titulo varchar(50),
    genero varchar(40),
    diretor varchar(40)
);

-- Inserir filmes do gênero Ação
INSERT INTO filme (titulo, genero, diretor) VALUES
('Mad Max: Estrada da Fúria', 'Ação', 'George Miller'),
('John Wick', 'Ação', 'Chad Stahelski'),
('Superbad', 'Comédia', 'Greg Mottola'),
('A Morte do Demônio', 'Comédia', 'Sam Raimi'),
('A Lista de Schindler', 'Drama', 'Steven Spielberg'),
('O Poderoso Chefão', 'Drama', 'Francis Ford Coppola'),
('Blade Runner 2049', 'Ficção Científica', 'Denis Villeneuve'),
('Inception', 'Ficção Científica', 'Christopher Nolan'),
('O Exorcista', 'Terror', 'William Friedkin'),
('Hereditário', 'Terror', 'Ari Aster');

SELECT * from filme;-- 1
alter Table filme ADD protagonista VARCHAR(50);-- 2
UPDATE filme set protagonista = ELT(
    id_filme,
    'Max e Furiosa',
    'John Wick',
    'Seth e Evan',
    'Mia Allen',
    'Ash', 'Oskar Schindler',
    'Michael Corleone',
    'K', 'Dom Cobb',
    'Regan e Padre Damien',
    'Annie Graham'
) where id_filme in (1,2,3,4,5,6,7,8,9,10);-- 3

alter Table filme MODIFY COLUMN diretor VARCHAR(150);-- 4
UPDATE filme SET diretor='Stevão Rei' where id_filme=5;-- 5
update filme set diretor='Some Dude' where id_filme=2 or id_filme=7;-- 7
update filme set titulo='O Poderoso Chefinho' where id_filme=6; --8
DELETE FROM filme where id_filme=3;-- 9
SELECT * FROM filme WHERE genero != 'Drama'; -- 10
SELECT * FROM filme WHERE genero = 'Suspense'; -- 11
DESCRIBE filme;

TRUNCATE filme;