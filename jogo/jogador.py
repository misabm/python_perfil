import random


class Jogador:
    """Representa um participante da partida."""

    TOTAL_CASAS = 130

    def __init__(self, nome="Jogador"):

        nome = str(nome).strip()

        if not nome:

            nome = "Jogador"

        self.nome = nome

        self.posicao = 0

        self.palpites = 0

        self.eh_humano = True

        self.perde_turno = False

        self.palpite_qualquer_hora = False

        self.acertou_ultima = False

    def __str__(self):

        return self.nome

    def mover(
        self,
        quantidade
    ):

        self.posicao += quantidade

        if self.posicao < 0:

            self.posicao = 0

    def voltar(
        self,
        quantidade
    ):

        self.mover(
            -quantidade
        )

    def avancar(
        self,
        quantidade
    ):

        self.mover(
            quantidade
        )

    def ganhou(self):

        return (

            self.posicao

            >=

            self.TOTAL_CASAS

        )

    def dar_palpite_extra(self):

        self.palpite_qualquer_hora = True

    def consumir_palpite_extra(self):

        self.palpite_qualquer_hora = False

    def perder_turno(self):

        self.perde_turno = True

    def restaurar_turno(self):

        self.perde_turno = False


class Computador(
    Jogador
):

    """
    Fácil:
        começa errando quase tudo

    Normal:
        cresce equilibrado

    Difícil:
        arrisca cedo
    """

    _CONFIG = {

        "facil": {

            "base": 0.01,

            "incremento": 0.025

        },

        "normal": {

            "base": 0.03,

            "incremento": 0.045

        },

        "dificil": {

            "base": 0.08,

            "incremento": 0.065

        }

    }

    def __init__(
        self,
        dificuldade="normal"
    ):

        super().__init__(

            nome="Computador"

        )

        self.eh_humano = False

        self.dificuldade = (
            dificuldade
            .lower()
            .strip()
        )

        cfg = (

            self._CONFIG.get(

                self.dificuldade,

                self._CONFIG[
                    "normal"
                ]

            )

        )

        self._base = cfg[
            "base"
        ]

        self._incremento = cfg[
            "incremento"
        ]

    def chance_de_acertar(
        self,
        dica
    ):

        chance = (

            self._base

            +

            self._incremento

            *

            (

                dica
                -
                1

            )

        )

        return min(

            chance,

            0.95

        )

    def quer_palpitar(
        self,
        dica
    ):

        return (

            random.random()

            <

            self.chance_de_acertar(

                dica

            )

        )

    def escolher_dica(
        self,
        usadas
    ):

        disponiveis = []

        for i in range(
            1,
            21
        ):

            if i not in usadas:

                disponiveis.append(
                    i
                )

        return random.choice(
            disponiveis
        )