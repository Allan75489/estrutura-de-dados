# Árvore Binária em Python

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    # =========================
    # Inserção
    # =========================
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            return

        atual = self.raiz
        while True:
            if valor < atual.valor:
                if atual.esquerda is None:
                    atual.esquerda = No(valor)
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = No(valor)
                    return
                atual = atual.direita

    # =========================
    # Busca (iterativa)
    # =========================
    def buscar(self, valor):
        atual = self.raiz

        while atual:
            if valor == atual.valor:
                return True
            elif valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False

    # =========================
    # Percurso em ordem
    # =========================
    def em_ordem(self, no):
        if no:
            self.em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.em_ordem(no.direita)

    # =========================
    # 🌳 Desenhar árvore no terminal
    # =========================
    def desenhar(self, no=None, nivel=0, prefixo="Raiz: "):
        if no is None:
            no = self.raiz
            if no is None:
                print("Árvore vazia.")
                return

        print(" " * (nivel * 4) + prefixo + str(no.valor))

        if no.esquerda:
            self.desenhar(no.esquerda, nivel + 1, "E--- ")
        if no.direita:
            self.desenhar(no.direita, nivel + 1, "D--- ")


# =============================
# TESTE
# =============================

arvore = ArvoreBinaria()

valores = [10, 5, 20, 2, 7, 15, 30, 8, 15, 25, 47, 3, 9, 555]
for v in valores:
    arvore.inserir(v)

print("Árvore em ordem:")
arvore.em_ordem(arvore.raiz)
print("\n")

print("Buscar 7:", arvore.buscar(7))
print("Buscar 99:", arvore.buscar(99))

print("\n🌳 Estrutura da árvore:")
arvore.desenhar()