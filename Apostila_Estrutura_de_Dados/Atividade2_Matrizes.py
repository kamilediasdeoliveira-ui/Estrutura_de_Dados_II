"""
Atividade 2 — Matrizes                                                                  
Crie uma matriz `3 × 3`.
Solicite os valores ao usuário e:
1. exiba a matriz;
2. calcule a soma de todos os elementos;
3. calcule a soma da diagonal principal;
4. encontre o maior elemento.
Exemplo:
```text
1 2 3
4 5 6
7 8 9
```
A diagonal principal é:
```text
1
   5
      9
```
Soma:
```text
1 + 5 + 9 = 15
```
---
""" 

matriz = [[0 for _ in range (3)] for _ in range(3)]

for i in range(3): # i é a linha
    for j in range(3): # j é a coluna
        matriz[i][j] = int(input(f"Digite um número para a posição [{i}][{j}]: "))

somaTotal = 0
for i in matriz:
    for valor in i:
        somaTotal += valor

somaDiagonal = 0
for i in range(3):
    for j in range(3):
        if i == j:
            somaDiagonal += matriz[i][j]

maior = matriz[0][0]
for i in matriz:
    for valor in i:
        if (valor > maior ):
            maior = valor

        
print("\n--- RESULTADOS ---\n")
print(f"Matriz: {matriz}\n")
print(f"Soma de todos os elementos: {somaTotal}\n")
print(f"Soma da diagonal principal: {somaDiagonal}\n")
print(f"Maior número: {maior}\n")



