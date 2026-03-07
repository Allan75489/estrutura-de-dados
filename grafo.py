# ==========================================
# GRAFO - Estrutura de Dados
# Representação usando Lista de Adjacência
# ==========================================

from collections import deque


class Grafo:

    def __init__(self):
        # dicionário que armazena o grafo
        # chave = vértice
        # valor = lista de vizinhos
        self.grafo = {}

 
    def adicionar_vertice(self, vertice):

        if vertice not in self.grafo:
            self.grafo[vertice] = []

    
    def adicionar_aresta(self, v1, v2):

        # cria os vértices se não existirem
        self.adicionar_vertice(v1)
        self.adicionar_vertice(v2)

        # adiciona conexão
        self.grafo[v1].append(v2)
        self.grafo[v2].append(v1)

   
    def mostrar(self):

        print("Lista de Adjacência do Grafo:\n")

        for vertice in self.grafo:
            print(f"{vertice} -> {self.grafo[vertice]}")

  
    def bfs(self, inicio):

        visitados = set()
        fila = deque()

        visitados.add(inicio)
        fila.append(inicio)

        print("\nBFS (Busca em Largura):")

        while fila:

            vertice = fila.popleft()
            print(vertice, end=" ")

            for vizinho in self.grafo[vertice]:

                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        print()

 
    def dfs(self, vertice, visitados=None):

        if visitados is None:
            visitados = set()
            print("\nDFS (Busca em Profundidade):")

        visitados.add(vertice)

        print(vertice, end=" ")

        for vizinho in self.grafo[vertice]:

            if vizinho not in visitados:
                self.dfs(vizinho, visitados)


# ==========================================
# Testando o Grafo
# ==========================================
if __name__ == "__main__":

    g = Grafo()

    # adicionando arestas
    g.adicionar_aresta("A", "B")
    g.adicionar_aresta("A", "C")
    g.adicionar_aresta("B", "D")
    g.adicionar_aresta("C", "D")
    g.adicionar_aresta("D", "E")

    # mostrar grafo
    g.mostrar()

    # BFS
    g.bfs("A")

    # DFS
    g.dfs("A")