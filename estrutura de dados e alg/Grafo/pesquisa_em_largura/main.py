from collections import deque


def pesquisa(nome, grafo):
    fila_de_pesquisa = deque()

    fila_de_pesquisa += grafo[nome]
    verificadas = []

    def pessoa_e_vendedor(pessoa):
        return pessoa[-1] == "m"
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()

        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor!")
            else:
                fila_de_pesquisa += grafo[pessoa]
                print(pessoa + " não é um vendedor!")
                verificadas.append(pessoa)



if __name__ == "__main__":
    grafo = {}

    grafo["voce"] = ["alice", "bob", "claire"]
    grafo["bob"] = ["anuj", "peggy"]
    grafo["alice"] = ["peggy"]
    grafo["claire"] = ["jonny", "thom"]
    grafo["anuj"] = []
    grafo["peggy"] = []
    grafo["thom"] = []
    grafo["jonny"] = []

    pesquisa("voce", grafo)