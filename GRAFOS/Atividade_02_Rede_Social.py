rede = {
    "Ana": ["Bruno", "Carla"],
    "Bruno": ["Ana", "Carla", "Diego"],
    "Carla":["Ana", "Bruno", "Elisa"],
    "Diego": ["Bruno", "Elisa", "Felipe", "João"],
    "Elisa": ["Carla", "Diego", "Felipe"],
    "Felipe": ["Diego", "Elisa","Pedro"],
    "João": ["Diego", "Maria"],
    "Pedro": ["Felipe", "Isabela"],
    "Maria": ["João", "Isabela"],
    "Isabela": ["Pedro", "Maria"]
}

n = len(rede) # n representa o número total de vértices (nós/pessoas) na rede

# rede.values() traz as listas de amigos. 
# 'a' é a lista de amigos atual no laço. len(a) é o grau (número de amigos) daquela pessoa.
soma_graus = sum(len(a)for a in rede.values()) 

# E representa o número de arestas (linhas de conexão exclusivas)
E = soma_graus // 2 

# D representa a densidade (proporção de conexões reais frente ao máximo teórico possível)
D = 2 * E / (n * (n -1)) 
print(f"Vértices: {n} | Arestas: {E} | Densidade: {D:.2%}")