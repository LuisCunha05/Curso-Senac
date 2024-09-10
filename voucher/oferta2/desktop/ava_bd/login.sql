-- Active: 1725663609565@@127.0.0.1@3306@sprint

use login;

create table usuario (
    id_user int PRIMARY key AUTO_INCREMENT,
    login_user VARCHAR(40) UNIQUE,
    senha VARCHAR(100),
    texto tinytext
);

INSERT into usuario VALUES 
(null, 'luis', 'senha321', 'Super texto interessante!');

INSERT into usuario VALUES 
(null, 'doido', SHA2('senha321', 256), 'Super texto!');

select IF((SELECT senha from usuario where id_user=2) = SHA2('senh321', 256), 1, 0);
-- SELECT SHA2('senha', 256) from usuario;

SELECT * from usuario;