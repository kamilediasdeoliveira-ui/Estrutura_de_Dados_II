"""
## Atividade 1 — Listas

Crie um programa que:

1. crie uma lista com 10 números inteiros;
2. solicite os valores ao usuário;
3. exiba todos os números;
4. calcule a soma;
5. calcule a média.

### Desafio

Além disso, encontre:

- o maior valor;
- o menor valor;
- a quantidade de números pares.

---

"""

numeros = []

maior = None
menor = None
quantidade_pares = 0
for i in range(10):
    valor = int(input(f"Digite um número inteiro:"))
    numeros.append(valor)

    if(maior is None or valor > maior):
        maior = valor
    if(menor is None or valor < menor):
        menor = valor

    if(valor % 2 == 0):
        quantidade_pares += 1

soma = sum(numeros)
media = soma / len(numeros)


print("\n--- RESULTADOS ---")
print(f"Números: {numeros}\n Soma: {soma}\n Média: {media}\n Maior: {maior}\n Menor: {menor}\n Quantidade de Pares: {quantidade_pares}")
