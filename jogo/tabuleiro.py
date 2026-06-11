import random


def criar_tabuleiro():
    especiais = random.sample(range(1, 130), 25)
    return especiais


def desenhar_tabuleiro(jogadores: list, especiais: list, total_casas: int = 130):
    """
    Mostra um tabuleiro em zigue-zague com:
    - casas especiais '?'
    - peões dos jogadores
    - casa final destacada
    """
    largura = 10
    ocupacao = {}

    for indice, jogador in enumerate(jogadores, start=1):
        posicao = min(max(jogador.posicao, 0), total_casas)
        marcador = jogador.nome[:2].upper() if jogador.nome else str(indice)
        ocupacao.setdefault(posicao, []).append(marcador)

    legenda_jogadores = " | ".join(
        f"{(jogador.nome[:2].upper() if jogador.nome else str(indice))}={jogador.nome}"
        for indice, jogador in enumerate(jogadores, start=1)
    )

    print("\n╔" + "═" * 78 + "╗")
    print("║" + " TABULEIRO ".center(78) + "║")
    print("╠" + "═" * 78 + "╣")
    print("║ Legenda: ? = casa especial | [AB] = peão do jogador".ljust(79) + "║")
    print(f"║ {legenda_jogadores[:76].ljust(76)} ║")
    print("╚" + "═" * 78 + "╝")

    linhas = []
    for inicio in range(1, total_casas + 1, largura):
        fim = min(inicio + largura - 1, total_casas)
        linha = list(range(inicio, fim + 1))
        if len(linhas) % 2 == 1:
            linha.reverse()
        linhas.append(linha)

    for linha in reversed(linhas):
        blocos = []
        for casa in linha:
            if casa == total_casas:
                base = " FIM "
            elif casa in especiais:
                base = "  ?  "
            else:
                base = f"{casa:>4} "

            jogadores_na_casa = ocupacao.get(casa, [])
            if jogadores_na_casa:
                if len(jogadores_na_casa) == 1:
                    peao = jogadores_na_casa[0][:2].ljust(2)
                else:
                    peao = str(len(jogadores_na_casa)).rjust(2)
                bloco = f"[{peao}]"
            else:
                bloco = "     "

            blocos.append(f"{base}{bloco}")

        print(" ".join(blocos))

    aguardando = ocupacao.get(0, [])
    if aguardando:
        print("\nNa largada:", ", ".join(aguardando))
