-- Active: 1725663609565@@127.0.0.1@3306@atividade_db
RENAME TABLE pecas to peca;
RENAME TABLE cadastro_clientes to cadastro_cliente;
RENAME TABLE stats to status_peca;
RENAME TABLE tabela_de_preco to tabela_preco;
RENAME TABLE sit_do_cadastro to situacao_cadastro;
ALTER TABLE cadastro_cliente RENAME COLUMN idsexo to id_sexo;

--tributacao
RENAME TABLE regime_tributação to regime_tributacao;
ALTER TABLE regime_tributacao RENAME COLUMN regime_tributação to tipo_tributacao;
ALTER TABLE regime_tributacao RENAME COLUMN idrgtri to id_regime_tribucao;

--icms
ALTER TABLE icms RENAME COLUMN idicms to id_icms;
ALTER TABLE icms RENAME COLUMN icms to tipo_icms;

--Frete
RENAME TABLE modelo_frete_padrao to frete_padrao;
ALTER TABLE frete_padrao RENAME COLUMN idmod_frete to id_frete_padrao;
ALTER TABLE frete_padrao RENAME COLUMN modelo_frete to tipo_frete;

--Tabela preco
ALTER TABLE tabela_preco RENAME COLUMN idtabela_preco to id_tabela_preco;
ALTER TABLE tabela_preco RENAME COLUMN tabela_preco to tipo_preco;

-- Transportadora
CREATE TABLE transportadora (
    id_transportadora INT PRIMARY KEY AUTO_INCREMENT,
    nome_transportadora VARCHAR(100)
);

--Nota fiscal
DESCRIBE nota_fiscal;
ALTER TABLE nota_fiscal RENAME COLUMN doc to documento;
ALTER TABLE nota_fiscal ADD COLUMN id_nota_fiscal INT PRIMARY KEY auto_increment;
ALTER TABLE nota_fiscal RENAME COLUMN emissao to data_emissao;
ALTER TABLE nota_fiscal RENAME COLUMN vencimento to data_vencimento;
ALTER TABLE nota_fiscal RENAME COLUMN previsao_fat to data_prev_faturamento;
ALTER TABLE nota_fiscal RENAME COLUMN aprovacao_cliente to data_aprovacao_cliente;
ALTER TABLE nota_fiscal RENAME COLUMN embarques to embarque;
ALTER TABLE nota_fiscal RENAME COLUMN prazo_entrega_dias to prazo_entrega_dia;
ALTER TABLE nota_fiscal ADD Foreign Key (cpf) REFERENCES cadastro_cliente(cpf);
ALTER TABLE nota_fiscal RENAME COLUMN idtabela_preco to id_tabela_preco;
ALTER TABLE nota_fiscal ADD Foreign Key (id_tabela_preco) REFERENCES tabela_preco(id_tabela_preco);
ALTER TABLE nota_fiscal RENAME COLUMN transportadora to id_transportadora_1;
ALTER TABLE nota_fiscal RENAME COLUMN transportadora_2 to id_transportadora_2;
ALTER TABLE nota_fiscal ADD Foreign Key (id_transportadora_1) REFERENCES transportadora(id_transportadora);
ALTER TABLE nota_fiscal ADD Foreign Key (id_transportadora_2) REFERENCES transportadora(id_transportadora);
ALTER TABLE nota_fiscal RENAME COLUMN idmod_frete to id_frete_padrao;
ALTER TABLE nota_fiscal ADD Foreign Key (id_frete_padrao) REFERENCES frete_padrao(id_frete_padrao);

-- Ordem Servico
RENAME TABLE ordem_serv to ordem_servico;
ALTER TABLE ordem_servico RENAME COLUMN doc to id_ordem_servico;
ALTER TABLE ordem_servico RENAME COLUMN emissao to data_emissao;
--ALTER TABLE ordem_servico ADD Foreign Key (cpf) REFERENCES cadastro_cliente(cpf);
ALTER TABLE ordem_servico RENAME COLUMN previsao to data_previsao;
ALTER TABLE ordem_servico ADD COLUMN id_peca INT;
ALTER TABLE ordem_servico ADD Foreign Key (id_peca) REFERENCES peca(cod_peca);
ALTER TABLE ordem_servico DROP COLUMN descricao;
ALTER TABLE ordem_servico DROP COLUMN variante;

-- ALTER Table ordem_servico DROP CONSTRAINT ordem_servico_ibfk_2;

-- Peca
ALTER TABLE peca RENAME COLUMN cod_peca to id_peca;
ALTER TABLE peca RENAME COLUMN UM to unidade_medida;
-- ALTER TABLE peca DROP CONSTRAINT peca_ibfk_2;
-- ALTER TABLE peca ADD Foreign Key (id_status) REFERENCES status_peca(id_status);

-- Sexo
ALTER TABLE sexo RENAME COLUMN idsexo to id_sexo;
ALTER TABLE sexo RENAME COLUMN sexualidade to tipo_sexo;

--Situacao cadastro
ALTER TABLE situacao_cadastro RENAME COLUMN id_sit_cad to id_situacao_cadastro;
ALTER TABLE situacao_cadastro RENAME COLUMN sit_cad to tipo_situacao_cadastro;

-- Status Peca
ALTER TABLE status_peca RENAME COLUMN id_status to id_status_peca;
ALTER TABLE status_peca RENAME COLUMN status to status_peca;

--Vendedor
ALTER TABLE vendedor RENAME COLUMN transportadora to id_transportadora_1;
ALTER TABLE vendedor MODIFY COLUMN id_transportadora_1 INT;
ALTER TABLE vendedor ADD Foreign Key (id_transportadora_1) REFERENCES transportadora(id_transportadora);
ALTER TABLE vendedor RENAME COLUMN transportadora_2 to id_transportadora_2;
ALTER TABLE vendedor MODIFY COLUMN id_transportadora_2 INT;
ALTER TABLE vendedor ADD Foreign Key (id_transportadora_2) REFERENCES transportadora(id_transportadora);
ALTER TABLE vendedor RENAME COLUMN idmod_frete to id_frete_padrao;
ALTER TABLE vendedor RENAME COLUMN idtabela_preco to id_tabela_preco;
ALTER TABLE vendedor RENAME COLUMN id_sit_cad to id_situacao_cadastro;
ALTER TABLE vendedor RENAME COLUMN idicms to id_icms;
ALTER TABLE vendedor ADD Foreign Key (id_frete_padrao) REFERENCES frete_padrao(id_frete_padrao);
-- ALTER TABLE vendedor ADD Foreign Key (id_tabela_preco) REFERENCES tabela_preco(id_tabela_preco);
-- ALTER TABLE vendedor ADD Foreign Key (id_situacao_cadastro) REFERENCES situacao_cadastro(id_situacao_cadastro);
-- ALTER TABLE vendedor ADD Foreign Key (id_icms) REFERENCES icms(id_icms);
-- ALTER TABLE vendedor DROP CONSTRAINT vendedor_ibfk_9;
-- ALTER TABLE vendedor DROP CONSTRAINT vendedor_ibfk_10;
-- ALTER TABLE vendedor DROP CONSTRAINT vendedor_ibfk_11;

-- Cadastro cliente
ALTER TABLE cadastro_cliente RENAME COLUMN idrgtri to id_regime_tributacao;
ALTER TABLE cadastro_cliente RENAME COLUMN transportadora to id_transportadora_1;
ALTER TABLE cadastro_cliente RENAME COLUMN transportadora_2 to id_transportadora_2;
ALTER TABLE cadastro_cliente RENAME COLUMN idmod_frete to id_frete_padrao;
ALTER TABLE cadastro_cliente RENAME COLUMN idtabela_preco to id_tabela_preco;
ALTER TABLE cadastro_cliente RENAME COLUMN id_sit_cad to id_situacao_cadastro;
ALTER TABLE cadastro_cliente RENAME COLUMN idicms to id_icms;
ALTER TABLE cadastro_cliente MODIFY COLUMN id_transportadora_1 INT;
ALTER TABLE cadastro_cliente MODIFY COLUMN id_transportadora_2 INT;
ALTER TABLE cadastro_cliente ADD Foreign Key (id_transportadora_1) REFERENCES transportadora(id_transportadora);
ALTER TABLE cadastro_cliente ADD Foreign Key (id_transportadora_2) REFERENCES transportadora(id_transportadora);
-- ALTER TABLE cadastro_cliente ADD Foreign Key (id_frete_padrao) REFERENCES frete_padrao(id_frete_padrao);
-- ALTER TABLE cadastro_cliente ADD Foreign Key (id_tabela_preco) REFERENCES tabela_preco(id_tabela_preco);
-- ALTER TABLE cadastro_cliente ADD Foreign Key (id_situacao_cadastro) REFERENCES situacao_cadastro(id_situacao_cadastro);
-- ALTER TABLE cadastro_cliente ADD Foreign Key (id_icms) REFERENCES icms(id_icms);
-- ALTER TABLE cadastro_cliente DROP CONSTRAINT cadastro_cliente_ibfk_9;
-- ALTER TABLE cadastro_cliente DROP CONSTRAINT cadastro_cliente_ibfk_10;
-- ALTER TABLE cadastro_cliente DROP CONSTRAINT cadastro_cliente_ibfk_11;
-- ALTER TABLE cadastro_cliente DROP CONSTRAINT cadastro_cliente_ibfk_12;