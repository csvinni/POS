from fastapi import FastAPI,HTTPException
from models import Livro
from typing import List
app = FastAPI()
livros:List[Livro]=[]

@app.get("/livros",response_model=List[Livro])
def listar_livros():
    return livros
    
@app.get("/livros/{titulo}",response_model=Livro)
def listar_livros( titulo:str):
    for livro in livros:
        if livro.titulo == titulo:
            return livro
    raise HTTPException(404,"Não localizado")

@app.delete("/livros/{titulo}",response_model=Livro)
def deletar_livro(titulo:str):
    for id, livro in enumerate(livros):
        if livro.titutlo == titulo:
            livros.pop(id)
            return livro
    raise HTTPException(404,"Não localizado")

@app.post("/livros", response_model=Livro)
def criar_livro(nome:str,livro:Livro):
    livros.append(livro)
    for livro in livros:
            return livro
    raise HTTPException(404,"Não localizado")