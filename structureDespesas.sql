CREATE DATABASE dados_trimestrais;
USE dados_trimestrais;

    -- Criar a tabela com base nos arquivos CSV
CREATE TABLE despesas_saude (
    data DATE,
    reg_ans INT,
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    vl_saldo_inicial DECIMAL(18,2),
    vl_saldo_final DECIMAL(18,2),
    ano INT,
    trimestre INT
);
  