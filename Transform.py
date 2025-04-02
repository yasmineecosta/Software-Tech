import os
import zipfile
import dotenv
import pandas as pd
import pdfplumber
from dotenv import load_dotenv

load_dotenv()

pdf_path = os.getenv("PDF_PATH")
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

# Concatena em um único DataFrame
dataframes = [pd.DataFrame(table[1:], columns=table[0]) for table in all_tables if table[0]]
df = pd.concat(dataframes, ignore_index=True)

# Substitui siglas por descrições conforme legenda do PDF
substituicoes = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}
for col in df.columns:
    df[col] = df[col].replace(substituicoes)

# Salva o DataFrame como CSV
df.to_csv(csv_path, index=False)

# Compacta o CSV em um arquivo ZIP
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path, os.path.basename(csv_path))

print(f"CSV salvo como '{csv_path}' e compactado em '{zip_path}'.")