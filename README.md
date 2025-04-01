# **Software-Tech, Documentação**

Este projeto tem como objetivo coletar, transformar e disponibilizar dados relacionados às operadoras de planos de saúde e aos seus respectivos gastos com eventos/sinistros, a partir de dados fornecidos pela Agência Nacional de Saúde Suplementar (ANS).

---

## Funcionalidades

- Raspagem de PDFs dos Anexos I e II diretamente do site da ANS
- Extração de tabelas de PDFs e transformação em CSV
- Criação de banco de dados relacional com MySQL
- Carregamento de dados trimestrais e cadastrais via scripts SQL
- API REST em FastAPI para servir os dados para consulta via frontend

## Tecnologias Utilizadas - Dados

- Python 3.12
  - `pdfplumber`, `pandas`, `requests`, `beautifulsoup4`, `fastapi`, `uvicorn`
- MySQL 8.0+
- SQL (comandos `CREATE`, `LOAD DATA`, `SELECT`)
- FastAPI para API backend
- Vue.js como frontend

---


---

## Estrutura do Projeto

```
Software-Tech/
├── Scraping.py                # Script para baixar os PDFs do site da ANS
├── Transform.py              # Script para extrair e transformar os dados dos PDFs
├── main.py                   # Servidor FastAPI com endpoint de consulta
├── Relatorio_cadop.csv       # Arquivo CSV com dados das operadoras
├── search3-5.sql             # Consultas analíticas
├── structureDespesas.sql     # Script SQL para criar tabela de despesas
├── structureRelatorio.sql    # Script SQL para criar tabela de operadoras
```

---

## Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/yasmineecosta/Software-Tech.git
cd Software-Tech
```

### 2. Instalar dependências
> ```bash
> pip install pdfplumber pandas requests beautifulsoup4 fastapi uvicorn
> ```

### 3. Executar raspagem e transformação de dados
```bash
python Scraping.py   # Baixa PDFs de Anexos I e II
defina o caminho em Transform.py e execute:
python Transform.py  # Extrai tabelas, gera CSV e ZIP
```

### 4. Executar scripts de banco de dados

Certifique-se de ter o MySQL instalado e em execução.

```sql
-- Criar banco e tabela de operadoras
-- Execute o arquivo: structureRelatorio.sql

-- Criar banco e tabela de despesas trimestrais
-- Execute o arquivo: structureDespesas.sql

-- Executar as queries analíticas
-- Execute o arquivo: search3-5.sql
```

### 5. Rodar o servidor FastAPI
```bash
python -m uvicorn main:app --reload
```
Acesse [http://localhost:8000](http://localhost:8000)

---

## Endpoints Disponíveis

- `GET /` - Teste de conexão com o servidor
- `GET /build` - Retorna dados do CSV `Relatorio_cadop.csv`

(Em desenvolvimento: endpoint de busca textual entre operadoras)

---

## Consultas Analíticas

1. **Top 10 operadoras com maiores despesas em EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE no último trimestre**

    ```sql
    SELECT 
        o.razao_social,
        d.reg_ans,
        d.ano,
        d.trimestre,
        MIN(d.data) AS data_inicial,
        MAX(d.data) AS data_final,
        SUM(d.vl_saldo_final) AS total_despesa
    FROM dados_trimestrais.despesas_saude d
    LEFT JOIN dados_relatorio.operadoras o 
        ON d.reg_ans = o.registro_ans
    WHERE UPPER(d.descricao) LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE%'
      AND d.ano = 2024
      AND d.trimestre = 4
    GROUP BY d.reg_ans, o.razao_social, d.ano, d.trimestre
    ORDER BY total_despesa DESC
    LIMIT 10;
    ```

2. **Top 10 operadoras com maiores despesas em EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE no ano de 2024**

    ```sql
    SELECT 
        o.razao_social,
        d.reg_ans,
        d.ano,
        MIN(d.data) AS data_inicial,
        MAX(d.data) AS data_final,
        SUM(d.vl_saldo_final) AS total_despesa
    FROM dados_trimestrais.despesas_saude d
    LEFT JOIN dados_relatorio.operadoras o 
        ON d.reg_ans = o.registro_ans
    WHERE UPPER(d.descricao) LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE%'
      AND d.ano = 2024
    GROUP BY d.reg_ans, o.razao_social, d.ano
    ORDER BY total_despesa DESC
    LIMIT 10;
    ```

---
