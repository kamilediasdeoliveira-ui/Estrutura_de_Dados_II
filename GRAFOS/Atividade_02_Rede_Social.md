<img width="164" height="79" alt="image" src="https://github.com/user-attachments/assets/0ae7070c-8e2e-477c-abd1-73be0e2c64a8" />


# MINIPROJETO CONECTA UDF

**Disciplina:** Estrutura de Dados II | Unidade III: Grafos
**Professora:** Kadidja Valéria
**Aluna:** Isaú júlio, Kamile Dias, Thales da Mata e Thierry Henry

## Desafio Proposto

* Representar uma rede social como um grafo.
* Calcular conexões e densidade.
* Descobrir caminhos entre usuários.
* Usar Python para automatizar os cálculos.
* **Atividade Prática:** Adicionar 4 usuários fictícios, criar pelo menos 5 novas amizades, atualizar o grafo e o código, e comparar os graus e a densidade antes e depois.

## 1. Grafo Atualizado (Rede Expandida com 15 Usuários)

Abaixo está a representação visual da rede social expandida com os novos usuários (Kátia,Gabi,Nicolas,Hugo,Igor,Lucas,Mariana,Olivia,Julia) e as novas conexões:

<img width="1050" height="556" alt="ImagemC1" src="https://github.com/user-attachments/assets/a48140c1-5b7c-4228-9efc-61089ff3fdb9" />


## 2. Código Python Atualizado

```python
rede = {
    "Ana": ["Bruno", "Carla", "Kátia"],
     "Kátia": ["Ana", "Elisa"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe", "Gabi"],
    "Elisa": ["Carla", "Diego", "Felipe", "Kátia"],
    "Felipe": ["Diego", "Elisa", "Julia"],
     "Gabi": ["Diego", "Hugo"],
     "Julia": ["Hugo", "Igor", "Felipe"],
     "Nicolas": ["Igor", "Olivia"],
     "Igor": ["Julia", "Hugo", "Nicolas"],
     "Olivia": ["Lucas", "Nicolas"],
      "Lucas": ["Hugo", "Olivia"],
      "Hugo": ["Gabi", "Mariana", "Lucas", "Igor", "Julia"],
      "Mariana": ["Hugo"]
     }

n = len(rede)  # n representa o número total de vértices (nós/pessoas) na rede
# rede.values() traz as listas de amigos.
# len(a) calcula o grau (número de amigos) daquela pessoa.
soma_graus = sum(len(a) for a in rede.values())

# E representa o número de arestas (linhas de conexão exclusivas)
E = soma_graus // 2

# D representa a densidade (proporção de conexões reais frente ao máximo teórico possível)
D = 2 * E / (n * (n - 1))

print(f"Usuarios: {n} | Amizades: {E} | Densidade: {D:.2%}")
```

## 3. Comparativo: Antes vs. Depois

### ANTES (Rede Original com 6 Usuários)

* **Calcule o Grau:**
  * $\text{Ana} = 2$
  * $\text{Bruno} = 3$
  * $\text{Carla} = 3$
  * $\text{Diego} = 3$
  * $\text{Elisa} = 3$
  * $\text{Felipe} = 3$
  * *Maior grau:* Bruno, Carla, Diego e Elisa.

* **Conte as Arestas:**
  * $\text{Soma} = 2 + 3 + 3 + 3 + 3 + 2 = 16$
  * $\text{Arestas} = 16 \div 2 = 8$
  * $E = 8$ amizades.

* **Calcule a Densidade:**
  * $D = \frac{2E}{V \times (V - 1)}$
  * $E = 8$ | $V = 6$
  * $D = \frac{16}{6 \times 5} = \frac{16}{30}$
  * $D \approx 0,533 = 53,3\%$ das conexões possíveis.

### DEPOIS (Rede Expandida com 15 Usuários)

* **Calcule o Grau:**
  * $\text{Ana} = 2$
  * $\text{Bruno} = 3$
  * $\text{Katia} = 2$
  * $\text{Carla} = 3$
  * $\text{Diego} = 4$
  * $\text{Elisa} = 4$
  * $\text{Gabi} = 2$
  * $\text{Felipe} = 3$
  * $\text{Julia} = 3$
  * $\text{Hugo} = 5$
  * $\text{Mariana} = 1$
  * $\text{Igor} = 3$
  * $\text{Nicolas} = 2$
  * $\text{Lucas} = 2$
  * $\text{Olivia} = 2$
  * *Maior grau:* Hugo ($5$ conexões).

* **Conte as Arestas:**
  * $\text{Soma} =  3 + 3 + 2 + 3 + 4 + 4 + 2 + 3 + 3 + 5 + 1 + 3 + 2 + 2 + 2 = 42$
  * $\text{Arestas} = 42 \div 2 = 21$
  * $E = 21$ amizades.

* **Calcule a Densidade:**
  * $D = \frac{2E}{V \times (V - 1)}$
  * $E = 21$ | $V = 15$
  * $D = \frac{42}{15 \times 14} = \frac{42}{210}$
  * $D \approx 0,2 = 20,0\%$ das conexões possíveis.



* **Conclusões:**
* Enquanto existiu aumento no número de pessoas(nós) e amizades(arestas) em relação a  estrutura original, diminuiu o percentual das conexões possíveis. Logo, isso mostra  que a rede se expandiu com o número de conexões sendo menor do que antes.