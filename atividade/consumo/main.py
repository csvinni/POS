from fastapi import FastAPI, HTTPException
from typing import List
from models import Veiculo


app = FastAPI()

veiculos: List[Veiculo] = []

@app.get("/veiculos", response_model=List[Veiculo])
def listar_veiculos():
    return veiculos

@app.get("/veiculos/{placa}", response_model=Veiculo)
def buscar_veiculo(placa: str):
    for v in veiculos:
        if v.placa == placa:
            return v
    raise HTTPException(status_code=404, detail="Veículo não encontrado")

@app.post("/veiculos", response_model=Veiculo)
def cadastrar_veiculo(veiculo: Veiculo):
    for v in veiculos:
        if v.placa == veiculo.placa:
            raise HTTPException(status_code=400, detail="Placa já cadastrada")
    veiculos.append(veiculo)
    return veiculo

@app.put("/veiculos/{placa}", response_model=Veiculo)
def editar_veiculo(placa: str, dados: Veiculo):
    for i, v in enumerate(veiculos):
        if v.placa == placa:
            if placa != dados.placa:
                for existente in veiculos:
                    if existente.placa == dados.placa:
                        raise HTTPException(400, "Nova placa já cadastrada")
            veiculos[i] = dados
            return dados
    raise HTTPException(404, "Veículo não encontrado")

@app.delete("/veiculos/{placa}", response_model=Veiculo)
def deletar_veiculo(placa: str):
    for i, v in enumerate(veiculos):
        if v.placa == placa:
            return veiculos.pop(i)
    raise HTTPException(404, "Veículo não encontrado")
