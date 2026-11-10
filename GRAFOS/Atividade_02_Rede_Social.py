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
