# Implemnetando uma lista ordenada usando um estrutura de dados simples com python.
class ListaOrdenada:
    def __init__(self):
        # Inicializa a lista vazia que sempre será mantida em ordem
        self.lista = []

    def inserir(self, valor):
        """
        Insere um valor mantendo a lista ordenada.
        Usa busca binária para encontrar a posição correta.
        Complexidade:
            - Busca da posição: O(log n)
            - Inserção na lista: O(n)
        """
        esquerda, direita = 0, len(self.lista)

        # Busca binária para encontrar a posição de inserção
        while esquerda < direita:
            meio = (esquerda + direita) // 2

            # Se o valor do meio for menor, vai para a metade direita
            if self.lista[meio] < valor:
                esquerda = meio + 1
            else:
                # Caso contrário, vai para a metade esquerda
                direita = meio

        # Insere o valor na posição correta
        self.lista.insert(esquerda, valor)

    def buscar(self, valor):
        """
        Realiza busca binária.
        Retorna:
            - índice do elemento se encontrado
            - -1 se não encontrado
        Complexidade: O(log n)
        """
        esquerda, direita = 0, len(self.lista) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2

            # Elemento encontrado
            if self.lista[meio] == valor:
                return meio

            # Procura na metade direita
            elif self.lista[meio] < valor:
                esquerda = meio + 1

            # Procura na metade esquerda
            else:
                direita = meio - 1

        # Elemento não encontrado
        return -1

    def remover(self, valor):
        """
        Remove um valor da lista ordenada.
        Retorna True se removeu, False se não encontrou.
        Complexidade:
            - Busca: O(log n)
            - Remoção: O(n)
        """
        pos = self.buscar(valor)

        if pos != -1:
            self.lista.pop(pos)
            return True

        return False

    def __str__(self):
        """
        Permite imprimir o objeto diretamente com print().
        """
        return str(self.lista)


# ================== PROGRAMA PRINCIPAL ==================
if __name__ == "__main__":
    # Cria a lista ordenada
    lista = ListaOrdenada()

    # Inserções de teste
    lista.inserir(5)
    lista.inserir(2)
    lista.inserir(8)

    # Impressão da lista (já ordenada)
    print(lista)