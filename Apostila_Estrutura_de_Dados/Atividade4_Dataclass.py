"""Atividade 4 — Dataclass
Crie uma `dataclass` chamada `Aluno` com:
```text
nome
matricula
nota1
nota2
```
Crie um método chamado `media()` que calcule a média das duas notas.
Exemplo:
```python
aluno = Aluno(
    "Maria",
    12345,
    8.0,
    9.0
)
print(aluno.media())
```
---
"""

from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    matricula: int
    nota1: float
    nota2: float

    def media(self) -> float:
        return (self.nota1 + self.nota2) / 2



aluno = Aluno(
    "Maria",
    12345,
    7.8,
    8.8
)

print(f" ======= Aluno =======\n Nome: {aluno.nome}\n Matricula: {aluno.matricula}\n Nota 1: {aluno.nota1}\n Nota 2: {aluno.nota2}\n Media: {aluno.media()}")