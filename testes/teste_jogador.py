from jogo.jogador import Jogador


def teste():

    j = Jogador("Allyn")

    assert j.posicao == 0
    assert j.nome == "Allyn"

    print("OK")


teste()