from fastapi import FastAPI, Query, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import pandas as pd
import csv
import io
import json
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


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/verificar")
def verificar_csv():
    return {"linhas": len(df), "colunas": list(df.columns)}

@app.get("/busca")
def buscar_operadoras(q: str = Query(..., min_length=1)):
    resultados = df[df.apply(
        lambda row: row.astype(str).apply(lambda val: q.lower() in val.lower()).any(), axis=1
    )].head(15)

    # Substitui NaN, inf, -inf por None
    resultados = resultados.replace([np.nan, np.inf, -np.inf], None)

    # Converte para dicionário
    registros = resultados.to_dict(orient="records")

    # Serializa JSON com proteção contra valores inválidos
    json_str = json.dumps(registros, allow_nan=False)

    return JSONResponse(content=json.loads(json_str))
