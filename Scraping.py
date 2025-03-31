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
