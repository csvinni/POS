from pydantic import BaseModel

class Tarefa(BaseModel):
    id: int
    descricao: str
    prioridade: str
    concluida: bool
