-- Active: 1725968277993@@10.28.2.34@3306@login

use login;

create table usuario (
    id_user int PRIMARY key AUTO_INCREMENT,
    login_user VARCHAR(40) UNIQUE,
    senha VARCHAR(100),
    color CHAR(7),
    texto tinytext,
    img MEDIUMBLOB
);

INSERT into usuario VALUES 
(null, 'luis1', SHA2('senha123', 256), '#ffa500', 'Opa Opa!', NULL),
(null, 'user1', SHA2('senha1', 256), '#843c54', 'Super texto 1!', NULL),
(null, 'user2', SHA2('senha2', 256), '#03989e', 'Super texto 2!', NULL),
(null, 'user3', SHA2('senha3', 256), '#5d782e', 'Super texto 3!', NULL),
(null, 'user4', SHA2('senha4', 256), '#a14242', 'Super texto 4!', NULL);

-- select IF((SELECT senha from usuario where id_user=2) = SHA2('senh321', 256), 1, 0);
SELECT * from usuario;