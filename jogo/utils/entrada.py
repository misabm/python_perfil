def ler_inteiro(
    mensagem,
    minimo=None,
    maximo=None,
    validos=None
):

    while True:

        entrada = input(
            mensagem
        ).strip()

        try:

            numero = int(
                entrada
            )

        except ValueError:

            print(
                "\nDigite apenas números."
            )

            continue

        if (
            validos
            and numero not in validos
        ):

            print(
                "\nOpção inválida."
            )

            continue

        if (
            minimo is not None
            and numero < minimo
        ):

            print(
                f"\nDigite valor ≥ {minimo}"
            )

            continue

        if (
            maximo is not None
            and numero > maximo
        ):

            print(
                f"\nDigite valor ≤ {maximo}"
            )

            continue

        return numero


def ler_texto(
    mensagem,
    tamanho_min=1,
    tamanho_max=20
):

    while True:

        texto = input(
            mensagem
        ).strip()

        if len(texto) < tamanho_min:

            print(
                "\nTexto muito curto."
            )

            continue

        if len(texto) > tamanho_max:

            print(
                "\nTexto muito grande."
            )

            continue

        return texto


def ler_dica(
    usadas
):

    while True:

        numero = ler_inteiro(
            "\nEscolha dica (0–20): ",
            0,
            20
        )

        if numero in usadas:

            print(
                "\nEssa dica já foi usada."
            )

            continue

        return numero