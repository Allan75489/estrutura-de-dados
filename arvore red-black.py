# ==========================================
# IMPLEMENTAÇÃO DE UMA ÁRVORE RED-BLACK
# ==========================================


# =========================
# Classe do Nó
# =========================
class No:
    def __init__(self, valor):
        self.valor = valor
        
        # vermelho por padrão
        self.cor = "vermelho"
        
        # filhos
        self.esq = None
        self.dir = None
        
        # pai
        self.pai = None


# =========================
# Classe da Árvore
# =========================
class ArvoreRedBlack:

    def __init__(self):
        self.raiz = None


    # =========================
    # Rotação esquerda
    # =========================
    def rotacao_esquerda(self, x):

        y = x.dir
        x.dir = y.esq

        if y.esq:
            y.esq.pai = x

        y.pai = x.pai

        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esq:
            x.pai.esq = y
        else:
            x.pai.dir = y

        y.esq = x
        x.pai = y


    # =========================
    # Rotação direita
    # =========================
    def rotacao_direita(self, x):

        y = x.esq
        x.esq = y.dir

        if y.dir:
            y.dir.pai = x

        y.pai = x.pai

        if x.pai is None:
            self.raiz = y
        elif x == x.pai.dir:
            x.pai.dir = y
        else:
            x.pai.esq = y

        y.dir = x
        x.pai = y


    # =========================
    # Inserção
    # =========================
    def inserir(self, valor):

        novo = No(valor)

        pai = None
        atual = self.raiz

        while atual:
            pai = atual

            if valor < atual.valor:
                atual = atual.esq
            else:
                atual = atual.dir

        novo.pai = pai

        if pai is None:
            self.raiz = novo

        elif valor < pai.valor:
            pai.esq = novo
        else:
            pai.dir = novo

        self.corrigir_insercao(novo)


    # =========================
    # Corrigir cores
    # =========================
    def corrigir_insercao(self, no):

        while no != self.raiz and no.pai.cor == "vermelho":

            if no.pai == no.pai.pai.esq:

                tio = no.pai.pai.dir

                if tio and tio.cor == "vermelho":

                    no.pai.cor = "preto"
                    tio.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    no = no.pai.pai

                else:

                    if no == no.pai.dir:
                        no = no.pai
                        self.rotacao_esquerda(no)

                    no.pai.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    self.rotacao_direita(no.pai.pai)

            else:

                tio = no.pai.pai.esq

                if tio and tio.cor == "vermelho":

                    no.pai.cor = "preto"
                    tio.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    no = no.pai.pai

                else:

                    if no == no.pai.esq:
                        no = no.pai
                        self.rotacao_direita(no)

                    no.pai.cor = "preto"
                    no.pai.pai.cor = "vermelho"
                    self.rotacao_esquerda(no.pai.pai)

        self.raiz.cor = "preto"


    # =========================
    # BUSCA
    # =========================
    def buscar(self, valor):

        atual = self.raiz

        while atual:

            if valor == atual.valor:
                return atual

            elif valor < atual.valor:
                atual = atual.esq

            else:
                atual = atual.dir

        return None


    # =========================
    # IMPRIMIR ÁRVORE
    # =========================
    def imprimir(self, no, nivel=0):

        if no:

            self.imprimir(no.dir, nivel + 1)

            cor = "🔴" if no.cor == "vermelho" else "⚫"

            print("   " * nivel + f"{no.valor} {cor}")

            self.imprimir(no.esq, nivel + 1)


# =========================
# TESTE
# =========================

arvore = ArvoreRedBlack()

valores = [10, 20, 30, 15, 5, 1, 50]

for v in valores:
    arvore.inserir(v)

print("\nEstrutura da árvore:\n")

arvore.imprimir(arvore.raiz)


# =========================
# Testando busca
# =========================

busca = 15

resultado = arvore.buscar(busca)

if resultado:
    print(f"\nValor {busca} encontrado!")
else:
    print(f"\nValor {busca} não encontrado!")