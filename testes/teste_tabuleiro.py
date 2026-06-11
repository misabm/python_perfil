from jogo.tabuleiro import (
    criar_tabuleiro,
    desenhar_tabuleiro
)


class JogadorFake:

    def __init__(
        self,
        nome,
        posicao
    ):

        self.nome = nome
        self.posicao = posicao


def teste_criar_tabuleiro():

    especiais = criar_tabuleiro()

    assert len(
        especiais
    ) == 25

    assert all(
        6 <= c <= 125
        for c in especiais
    )


def teste_desenhar_tabuleiro():

    jogadores = [

        JogadorFake(
            "Ana",
            10
        ),

        JogadorFake(
            "Carlos",
            35
        )

    ]

    especiais = {

        20,
        40
    }

    desenhar_tabuleiro(
        jogadores,
        especiais
    )

    assert True