import random

class Jogador:
    """Representa um jogador humano."""

    def __init__(self, nome="Jogador"):
        # atributos originais
        self.posicao = 0
        self.palpites = 0

        # atributos adicionados
        self.nome = nome                    # nick do jogador
        self.eh_humano = True               # distingue de Computador
        self.perde_turno = False            # ativado por "Perca sua vez"
        self.palpite_qualquer_hora = False  # ativado pela dica especial

    def __str__(self):
        return self.nome


class Computador(Jogador):
    """
    Jogador Computado!
    Chance de acertar cresce a cada dica revelada.

    Dificuldades:
        facil   → começa em  2%, +3% por dica  (~59% na dica 20)
        normal  → começa em  4%, +5% por dica  (~99% na dica 20)
        dificil → começa em  8%, +7% por dica  (acerta cedo)
    """

    _CONFIGS = {
        "facil":   {"base": 0.02, "incremento": 0.03},
        "normal":  {"base": 0.04, "incremento": 0.05},
        "dificil": {"base": 0.08, "incremento": 0.07},
    }

    def __init__(self, dificuldade="normal"):
        super().__init__(nome="Computador")
        self.eh_humano = False
        self.dificuldade = dificuldade
        cfg = self._CONFIGS.get(dificuldade, self._CONFIGS["normal"])
        self._base = cfg["base"]
        self._incremento = cfg["incremento"]

    def chance_de_acertar(self, num_dica: int) -> float:
        """Probabilidade de arriscar palpite nesta dica (1-indexed)."""
        return min(self._base + self._incremento * (num_dica - 1), 0.97)

    def quer_palpitar(self, num_dica: int) -> bool:
        """Retorna True se o computador decidir arriscar palpite agora."""
        return random.random() < self.chance_de_acertar(num_dica)