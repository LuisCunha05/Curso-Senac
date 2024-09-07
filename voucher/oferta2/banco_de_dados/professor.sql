use sprint;

CREATE Table professor (
    id_professor int PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    especialidade VARCHAR(40),
    dt_nasc DATE
);

INSERT INTO professor (nome, especialidade, dt_nasc) VALUES
('João Silva', 'Matemática', '1980-04-12'),
('Maria Souza', 'Matemática', '1985-07-23'),
('Pedro Lima', 'Física', '1978-03-15'),
('Ana Pereira', 'Física', '1990-06-10'),
('Carlos Rocha', 'Química', '1975-09-30'),
('Paula Oliveira', 'Química', '1983-12-20'),
('Lucas Almeida', 'Biologia', '1982-11-02'),
('Fernanda Costa', 'Biologia', '1991-05-14');

SELECT * from professor; -- 1
alter Table professor add funcao ENUM('Monitor', 'Assistente','Titular'); -- 2
update professor set funcao= ELT(
    id_professor,
    'Monitor',
    'Assistente',
    'Titular',
    'Assistente',
    'Titular',
    'Assistente',
    'Titular',
    'Monitor'
) where id_professor in (1,2,3,4,5,6,7,8);-- 3
INSERT INTO professor VALUES (NULL, 'Maria Costa', 'História', '1988-06-24', 'Titular'); -- 4
delete FROM professor where id_professor=5; -- 5
SELECT nome from professor where funcao='Titular';-- 6
SELECT especialidade,dt_nasc from professor where funcao='Monitor';-- 7
update professor set dt_nasc='1980-03-15' where id_professor=3;-- 8
TRUNCATE professor;


