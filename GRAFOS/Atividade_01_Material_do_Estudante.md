![UDF](Imagem/ImagemA.png)

# Material do Estudante – Prática de Grafos

**Disciplina:** Estrutura de Dados II | **Unidade III:** Grafos  
**Professora:** Kadidja Valéria  
**Aluna:** Kamile Dias de Oliveira  

---

## 1. Atividade 1 – Desenhando um grafo

- Considere $V = \{1, 2, 3, 4, 5\}$ e $E = \{(1,2), (1,4), (1,5), (2,3), (3,4), (4,4)\}$. 
- Desenhe o grafo; determine ordem e tamanho; identifique o laço; calcule o grau de cada vértice.
- A aresta $(4,4)$ é um laço. No cálculo do grau, um laço é contado duas vezes.

![FOTO 1](Imagem/ImagemA1.png)

- **Ordem:** 5 
- **Tamanho:** 6
- **Laço:** $(4,4)$
- **Graus:** $v_1 = 3$, $v_2 = 2$, $v_3 = 2$, $v_4 = 4$, $v_5 = 1$

---

## 2. Atividade 2 – Incidência e adjacência

Utilize o grafo da Atividade 1.  
Liste os vértices adjacentes a cada vértice e as arestas incidentes.  
Escolha dois vértices adjacentes e dois não adjacentes e justifique.

### 1. Vértices Adjacentes a Cada Vértice
- **Vértice 1:** adjacente a 2, 4 e 5.
- **Vértice 2:** adjacente a 1 e 3.
- **Vértice 3:** adjacente a 2 e 4.
- **Vértice 4:** adjacente a 1, 3 e ele mesmo (4) (devido ao laço $(4,4)$).
- **Vértice 5:** adjacente a 1.

### 2. Arestas Incidentes a Cada Vértice
- **Vértice 1:** incidentes às arestas $(1,2)$, $(1,4)$ e $(1,5)$.
- **Vértice 2:** incidentes às arestas $(1,2)$ e $(2,3)$.
- **Vértice 3:** incidentes às arestas $(2,3)$ e $(3,4)$.
- **Vértice 4:** incidentes às arestas $(1,4)$, $(3,4)$ e o laço $(4,4)$.
- **Vértice 5:** incidente à aresta $(1,5)$.

### 3. Escolha e Justificativa de Vértices
- **Vértices adjacentes (1 e 2):**  
  São adjacentes porque existe uma aresta representada por $(1,2)$, que conecta diretamente o vértice 1 ao vértice 2.
- **Vértices não adjacentes (2 e 5):**  
  Não são adjacentes porque não existe nenhuma aresta no conjunto que conecte o vértice 2 diretamente ao vértice 5.

---

## 3. Atividade 3 – Modelagem de uma rede de amizades

Considere João, Carolina, Maria e Marco.  
Defina $V$ e $E$, desenhe a rede, informe se o grafo é dirigido ou não dirigido e justifique.  
Identifique quem possui maior grau no grafo criado.  
Explique o que vértices e arestas representam no problema.

![FOTO 2](Imagem/ImagemA2.png)

### 1. Definição dos Conjuntos V e E
- $V = \{\text{CAROLINA, MARIA, JOÃO, MARCOS}\}$
- $E = \{(\text{CAROLINA, MARIA}), (\text{MARIA, CAROLINA}), (\text{CAROLINA, JOÃO}), (\text{JOÃO, CAROLINA}), (\text{JOÃO, MARIA}), (\text{MARCOS, JOÃO})\}$

> *Como se trata de um grafo dirigido, cada seta bidirecional representa dois pares ordenados (ida e volta).*

### 2. Classificação do Grafo e Justificativa
- **Tipo de Grafo:** Grafo Dirigido.
- **Justificativa:** O grafo possui setas que indicam a direção das conexões. Em um contexto de rede social (como o Instagram), isso significa que a relação de "seguir" pode ser unilateral (por exemplo, Marcos segue João, mas João não segue Marcos) ou mútua/recíproca (como entre Carolina e Maria, ou Carolina e João).

### 3. Maior Grau
Em grafos dirigidos, calcula-se os graus de entrada (quantas setas chegam) e de saída (quantas setas saem):

$$\text{Grau Total} = \text{Grau Entrada} + \text{Grau Saída}$$

- **CAROLINA:** Chegam 2 setas (de Maria e João) e saem 2 setas (para Maria e João).  
  $$\text{Grau Total} = 2 + 2 = 4$$
- **JOÃO:** Chegam 2 setas (de Carolina e Marcos) e saem 2 setas (para Carolina e Maria).  
  $$\text{Grau Total} = 2 + 2 = 4$$

**Maior Grau:** **CAROLINA** e **JOÃO** possuem o maior grau no grafo criado ($\text{grau} = 4$).

---

## 4. Atividade 4 – Modelagem de ruas de mão única

- Represente cruzamentos/pontos relevantes por vértices e ruas por arestas dirigidas.
- Defina $V$ e $E$ e use setas para indicar o sentido permitido.
- Escolha um vértice e determine seu grau de entrada e grau de saída.
- Explique por que um grafo não dirigido não representa adequadamente a situação.

![FOTO 3](Imagem/ImagemA3.png)

### 1. Definição dos Conjuntos V e E
- $V = \{A, B, C, D\}$
- $E = \{(A,D), (D,C), (C,B), (B,A)\}$

### 2. Grau de Entrada e Grau de Saída do Vértice A
- **Grau de Entrada:** $1$ (recebe a seta que vem do cruzamento $B$)
- **Grau de Saída:** $1$ (envia a seta que vai para o cruzamento $D$)
- **Grau Total:** $1 + 1 = 2$

### 3. Justificativa
Um grafo não dirigido não representa adequadamente a situação porque suas arestas não possuem direção, o que indicaria que o trânsito é de mão dupla em todas as ruas. Como o problema trata de ruas de mão única, é fundamental utilizar um grafo dirigido (com setas) para definir o sentido permitido e proibir o tráfego no sentido contrário.