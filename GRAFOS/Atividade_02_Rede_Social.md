<img width="164" height="79" alt="image" src="https://github.com/user-attachments/assets/0ae7070c-8e2e-477c-abd1-73be0e2c64a8" />


# MINIPROJETO CONECTA UDF

**Disciplina:** Estrutura de Dados II | Unidade III: Grafos

**Professora:** Kadidja Valéria

**Alunos:** Isaú Júlio, Thales da Mata, Kamile Dias de Oliveira, Thierry Henry

## Desafio Proposto

* Representar uma rede social como um grafo.
* Calcular conexões e densidade.
* Descobrir caminhos entre usuários.
* Usar Python para automatizar os cálculos.
* **Atividade Prática:** Adicionar 4 usuários fictícios, criar pelo menos 5 novas amizades, atualizar o grafo e o código, e comparar os graus e a densidade antes e depois.

## 1. Grafo Atualizado (Rede Expandida com 20 Usuários)

Abaixo está a representação visual da rede social expandida com os novos usuários e as novas conexões:

<img width="1050" height="668" alt="ImagemC1" src="https://github.com/user-attachments/assets/673290a0-b985-4310-85d4-4853347b72b2" />


## 2. Código Python Atualizado
### LINK DO COLAB: https://colab.research.google.com/drive/1xlz-5g8UOmjVNiOMR9G2MHT5pazlRNFU

```python
rede = {
    "Ana": ["Bruno", "Carla", "Kátia"],
    "Kátia": ["Ana", "Elisa"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla": ["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe", "Gabi"],
    "Elisa": ["Carla", "Diego", "Felipe", "Kátia", "Pedro"],
    "Felipe": ["Diego", "Elisa", "Julia", "Rodrigo"],
    "Gabi": ["Diego", "Hugo", "Thales"],
    "Julia": ["Hugo", "Igor", "Felipe"],
    "Nicolas": ["Igor", "Olivia", "Úrsula"],
    "Igor": ["Julia", "Hugo", "Nicolas"],
    "Olivia": ["Lucas", "Nicolas"],
    "Lucas": ["Hugo", "Olivia"],
    "Hugo": ["Gabi", "Mariana", "Lucas", "Igor", "Julia"],
    "Mariana": ["Hugo"],
    "Thales": ["Gabi"],
    "Úrsula": ["Nicolas"],
    "Sofia": ["Pedro", "Rodrigo"],
    "Pedro": ["Elisa", "Rodrigo", "Sofia"],
    "Rodrigo": ["Felipe", "Pedro", "Sofia"]

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

### DEPOIS (Rede Expandida com 20 Usuários)

* **Calcule o Grau:**
  * $\text{Ana} = 3$
  * $\text{Bruno} = 3$
  * $\text{Katia} = 2$
  * $\text{Carla} = 3$
  * $\text{Diego} = 4$
  * $\text{Elisa} = 5$
  * $\text{Gabi} = 3$
  * $\text{Felipe} = 4$
  * $\text{Julia} = 3$
  * $\text{Hugo} = 5$
  * $\text{Mariana} = 1$
  * $\text{Igor} = 3$
  * $\text{Nicolas} = 3$
  * $\text{Lucas} = 2$
  * $\text{Olivia} = 2$
  * $\text{Thales} = 1$
  * $\text{Úrsula} = 1$
  * $\text{Sofia} = 2$
  * $\text{Pedro} = 3$
  * $\text{Rodrigo} = 3$
  * *Maior grau:* Hugo ($5$ conexões), *Elisa  ($5$ conexões) .

* **Conte as Arestas:**
  * $\text{Soma} =  3 + 3 + 2 + 3 + 4 + 5 + 3 + 4 + 3 + 5 + 1 + 3 + 3 + 2 + 2 + 1 + 1 + 2 + 3 + 3 = 56$
  * $\text{Arestas} = 56 \div 2 = 28$
  * $E = 28$ amizades.

* **Calcule a Densidade:**
  * $D = \frac{2E}{V \times (V - 1)}$
  * $E = 28$ | $V = 20$
  * $D = \frac{56}{20 \times 19} = \frac{56}{380}$
  * $D \approx 0,1474 = 15,0\%$ das conexões possíveis.



## **Conclusões:**
* Enquanto existiu aumento no número de pessoas(nós) e amizades(arestas) em relação a  estrutura original, diminuiu o percentual das conexões possíveis. Logo, isso mostra  que a rede se expandiu com o número de conexões sendo menor do que antes.
* As pessoas mais conectadas da rede são Elisa e Hugo
*  Pensando em como a rede social do Instagram funciona podemos analisar a lógica de recomendação e  conectar a lógica do grafo ao tentar responder a pergunta "Como sugerir amizade usando amigos e comum?". Por exemplo: no grafo Ana não conhece a Elisa, mas,  Elisa conhece  Carla e Kátia, conexões de Ana, então, como elas têm conexões em comum a rede social deve fazer Elisa aparecer como uma recomendação para Ana e vice-versa. Outro exemplo: Carla e Diego possuem algumas conexões em comum(Bruno e Elisa), então Carla deve ser uma recomendação de conexão para Diego e  vice-versa
*  A rede social, tendo em vista que faz usuários trocarem dados entre si por meio das conexões deve se preocupar com a privacidade. Uma forma de assegurar a privacidade dos usuários é permitir que eles determinem quem pode se conectar a eles ou não com a opção de restringir o acesso de pessoas recomendadas, ou seja, se existe pessoas indesejáveis ou que apresentam algum tipo de risco por ser talvez algum 'bot' o indivíduo pode anular aquela recomendação e também não ser recomendada para o perfil indesejado.
*  Outras métricas que podem ser observadas para descrever uma rede são: nível de largura e profundidade da conta, fluxo de postagens e informações dos perfis.
    

    
