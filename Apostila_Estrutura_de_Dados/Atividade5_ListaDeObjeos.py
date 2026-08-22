"""
## Atividade 5 — Lista de objetos
Utilizando a `dataclass` `Aluno`, cadastre cinco alunos.
Depois:
1. calcule a média de cada aluno;
2. exiba os alunos aprovados;
3. identifique o aluno com maior média.
Considere aprovação:
```text
média >= 7.0
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


lista_alunos = []

maior_media = 0
aluno_maior_media = None
for i in range(5):
    aluno = Aluno(
        nome = input("Nome do aluno: "),
        matricula = int(input("Matricula: ")),
        nota1 = float(input("Primeira nota: ")),
        nota2 = float(input("Segunda nota: ")),
    )

    lista_alunos.append(aluno)

    resultado_media = aluno.media()

    if(resultado_media > maior_media):
        maior_media = resultado_media
        aluno_maior_media = aluno


print("\n======= Alunos aprovados =======")

for aluno in lista_alunos:
    if aluno.media() >= 7.0:
        print(f"Nome: {aluno.nome} | Média: {aluno.media():.2f}")


print("\n======= Maior média =======")
print(f"Nome: {aluno_maior_media.nome}")
print(f"Média: {maior_media:.2f}")