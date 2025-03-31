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

