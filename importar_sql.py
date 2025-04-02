import os
from dotenv import load_dotenv

load_dotenv()

path = os.getenv('CSV_1T2023')
if path:
    print(f"""
LOAD DATA LOCAL INFILE '{path}'
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
""")

path = os.getenv('CSV_2T2023')
if path:
    print(f"""
LOAD DATA LOCAL INFILE '{path}'
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
""")

path = os.getenv('CSV_3T2023')
if path:
    print(f"""
LOAD DATA LOCAL INFILE '{path}'
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
""")

path = os.getenv('CSV_4T2023')
if path:
    print(f"""
LOAD DATA LOCAL INFILE '{path}'
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
""")

path = os.getenv('CSV_1T2024')
if path:
    print(f"""
LOAD DATA LOCAL INFILE '{path}'
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
""")

path = os.getenv('CSV_2T2024')
if path:
    print(f"""
LOAD DATA LOCAL INFILE '{path}'
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
""")

path = os.getenv('CSV_3T2024')
if path:
    print(f"""
LOAD DATA LOCAL INFILE '{path}'
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
""")

path = os.getenv('CSV_4T2024')
if path:
    print(f"""
LOAD DATA LOCAL INFILE '{path}'
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
""")
