from jogo.cartas import pegar_carta


def teste():

    carta = pegar_carta()

    assert "nome" in carta
    assert len(carta["dicas"]) == 20

    print("OK")


teste()