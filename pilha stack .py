# Pilha stack uma estrutura de dados do tipo LIFO em Python

class Stack:
    def __init__(self, n):
        self.keys = [None] * n
        self.n = n
        self.topo = 0

    def is_empty(self):
        return self.topo == 0

    def peek(self):
        if self.is_empty():
            print("Erro: stack vazia")
            return None
        return self.keys[self.topo - 1]

    def push(self, key):
        if self.topo == self.n:
            print("Erro: overflow")
            return
        self.keys[self.topo] = key
        self.topo += 1
        print(f"{key} inserido na pilha.")

    def pop(self):
        if self.is_empty():
            print("Erro: underflow")
            return None
        self.topo -= 1
        key = self.keys[self.topo]
        self.keys[self.topo] = None
        print(f"{key} removido da pilha.")
        return key

    def mostrar(self):
        print("Pilha:", self.keys[:self.topo])


# ===============================
# PROGRAMA PRINCIPAL (funcional)
# ===============================

tamanho = int(input("Digite o tamanho da pilha: "))
pilha = Stack(tamanho)

while True:
    print("\n=== MENU ===")
    print("1 - Push")
    print("2 - Pop")
    print("3 - Peek")
    print("4 - Ver pilha")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        valor = input("Valor para inserir: ")
        pilha.push(valor)

    elif op == "2":
        pilha.pop()

    elif op == "3":
        topo = pilha.peek()
        if topo is not None:
            print("Topo da pilha:", topo)

    elif op == "4":
        pilha.mostrar()

    elif op == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")