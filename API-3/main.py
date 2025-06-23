from fastapi import FastAPI,HTTPException
from models import Usuario,Livro,Biblioteca,Emprestimo
from typing import List
import datetime

app = FastAPI()


bibliotecas: List[Biblioteca] = []

@app.get("/bibliotecas",response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas

@app.get("/bibliotecas/{biblioteca}",response_model=Biblioteca)
def listar_biblioteca(biblioteca:str):
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            return biblio
    raise HTTPException(404,"Não localizado.")

@app.post("/bibliotecas")
def cadastrar_biblioteca(nome:str):
    data = {
        "nome":nome,
        "acervo":[],
        "usuarios":[],
        "emprestimos":[]
    }
    biblioteca = Biblioteca(**data)
    bibliotecas.append(biblioteca)
    
@app.delete("/bibliotecas/{biblioteca}",response_model=Biblioteca)
def listar_biblioteca(biblioteca:str):
    for id,biblio in enumerate(bibliotecas):
        if biblio.nome ==biblioteca:
            bibliotecas.pop(id)
            return biblio
    raise HTTPException(404,"Não localizado.")

@app.get("/usuarios/",response_model=List[Usuario])
def listar_usuarios(nome_biblioteca:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome_biblioteca:
            return biblioteca.usuarios
    raise HTTPException(404,"Não localizado.")

@app.get("/usuarios/{username}", response_model=Usuario)
def listar_usuario(biblioteca:str, username:str):
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            for usuario in biblio.usuarios:
                if usuario.username == username:
                    return usuario
    raise HTTPException(404,"Usuário não localizado")

@app.post("/usuarios/")
def criar_usuario(biblioteca:str,usuario:Usuario):
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            return biblio.usuarios.append(usuario)
    raise HTTPException(404,"Não localizado.")
   
@app.delete("/usuarios/{username}",response_model=Usuario)
def excluir_usuario(biblioteca:str,username:str):
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            for id,usuario in enumerate(biblio.usuarios):
                if usuario.username == username:
                    biblio.usuarios.pop(id)
                    return usuario
    raise HTTPException(404,"Usuário não localizado")

@app.get("/livros",response_model=List[Livro])
def listar_livros(biblioteca:str):
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            return biblio.acervo
    raise HTTPException(404,"não localizado")  
 
@app.get("/livros/{titulo}",response_model=Livro)
def listar_livros(biblioteca:str, titulo:str):
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            for livro in biblio.acervo:
             if livro.titulo == titulo:
                return livro
    raise HTTPException(404,"Não localizado")

@app.delete("/livros/{titulo}",response_model=Livro)
def deletar_livro(biblioteca:str,titulo:str):
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            for id, livro in enumerate(biblio.acervo):
                if livro.titutlo == titulo:
                    biblio.acervo.pop(id)
                    return livro
    raise HTTPException(404,"Não localizado")

@app.post("/livros", response_model=Livro)
def criar_livro(biblioteca:str,livro:Livro):
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            biblio.acervo.append(livro)
            return livro
    raise HTTPException(404,"Não localizado")

@app.get("/emprestimos",response_model=List[Emprestimo])
def listar_emprestimos(biblioteca:str):
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            return biblio.emprestimos
    raise HTTPException(404,"Não localizado")

@app.post("/emprestimos")
def cadastrar_emprestimos(biblioteca:str,usuario:str,titulo:str):
    user = None
    book = None
    for biblio in bibliotecas:
        if biblio.nome == biblioteca:
            for u in biblio.usuarios:
                if u.username == usuario:
                    user = u
            for l in biblio.acervo:
                if l.titulo == titulo:
                    book = l
            if user and book:
                data = {
                    "usuario":user,
                    "livro":book,
                    "data_emprestimo":datetime.datetime.now().date(),
                    "data_devolucao":datetime.date(2025,5,31),
                }
                emprestimo = Emprestimo(**data)
                biblio.emprestimos.append(emprestimo)
    if not user or not book:
        raise HTTPException(404,"Não localizado")