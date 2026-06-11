from jogo.engine import iniciar_jogo
from jogo.ranking import Ranking
from jogo.tutorial import mostrar_tutorial

from jogo.utils.entrada import (
    ler_inteiro
)

from jogo.utils.terminal import (
    limpar,
    pausar,
    titulo
)


def mostrar_menu():

    titulo(
        "PERFIL"
    )

    print()

    print(
        "[1] Jogar"
    )

    print(
        "[2] Tutorial"
    )

    print(
        "[3] Ranking"
    )

    print(
        "[4] Sair"
    )

    print()


def abrir_ranking():

    limpar()

    titulo(
        "RANKING"
    )

    Ranking().mostrar_ranking()

    pausar()


def abrir_tutorial():

    limpar()

    mostrar_tutorial()

    pausar()


def jogar():

    limpar()

    resultado = iniciar_jogo()

    if resultado:

        print()

        print(
            "Partida encerrada."
        )

    pausar()


def menu():

    while True:

        limpar()

        mostrar_menu()

        opcao = ler_inteiro(

            "\nEscolha: ",

            1,

            4

        )

        if opcao == 1:

            jogar()

        elif opcao == 2:

            abrir_tutorial()

        elif opcao == 3:

            abrir_ranking()

        else:

            limpar()

            titulo(
                "ATÉ LOGO"
            )

            break


if __name__ == "__main__":

    menu()