"""
## Desafio integrador — Sistema de estoque
Desenvolva um pequeno sistema de estoque.
Crie uma `dataclass`:
```python
@dataclass
class Produto:
    codigo: int
    nome: str
    preco: float
    quantidade: int
```
O programa deverá permitir:
- cadastrar produtos;
- listar produtos;
- calcular o valor total do estoque;
- localizar um produto pelo código;
- identificar o produto com maior preço.
### Desafio adicional
Implemente um menu:
```text
===== SISTEMA DE ESTOQUE =====
1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto
4 - Valor total do estoque
5 - Produto mais caro
0 - Sair
Escolha:
"""
from dataclasses import dataclass

@dataclass
class Produto:
    codigo: int
    nome: str
    preco: float
    quantidade: int

lista_produtos = []

def cadastrar():
    produto = Produto(
        codigo = int(input("Código:\n")),
        nome = input("Nome: \n"),
        preco = float(input("Preço: \n")),
        quantidade = int(input("Quantidade: \n"))
    )

    lista_produtos.append(produto)

def listar_produtos():
    print("\n === Todos os Produtos ===\n")

    print(f"{'Código':<10}{'Nome':<20}{'Preço':<12}{'Quantidade':<10}")

    for produto in lista_produtos:
        print(f"{produto.codigo:<10}{produto.nome:<20}{produto.preco:<12.2f}{produto.quantidade:<10}")


def buscar_produto():
    busca = int(input("Digite o código do produto"))

    encontrado = False

    for produto in lista_produtos:
        if busca == produto.codigo:
            print(f"Produto: {produto.codigo}\n {produto.nome}")
            encontrado = True

    if not encontrado:
        print(f"Produto não encontrado. Tente novamente")





def valor_total_estoque():
    valor_estoque = 0

    for produto in lista_produtos:
        valor_produto_estoque = produto.preco * produto.quantidade
        valor_estoque += valor_produto_estoque

    print(f"Preço total do estoque: {valor_estoque}")


def produto_mais_caro():
    mais_caro = None

    if not lista_produtos:
        print(f"Nenhum produto encontrado")
    else:
        for produto in lista_produtos:
            if mais_caro is None or produto.preco > mais_caro.preco:
                mais_caro = produto

        print(f"Produto mais caro: {mais_caro.nome} | {mais_caro.preco}")
    

def sair():
    print(f"Saindo...")

escolha = -1
while escolha != 0:
    print(f"===== SISTEMA DE ESTOQUE =====\n")

    escolha = int(input("1 - Cadastrar produto \n"
                        "2 - Listar produtos\n"
                        "3 - Buscar produto\n"
                        "4 - Valor total do estoque\n"
                        "5 - Produto mais caro\n"
                        "0 - Sair\n"
                        "Escolha uma opção: \n "
                        ))

    if escolha == 1:
        cadastrar()
    elif escolha == 2:
        listar_produtos()
    elif escolha == 3:
        buscar_produto()
    elif escolha == 4:
        valor_total_estoque()
    elif escolha == 5:
        produto_mais_caro()
    elif escolha == 0:
        sair()
    else:
        print(f"Opção inválida")






