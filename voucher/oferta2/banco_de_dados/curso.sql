use sprint;

CREATE Table curso (
    id_curso INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    sigla CHAR(3),
    coordenador VARCHAR(50)
);

INSERT INTO curso (nome, sigla, coordenador) VALUES
('Engenharia de Software', 'ENS', 'João Silva'),
('Física Aplicada', 'FIP', 'Pedro Lima'),
('Química Industrial', 'QUI', 'Carlos Rocha'),
('Biologia Molecular', 'BIM', 'Lucas Almeida');

SELECT * from curso; -- 1
SELECT coordenador from curso; -- 2
SELECT sigla from curso; -- 3
SELECT * from curso ORDER BY nome; -- 4
SELECT * from curso ORDER BY coordenador DESC; -- 5
SELECT * from curso where nome like 'F%'; -- 6
SELECT * from curso where nome like '%e'; -- 7
SELECT * from curso where nome like '_i%'; -- 8
SELECT * from curso where nome like '%a_'; -- 9
TRUNCATE curso; -- 10


