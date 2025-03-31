import os
import zipfile
import pandas as pd
import pdfplumber


pdf_path = "C:\\Users\\Yasmine Martins\\Desktop\\vsCode\\Software-Tech\\anexos\\anexo_i.pdf"
csv_path = "rol_procedimentos.csv"
zip_path = "Teste_Yasmine.zip" 

# Lê todas as tabelas do PDF
all_tables = []
if os.path.exists(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                if table and len(table) > 1:
                    all_tables.append(table)
else:
    print(f"Erro: O arquivo PDF '{pdf_path}' não foi encontrado.")
    exit(1)
