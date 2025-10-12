use sprint;

create Table revista (
    id_revista INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(40),
    categoria VARCHAR(30)
);

INSERT INTO revista VALUES 
(NULL,'Superinteressante', 'Ciência e Tecnologia'),
(NULL,'Caras', 'Celebridades'),
(NULL,'Exame', 'Negócios'),
(NULL,'Globo Rural', 'Agronegócio');

SELECT * from revista; -- 1
update revista set categoria= (CASE 
    WHEN id_revista=1 THEN 'Ciência e TI'
    WHEN id_revista=2 THEN 'Celebridades e Entreterimento' 
    WHEN id_revista=3 THEN 'Negócios e Economia'
    ELSE categoria
END);
SELECT * from revista; -- 2
INSERT INTO revista VALUES
(NULL, 'Pequenas Empresas & Grandes Negócios', 'Empreendedorismo'),
(NULL, 'Saúde', 'Bem-estar e Saúde'),
(NULL, 'Mundo Estranho', 'Curiosidades e Cultura Pop'); -- 3
SELECT * from revista; -- 4
DESCRIBE revista; -- 5
ALTER TABLE revista MODIFY COLUMN categoria VARCHAR(70); -- 6
DESCRIBE revista; -- 7
ALTER TABLE revista ADD periodicidade VARCHAR(15); -- 8
SELECT * FROM revista; -- 9
ALTER TABLE revista DROP COLUMN periodicidade;
