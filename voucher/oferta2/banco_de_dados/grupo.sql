create database grupo;
use grupo;

CREATE TABLE `tabela_de_preco` (
  `idtabela_preco` int NOT NULL AUTO_INCREMENT,
  `tabela_preco` varchar(255) NOT NULL,
  PRIMARY KEY (`idtabela_preco`)
);
CREATE TABLE `sit_do_cadastro` (
  `id_sit_cad` int NOT NULL AUTO_INCREMENT,
  `sit_cad` varchar(255) NOT NULL,
  PRIMARY KEY (`id_sit_cad`)
);
CREATE TABLE `sexo` (
  `idsexo` int NOT NULL AUTO_INCREMENT,
  `sexualidade` varchar(55) NOT NULL,
  PRIMARY KEY (`idsexo`)
);
CREATE TABLE `regime_tributação` (
  `idrgtri` int NOT NULL AUTO_INCREMENT,
  `regime_tributação` varchar(55) NOT NULL,
  PRIMARY KEY (`idrgtri`)
);
CREATE TABLE `modelo_frete_padrao` (
  `idmod_frete` int NOT NULL AUTO_INCREMENT,
  `modelo_frete` varchar(55) NOT NULL,
  PRIMARY KEY (`idmod_frete`)
);
CREATE TABLE `icms` (
  `idicms` int NOT NULL AUTO_INCREMENT,
  `icms` varchar(55) NOT NULL,
  PRIMARY KEY (`idicms`)
);
