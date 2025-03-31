-- criando o banco de dados
CREATE DATABASE dados_relatorio;
USE dados_relatorio;

    -- Criar a tabela com base no arquivo Relatorio_cadop.csv
CREATE TABLE operadoras (
	registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(14),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero VARCHAR(8),
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_de_comercializacao INT,
    data_registro_ans DATE
);

-- Importando os dados do arquivo CSV 
-- O caminho do arquivo deve ser alterado para o local correto no seu sistema
LOAD DATA LOCAL INFILE 'D:/Downloads/Relatorio_cadop.csv'
INTO TABLE operadoras
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero,
 complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico,
 representante, cargo_representante, regiao_de_comercializacao, data_registro_ans);
