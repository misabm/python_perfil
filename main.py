from jogo.engine import iniciar_jogo
from jogo.ranking import Ranking

# ─────────────────────────────────────────────────────────────────────────────
# main.py — ponto de entrada do programa (original preservado)
#
# TODO – deixar o menu mais bonito (responsável tarefa 2)
# ─────────────────────────────────────────────────────────────────────────────

def menu():
    vitorias = 0
    while True:
        print("\n1 - Jogar")
        print("2 - Ver Ranking")
        print("3 - Sair")
        op = input("Escolha: ")

        if op == "1":
            ganhou = iniciar_jogo()
            if ganhou:
                vitorias += 1
                print("Vitórias nesta sessão:", vitorias)
        elif op == "2":
            Ranking().mostrar_ranking()
        elif op == "3":
            break

menu()
