-- querie para buscar os 10 maiores valores de despesas de saúde por operadora
-- 4º Trimestre de 2024
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
