use grupo;
describe cadastro_cliente;
describe icms;
describe modelo_frete_padrao;
describe nota_fiscal;
describe ordem_serv;
describe peca;
describe regime_tributação;
describe sexo;
describe sit_do_cadastro;
describe status_peca;
describe tabela_de_preco;
describe vendedor;

SELECT * from cadastro_cliente;
SELECT * from icms;
SELECT * from modelo_frete_padrao;
SELECT * from nota_fiscal;
SELECT * from ordem_serv;
SELECT * from peca;
SELECT * from regime_tributação;
SELECT * from sexo;
SELECT * from sit_do_cadastro;
SELECT * from status_peca;
SELECT * from tabela_de_preco;
SELECT * from vendedor;

RENAME TABLE pecas to peca;
RENAME TABLE cadastro_clientes to cadastro_cliente;
RENAME TABLE stats to status_peca;

ALTER TABLE cadastro_cliente RENAME COLUMN idsexo to id_sexo;
