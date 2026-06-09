from jogo.engine import iniciar_jogo

# ─────────────────────────────────────────────────────────────────────────────
# main.py — ponto de entrada do programa (original preservado)
#
# TODO – deixar o menu mais bonito (responsável tarefa 2)
# TODO – integrar ranking de vitórias (Mari, tarefa 6)
# ─────────────────────────────────────────────────────────────────────────────

def menu():
    vitorias = 0
    while True:
        print("\n1 - Jogar")
        print("2 - Sair")
        op = input("Escolha: ")

        if op == "1":
            ganhou = iniciar_jogo()
            if ganhou:
                vitorias += 1
                print("Vitórias:", vitorias)
        elif op == "2":
            break

menu()
