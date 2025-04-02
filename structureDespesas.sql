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
  
-- 1º Trimestre de 2023
LOAD DATA LOCAL INFILE 'dados/1T2023.csv'
INTO TABLE despesas_saude
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
  data = STR_TO_DATE(@data, '%Y-%m-%d'),
  reg_ans = @reg_ans,
  cd_conta_contabil = @cd_conta_contabil,
  descricao = @descricao,
  vl_saldo_inicial = @vl_saldo_inicial,
  vl_saldo_final = @vl_saldo_final,
  ano = 2023,
  trimestre = 1;
  
-- 2º Trimestre de 2023
LOAD DATA LOCAL INFILE 'dados/2t2023.csv'
INTO TABLE despesas_saude
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
  data = STR_TO_DATE(@data, '%Y-%m-%d'),
  reg_ans = @reg_ans,
  cd_conta_contabil = @cd_conta_contabil,
  descricao = @descricao,
  vl_saldo_inicial = @vl_saldo_inicial,
  vl_saldo_final = @vl_saldo_final,
  ano = 2023,
  trimestre = 2;

-- 3º Trimestre de 2023
LOAD DATA LOCAL INFILE 'dados/3T2023.csv'
INTO TABLE despesas_saude
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
  data = STR_TO_DATE(@data, '%Y-%m-%d'),
  reg_ans = @reg_ans,
  cd_conta_contabil = @cd_conta_contabil,
  descricao = @descricao,
  vl_saldo_inicial = @vl_saldo_inicial,
  vl_saldo_final = @vl_saldo_final,
  ano = 2023,
  trimestre = 3;
  
-- 4º Trimestre de 2023
LOAD DATA LOCAL INFILE 'dados/4T2023.csv'
INTO TABLE despesas_saude
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
  data = STR_TO_DATE(@data, '%Y-%m-%d'),
  reg_ans = @reg_ans,
  cd_conta_contabil = @cd_conta_contabil,
  descricao = @descricao,
  vl_saldo_inicial = @vl_saldo_inicial,
  vl_saldo_final = @vl_saldo_final,
  ano = 2023,
  trimestre = 4;
    
    
-- 1º Trimestre de 2024
LOAD DATA LOCAL INFILE 'dados/1T2024.csv'
INTO TABLE despesas_saude
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
  data = STR_TO_DATE(@data, '%Y-%m-%d'),
  reg_ans = @reg_ans,
  cd_conta_contabil = @cd_conta_contabil,
  descricao = @descricao,
  vl_saldo_inicial = @vl_saldo_inicial,
  vl_saldo_final = @vl_saldo_final,
  ano = 2024,
  trimestre = 1;
  -- pra cada ano e trimestre 
  
-- 2º Trimestre de 2024
LOAD DATA LOCAL INFILE 'dados/2t2024.csv'
INTO TABLE despesas_saude
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
  data = STR_TO_DATE(@data, '%Y-%m-%d'),
  reg_ans = @reg_ans,
  cd_conta_contabil = @cd_conta_contabil,
  descricao = @descricao,
  vl_saldo_inicial = @vl_saldo_inicial,
  vl_saldo_final = @vl_saldo_final,
  ano = 2024,
  trimestre = 2;

-- 3º Trimestre de 2024
LOAD DATA LOCAL INFILE 'dados/3T2024.csv'
INTO TABLE despesas_saude
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
  data = STR_TO_DATE(@data, '%Y-%m-%d'),
  reg_ans = @reg_ans,
  cd_conta_contabil = @cd_conta_contabil,
  descricao = @descricao,
  vl_saldo_inicial = @vl_saldo_inicial,
  vl_saldo_final = @vl_saldo_final,
  ano = 2024,
  trimestre = 3;
  
-- 4º Trimestre de 2024
LOAD DATA LOCAL INFILE 'dados/4T2024.csv'
INTO TABLE despesas_saude
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
  data = STR_TO_DATE(@data, '%Y-%m-%d'),
  reg_ans = @reg_ans,
  cd_conta_contabil = @cd_conta_contabil,
  descricao = @descricao,
  vl_saldo_inicial = @vl_saldo_inicial,
  vl_saldo_final = @vl_saldo_final,
  ano = 2024,
  trimestre = 4;
  