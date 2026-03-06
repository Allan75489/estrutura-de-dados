
# ==========================================
# TABELA HASH COM ENCADEAMENTO
# ==========================================

class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
        self.quantidade = 0

    # =========================
    # Função hash
    # =========================
    def funcao_hash(self, chave):
        return hash(chave) % self.tamanho

    # =========================
    # Fator de carga
    # =========================
    def fator_carga(self):
        return self.quantidade / self.tamanho

    # =========================
    # Rehash (resize)
    # =========================
    def _rehash(self):
        print("⚠️ Rehashing... aumentando tabela")

        tabela_antiga = self.tabela
        self.tamanho *= 2
        self.tabela = [[] for _ in range(self.tamanho)]
        self.quantidade = 0

        for bucket in tabela_antiga:
            for chave, valor in bucket:
                self.inserir(chave, valor)

    # =========================
    # Inserir (VERSÃO OTIMIZADA)
    # =========================
    def inserir(self, chave, valor):
        indice = self.funcao_hash(chave)
        bucket = self.tabela[indice]

        # 🔄 Atualiza se já existir
        for i, (k, v) in enumerate(bucket):
            if k == chave:
                bucket[i] = (chave, valor)
                return

        # 🚨 Verifica carga apenas se for novo
        if (self.quantidade + 1) / self.tamanho > 0.75:
            self._rehash()
            indice = self.funcao_hash(chave)
            bucket = self.tabela[indice]

        bucket.append((chave, valor))
        self.quantidade += 1

    # =========================
    # Buscar
    # =========================
    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        bucket = self.tabela[indice]

        for k, v in bucket:
            if k == chave:
                return v
        return None

    # =========================
    # Existe
    # =========================
    def existe(self, chave):
        return self.buscar(chave) is not None

    # =========================
    # Remover
    # =========================
    def remover(self, chave):
        indice = self.funcao_hash(chave)
        bucket = self.tabela[indice]

        for i, (k, v) in enumerate(bucket):
            if k == chave:
                del bucket[i]
                self.quantidade -= 1
                return True
        return False

    # =========================
    # Exibir tabela (melhorado)
    # =========================
    def exibir(self):
        print("\n🗂️ ESTADO DA TABELA")
        for i, bucket in enumerate(self.tabela):
            print(f"Índice {i}: {bucket}")

    # =========================
    # Informações
    # =========================
    def info(self):
        print("\n📊 INFORMAÇÕES DA TABELA")
        print(f"Tamanho da tabela: {self.tamanho}")
        print(f"Elementos armazenados: {self.quantidade}")
        print(f"Fator de carga: {self.fator_carga():.2f}")

    # ==================================
    # MÉTODOS MÁGICOS (estilo dict)
    # ==================================
    def __setitem__(self, chave, valor):
        self.inserir(chave, valor)

    def __getitem__(self, chave):
        valor = self.buscar(chave)
        if valor is None:
            raise KeyError(chave)
        return valor

    def __contains__(self, chave):
        return self.existe(chave)

    def __len__(self):
        return self.quantidade


# ==========================================
# TESTE PROFISSIONAL
# ==========================================

if __name__ == "__main__":
    tabela = TabelaHash(5)

    # Inserção normal
    tabela.inserir("nome", "Allan")
    tabela.inserir("idade", 20)

    # Inserção estilo dict 🔥
    tabela["cidade"] = "Guarabira"
    tabela["linguagem"] = "Python"

    print("Buscar nome:", tabela.buscar("nome"))
    print("Acessando como dict:", tabela["cidade"])

    if "idade" in tabela:
        print("✅ 'idade' existe na tabela")

    print("Tamanho:", len(tabela))

    tabela.exibir()
    tabela.info()