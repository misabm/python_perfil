# ranking.py — Sistema de Ranking do Jogo Perfil
#
# Como usar:
#   from jogo.ranking import Ranking
#   r = Ranking()
#   r.registrar_partida([("Ana", True), ("Bob", False), ("Carlos", False)])
#   r.mostrar_ranking()

import json
import os

# Arquivo onde os dados ficam salvos entre as partidas
ARQUIVO_RANKING = "ranking.json"

# Pontos ganhos por posição ao final da partida
PONTOS_POR_POSICAO = {
    1: 100,   # Vencedor
    2: 60,    # 2º lugar
    3: 40,    # 3º lugar
    4: 25,    # 4º lugar
    5: 15,    # 5º lugar
    6: 10,    # 6º lugar
}


class JogadorRanking:
    """Guarda o histórico de pontos de um jogador."""

    def __init__(self, nome):
        self.nome = nome
        self.pontos_totais = 0
        self.partidas_jogadas = 0
        self.vitorias = 0

    def adicionar_pontos(self, pontos):
        """Soma pontos e conta mais uma partida."""
        self.pontos_totais += pontos
        self.partidas_jogadas += 1

    def para_dict(self):
        """Converte o jogador para dicionário (necessário para salvar no JSON)."""
        return {
            "nome": self.nome,
            "pontos_totais": self.pontos_totais,
            "partidas_jogadas": self.partidas_jogadas,
            "vitorias": self.vitorias,
        }

    @classmethod
    def do_dict(cls, dados):
        """Cria um JogadorRanking a partir de um dicionário lido do JSON."""
        jogador = cls(dados["nome"])
        jogador.pontos_totais = dados.get("pontos_totais", 0)
        jogador.partidas_jogadas = dados.get("partidas_jogadas", 0)
        jogador.vitorias = dados.get("vitorias", 0)
        return jogador


class Ranking:
    """Gerencia o ranking completo: carrega, salva e exibe."""

    def __init__(self):
        # Dicionário: nome do jogador -> JogadorRanking
        self.jogadores = {}
        self.carregar_ranking()

    def carregar_ranking(self):
        """Lê o arquivo ranking.json e carrega os dados."""
        try:
            if os.path.exists(ARQUIVO_RANKING):
                with open(ARQUIVO_RANKING, "r", encoding="utf-8") as f:
                    lista = json.load(f)
                for item in lista:
                    j = JogadorRanking.do_dict(item)
                    self.jogadores[j.nome] = j
        except (json.JSONDecodeError, IOError):
            # Se o arquivo estiver corrompido, começa do zero sem quebrar
            self.jogadores = {}

    def salvar_ranking(self):
        """Salva todos os dados no arquivo ranking.json."""
        try:
            lista = [j.para_dict() for j in self.jogadores.values()]
            with open(ARQUIVO_RANKING, "w", encoding="utf-8") as f:
                json.dump(lista, f, ensure_ascii=False, indent=2)
        except IOError:
            print("  Aviso: não foi possível salvar o ranking.")

    def registrar_partida(self, resultado):
        """
        Registra os pontos de uma partida.

        Parâmetro resultado: lista de tuplas (nome, eh_vencedor)
            - O primeiro item é o vencedor (posição 1)
            - Os demais estão em ordem decrescente de posição no tabuleiro
            - Jogadores chamados "Computador" são ignorados

        Exemplo: [("Ana", True), ("Bob", False), ("Carlos", False)]
        """
        for pos_ranking, (nome, eh_vencedor) in enumerate(resultado, start=1):
            # O Computador não entra no ranking (não tem identidade persistente)
            if nome.lower() == "computador":
                continue

            pontos = PONTOS_POR_POSICAO.get(pos_ranking, 5)

            # Cria o jogador no ranking se ainda não existir
            if nome not in self.jogadores:
                self.jogadores[nome] = JogadorRanking(nome)

            self.jogadores[nome].adicionar_pontos(pontos)

            if eh_vencedor:
                self.jogadores[nome].vitorias += 1

        self.salvar_ranking()

    def mostrar_ranking(self):
        """Exibe o ranking em ordem decrescente de pontos totais."""
        # Filtra só jogadores humanos (exclui Computador, caso haja algum salvo)
        humanos = [j for j in self.jogadores.values() if j.nome.lower() != "computador"]

        if not humanos:
            print("\n  Nenhum dado de ranking ainda. Jogue uma partida!")
            return

        # Ordena do maior para o menor
        lista = sorted(humanos, key=lambda j: j.pontos_totais, reverse=True)

        print("\n  ╔══════════════════════════════════════════════════════╗")
        print("  ║                  🏆  RANKING  🏆                    ║")
        print("  ╠═════╦══════════════════╦═════════╦══════════╦═══════╣")
        print("  ║ Pos ║ Jogador          ║ Pontos  ║ Partidas ║ Vitór.║")
        print("  ╠═════╬══════════════════╬═════════╬══════════╬═══════╣")

        for i, j in enumerate(lista, start=1):
            nome_fmt = j.nome[:16].ljust(16)
            print(f"  ║ {i:<3} ║ {nome_fmt} ║ {j.pontos_totais:<7} ║ {j.partidas_jogadas:<8} ║ {j.vitorias:<5} ║")

        print("  ╚═════╩══════════════════╩═════════╩══════════╩═══════╝")

    def mostrar_pontos_partida(self, resultado):
        """Mostra os pontos ganhos nesta partida antes de salvar."""
        print("\n  ── Pontos desta partida ──")
        for pos_ranking, (nome, _) in enumerate(resultado, start=1):
            if nome.lower() == "computador":
                continue
            pontos = PONTOS_POR_POSICAO.get(pos_ranking, 5)
            print(f"  {pos_ranking}º lugar: {nome}  →  +{pontos} pontos")


# ─────────────────────────────────────────────────────────────────────────────
# Exemplo de uso (executar diretamente para testar)
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Teste do sistema de ranking ===\n")

    r = Ranking()

    # Simula uma partida com 3 jogadores
    print("Partida 1: Ana vence, Bob fica em 2º, Carlos em 3º")
    r.mostrar_pontos_partida([("Ana", True), ("Bob", False), ("Carlos", False)])
    r.registrar_partida([("Ana", True), ("Bob", False), ("Carlos", False)])

    # Simula outra partida
    print("\nPartida 2: Bob vence, Ana fica em 2º")
    r.mostrar_pontos_partida([("Bob", True), ("Ana", False)])
    r.registrar_partida([("Bob", True), ("Ana", False)])

    print()
    r.mostrar_ranking()
    print("\nDados salvos em:", ARQUIVO_RANKING)
