from fastapi import FastAPI, HTTPException
from typing import List
from models import Tarefa

app = FastAPI()

tarefas: List[Tarefa] = []

@app.get("/tarefas/", response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.post("/tarefas/", response_model=Tarefa)
def criar_tarefa(tarefa:Tarefa):
    tarefa.id = len(tarefas)+1
    tarefas.append(tarefa)
    return tarefa

@app.delete("/tarefas/", response_model=Tarefa)
def excluir_tarefa(tarefa_id:int):
    for index, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            del tarefas[index]
            return {"message": "tarefa removida"}
    raise HTTPException(status_code=404, detail="não localizado")