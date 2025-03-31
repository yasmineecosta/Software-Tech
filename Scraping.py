# pip install requests beautifulsoup4
# pip install pdfplumber pandas
# pip install tabula-py pandas
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from zipfile import ZipFile

import pandas as pd
# URL base
base_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Diretório para salvar os arquivos
output_dir = "anexos"
os.makedirs(output_dir, exist_ok=True)

# Acessa o site
response = requests.get(base_url)
soup = BeautifulSoup(response.content, "html.parser")

# Baixar PDFs de Anexo I e II
pdf_links = []
for link in soup.find_all("a", href=True):
    href = link["href"]
    text = link.get_text().lower()

    if "anexo i" in text or "anexo ii" in text:
        full_url = urljoin(base_url, href)
        if full_url.endswith(".pdf"):
            pdf_links.append((text.strip(), full_url))
