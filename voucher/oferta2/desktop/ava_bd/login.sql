-- Active: 1725968277993@@10.28.2.34@3306@login

use login;

create table usuario (
    id_user int PRIMARY key AUTO_INCREMENT,
    login_user VARCHAR(40) UNIQUE,
    senha VARCHAR(100),
    texto tinytext
);

INSERT into usuario VALUES 
(null, 'luiscunha05', 'senhaboa123', 'Super texto interessante!');

INSERT into usuario VALUES 
(null, 'user2doido', SHA2('senha321', 256), 'Super texto!');

select IF((SELECT senha from usuario where id_user=2) = SHA2('senh321', 256), 1, 0);
-- SELECT SHA2('senha', 256) from usuario;