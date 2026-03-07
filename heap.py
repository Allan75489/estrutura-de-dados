# ==========================================
# HEAP (MIN HEAP) - Estrutura de Dados
# ==========================================
# Uma Heap é uma árvore binária completa onde:
# - No Min Heap o menor elemento fica na raiz
# - Cada pai é menor ou igual aos seus filhos

class MinHeap:

    def __init__(self):
        """Inicializa uma heap vazia"""
        self.heap = []

    # ==============================
    # Índice do pai
    # ==============================
    def pai(self, i):
        return (i - 1) // 2

    # ==============================
    # Filho esquerdo
    # ==============================
    def filho_esquerdo(self, i):
        return 2 * i + 1

    # ==============================
    # Filho direito
    # ==============================
    def filho_direito(self, i):
        return 2 * i + 2

    # ==============================
    # Verifica se está vazia
    # ==============================
    def esta_vazia(self):
        return len(self.heap) == 0

    # ==============================
    # Retorna tamanho da heap
    # ==============================
    def tamanho(self):
        return len(self.heap)

    # ==============================
    # Ver menor elemento (sem remover)
    # ==============================
    def peek(self):
        if self.esta_vazia():
            return None
        return self.heap[0]

    # ==============================
    # Inserir elemento
    # ==============================
    def inserir(self, valor):
        self.heap.append(valor)

        i = len(self.heap) - 1

        # sobe o elemento
        while i > 0 and self.heap[self.pai(i)] > self.heap[i]:
            self.heap[i], self.heap[self.pai(i)] = self.heap[self.pai(i)], self.heap[i]
            i = self.pai(i)

    # ==============================
    # Heapify
    # ==============================
    def heapify(self, i):
        menor = i
        esq = self.filho_esquerdo(i)
        dir = self.filho_direito(i)

        if esq < len(self.heap) and self.heap[esq] < self.heap[menor]:
            menor = esq

        if dir < len(self.heap) and self.heap[dir] < self.heap[menor]:
            menor = dir

        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self.heapify(menor)

    # ==============================
    # Remover menor elemento
    # ==============================
    def remover_min(self):

        if self.esta_vazia():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify(0)

        return raiz

    # ==============================
    # Mostrar heap
    # ==============================
    def mostrar(self):
        print("Heap:", self.heap)


# ==========================================
# Teste da estrutura
# ==========================================
if __name__ == "__main__":

    heap = MinHeap()

    heap.inserir(10)
    heap.inserir(4)
    heap.inserir(15)
    heap.inserir(20)
    heap.inserir(0)
    heap.inserir(8)

    print("Heap atual:")
    heap.mostrar()

    print("Menor elemento:", heap.peek())

    print("\nRemovendo menor:", heap.remover_min())

    print("\nHeap após remoção:")
    heap.mostrar()

    print("\nTamanho da heap:", heap.tamanho())