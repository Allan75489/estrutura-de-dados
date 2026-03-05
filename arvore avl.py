class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class AVL:
    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, y):
        x = y.esquerda
        t2 = x.direita

        x.direita = y
        y.esquerda = t2

        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        t2 = y.esquerda

        y.esquerda = x
        x.direita = t2

        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    def inserir(self, raiz, valor):

        if not raiz:
            return No(valor)

        if valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        else:
            raiz.direita = self.inserir(raiz.direita, valor)

        raiz.altura = 1 + max(self.altura(raiz.esquerda),
                              self.altura(raiz.direita))

        balance = self.fator_balanceamento(raiz)

        # Rotação Direita
        if balance > 1 and valor < raiz.esquerda.valor:
            return self.rotacao_direita(raiz)

        # Rotação Esquerda
        if balance < -1 and valor > raiz.direita.valor:
            return self.rotacao_esquerda(raiz)

        # Esquerda-Direita
        if balance > 1 and valor > raiz.esquerda.valor:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Direita-Esquerda
        if balance < -1 and valor < raiz.direita.valor:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def pre_ordem(self, raiz):
        if not raiz:
            return
        print(raiz.valor, end=" ")
        self.pre_ordem(raiz.esquerda)
        self.pre_ordem(raiz.direita)


# Teste
arvore = AVL()
raiz = None

valores = [10, 20, 30, 40, 50, 25]

for v in valores:
    raiz = arvore.inserir(raiz, v)

print("Pré-ordem da árvore AVL:")
arvore.pre_ordem(raiz)