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
        print("\n  ╔════════════════════════════════════════════════════╗")
        print("  ║                 LABORATÓRIO PERFIL                ║")
        print("  ╠════════════════════════════════════════════════════╣")
        print("  ║  1 - Jogar                                        ║")
        print("  ║      Começar uma nova partida.                    ║")
        print("  ║  2 - Ver Ranking                                  ║")
        print("  ║      Conferir a pontuação acumulada.              ║")
        print("  ║  3 - Sair                                         ║")
        print("  ╚════════════════════════════════════════════════════╝")
        op = input("Escolha uma opção: ").strip()

        if op == "1":
            ganhou = iniciar_jogo()
            if ganhou:
                vitorias += 1
            print(f"Vitórias nesta sessão: {vitorias}")
        elif op == "2":
            Ranking().mostrar_ranking()
        elif op == "3":
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")

menu()
