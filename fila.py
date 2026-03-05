class FilaAtendimento:
    def __init__(self):
        # Filas separadas
        self.fila_normal = []
        self.fila_preferencial = []

        # Contadores
        self.cont_normal = 0
        self.cont_pref = 0

    def gerar_senha_normal(self):
        """Gera senha normal (N001)"""
        self.cont_normal += 1
        senha = f"N{self.cont_normal:03}"
        self.fila_normal.append(senha)
        return senha

    def gerar_senha_preferencial(self):
        """Gera senha preferencial (P001)"""
        self.cont_pref += 1
        senha = f"P{self.cont_pref:03}"
        self.fila_preferencial.append(senha)
        return senha

    def atender_cliente(self):
        """
        Regra profissional:
        atende preferencial primeiro
        """
        if self.fila_preferencial:
            senha = self.fila_preferencial.pop(0)
            return f"🔔 Atendendo senha preferencial {senha}"

        elif self.fila_normal:
            senha = self.fila_normal.pop(0)
            return f"🔔 Atendendo senha normal {senha}"

        else:
            return "⚠️ Não há clientes na fila."

    def mostrar_filas(self):
        """Mostra tamanho das filas"""
        return (
            f"📊 Normal: {len(self.fila_normal)} | "
            f"Preferencial: {len(self.fila_preferencial)}"
        )


# =============================
# MENU INTERATIVO
# =============================

fila = FilaAtendimento()

while True:
    print("\n=== SISTEMA DE FILA ===")
    print("1 - Gerar senha NORMAL")
    print("2 - Gerar senha PREFERENCIAL")
    print("3 - Atender próximo")
    print("4 - Mostrar filas")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("Senha gerada:", fila.gerar_senha_normal())

    elif opcao == "2":
        print("Senha gerada:", fila.gerar_senha_preferencial())

    elif opcao == "3":
        print(fila.atender_cliente())

    elif opcao == "4":
        print(fila.mostrar_filas())

    elif opcao == "5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")