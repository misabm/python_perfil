from jogo.jogador import Jogador
from jogo.cartas import pegar_carta
from jogo.tabuleiro import criar_tabuleiro


def aplicar_efeitos(texto, jogador):
    texto = texto.lower()

    if "avance" in texto and "casas" in texto:
        try:
            num = int([s for s in texto.split() if s.isdigit()][0])
            jogador.posicao += num
            print(f"Avançou {num} casas!")
        except:
            pass

    elif "volte" in texto and "casas" in texto:
        try:
            num = int([s for s in texto.split() if s.isdigit()][0])
            jogador.posicao -= num
            print(f"Voltou {num} casas!")
        except:
            pass

    elif "perca sua vez" in texto:
        jogador.perde_turno = True
        print("Você perderá o próximo turno!")

    # "um palpite a qualquer hora" -> ignorado por enquanto


def rodada_normal(jogador):
    if getattr(jogador, "perde_turno", False):
        print("Você perdeu este turno!")
        jogador.perde_turno = False
        return

    carta = pegar_carta()
    print("\nTipo:", carta["tipo"])

    for i in range(20):
        escolha = int(input("Escolha dica 1-20: "))
        dica = carta["dicas"][escolha-1]
        print(dica)

        # aplica efeito da dica automaticamente
        aplicar_efeitos(dica, jogador)

        palpite = input("Palpite: ")
        jogador.palpites += 1

        if palpite.lower() == carta["nome"].lower():
            casas = 20 - (i+1)
            jogador.posicao += casas
            print("Acertou! Andou", casas)
            return


def rodada_extra(jogador):
    if getattr(jogador, "perde_turno", False):
        print("Você perdeu este turno!")
        jogador.perde_turno = False
        return

    carta = pegar_carta()
    print("\nCARTA EXTRA")

    for i in range(5):
        escolha = int(input("Escolha dica 1-20: "))
        dica = carta["dicas"][escolha-1]
        print(dica)

        aplicar_efeitos(dica, jogador)

        palpite = input("Palpite: ")
        jogador.palpites += 1

        if palpite.lower() == carta["nome"].lower():
            ganhos = [10, 8, 6, 4, 2]
            jogador.posicao += ganhos[i]
            print("Acertou!")
            return


def iniciar_jogo():
    jogador = Jogador()
    especiais = criar_tabuleiro()

    while jogador.posicao < 130:
        print("\nPosição:", jogador.posicao)

        if jogador.posicao in especiais:
            rodada_extra(jogador)
        else:
            rodada_normal(jogador)

    print("Você venceu!")
    return True