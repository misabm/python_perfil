import random


TOTAL_CASAS = 130
CASAS_ESPECIAIS = 25
LARGURA = 10


def criar_tabuleiro():

    return set(

        random.sample(

            range(
                6,
                126
            ),

            CASAS_ESPECIAIS

        )

    )


def _peoes(
    jogadores,
    casa
):

    peoes = []

    for jogador in jogadores:

        if jogador.posicao == casa:

            peoes.append(

                jogador.nome[
                    :2
                ].upper()

            )

    return peoes


def _montar_casa(
    casa,
    jogadores,
    especiais,
    total
):

    peoes = _peoes(
        jogadores,
        casa
    )

    if casa >= total:

        texto = "🏆"

    elif casa in especiais:

        texto = " ?"

    else:

        texto = (
            f"{casa:03}"
        )

    if peoes:

        if len(
            peoes
        ) == 1:

            texto += peoes[0]

        else:

            texto += (
                "+"
                +
                str(
                    len(
                        peoes
                    )
                )
            )

    return f"[{texto:^7}]"


def desenhar_tabuleiro(
    jogadores,
    especiais,
    total_casas=130
):

    print()

    print(
        "═"
        *
        120
    )

    print(
        "PERFIL"
        .center(
            120
        )
    )

    print(
        "═"
        *
        120
    )

    legenda = []

    for jogador in jogadores:

        legenda.append(

            f"{jogador.nome[:2].upper()}"

            +

            " = "

            +

            jogador.nome

        )

    print()

    print(
        " | ".join(
            legenda
        )
    )

    print(
        "? = rodada especial"
    )

    print()

    linhas = []

    for inicio in range(

        1,

        total_casas
        +
        1,

        LARGURA

    ):

        fim = min(

            inicio
            +
            (
                LARGURA
                -
                1
            ),

            total_casas

        )

        linha = list(

            range(

                inicio,

                fim
                +
                1

            )

        )

        if (

            len(
                linhas
            )
            %
            2

        ):

            linha.reverse()

        linhas.append(
            linha
        )

    linhas.reverse()

    for linha in linhas:

        for casa in linha:

            print(

                _montar_casa(

                    casa,

                    jogadores,

                    especiais,

                    total_casas

                ),

                end=""

            )

        print()

        print()

    print(
        "═"
        *
        120
    )

    print()