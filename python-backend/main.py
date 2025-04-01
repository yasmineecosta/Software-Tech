from fastapi import FastAPI, Query, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import numpy as np


app = FastAPI()
# python -m uvicorn server:app --reload
# Permitir acesso do frontend (Vue.js) 
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"], 
    allow_origins=["http://127.0.0.1:5500"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega o CSV uma vez na memória
df = pd.read_csv("Relatorio_cadop.csv", sep=";", encoding="utf-8")
df = df.rename(columns={
    "Registro_ANS": "registro_ans",
    "Razao_Social": "razao_social",
    "Nome_Fantasia": "nome_fantasia",
    "Cidade": "cidade"
})
df = df.where(pd.notnull(df), None)
 # Substitui NaN por None para evitar erros JSON
