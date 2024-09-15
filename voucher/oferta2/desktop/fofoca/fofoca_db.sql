CREATE DATABASE fofoca;

use fofoca;

CREATE TABLE user_type(
    id_user_type int PRIMARY KEY AUTO_INCREMENT,
    user_type VARCHAR(20)
);

create table usuario (
    id_user int PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(30),
    passw VARCHAR(70),
    id_user_type int,
    Foreign Key (id_user_type) REFERENCES user_type(id_user_type)
);

CREATE Table fofoca (
    id_fofoca INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    texto TEXT not NULL,
    ponto TINYINT not NULL,
    image1 VARCHAR(200),
    image2 VARCHAR(200),
    image3 VARCHAR(200)
);

CREATE Table visualizacao (
    id_view int PRIMARY KEY AUTO_INCREMENT,
    id_fofoca int not NULL,
    id_user int not NULL,
    Foreign Key (id_fofoca) REFERENCES fofoca(id_fofoca),
    Foreign Key (id_user) REFERENCES usuario(id_user)
);

INSERT INTO user_type VALUES 
(NULL, 'admin'),
(NULL, 'famoso'),
(NULL, 'cliente');

INSERT INTO usuario VALUES
(NULL, 'administrador', SHA2('admin123', 256), 1),
(NULL, 'famoso', SHA2('famoso123', 256), 2),
(NULL, 'cliente1', SHA2('senha1', 256), 3);

