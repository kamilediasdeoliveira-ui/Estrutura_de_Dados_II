"""
## Atividade 3 — Dicionário
Crie um dicionário para representar um livro com:
```text
titulo
autor
ano
preco
```
Depois:
1. leia os dados;
2. armazene-os no dicionário;
3. exiba os dados;
4. altere o preço;
5. adicione uma informação chamada `categoria`.
---
"""


livro = {}

livro["titulo"] = input("Digite o titulo: \n")
livro["autor"] = input("Nome do autor: \n")
livro["ano"] = int(input("Ano de lançamento: \n"))
livro["preco"] = float(input("Preço: \n"))

print(f"\n--- Dados do Livro ---\n")

for chave, valor in livro.items():
    print(f"{chave}: {valor}")

# muda o preço diretamente
livro["preco"] = 20.33

# Adiciona a categoria diretamente
livro["categoria"] = "Drama"

print("\n--- Dados atualizados ---")

for chave, valor in livro.items():
    print(f"{chave}: {valor}")