import time
import random

from jogo.jogador import Jogador, Computador
from jogo.cartas import pegar_carta
from jogo.tabuleiro import criar_tabuleiro, desenhar_tabuleiro
from jogo.ranking import Ranking

POSICAO_FINAL = 130

def _ler_inteiro(prompt: str, validos: list = None) -> int:
    """Lê inteiro sem quebrar o programa com entrada inválida."""
    while True:
        try:
            valor = int(input(prompt).strip())
            if validos is None or valor in validos:
                return valor
            print(f"    Opção inválida. Escolha entre: {min(validos)} e {max(validos)}.")
        except (ValueError, EOFError):
            print("    Digite apenas números.")


def _ler_texto(prompt: str) -> str:
    """Lê uma string não vazia do terminal."""
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("    Não pode ser vazio.")


def _pausar():
    input("[ Pressione Enter para continuar ] ")


def _exibir_posicoes(jogadores: list):
    """Exibe barra de progresso de cada jogador."""
    print("┌─ Posições ──────────────────────────────────┐")
    for j in jogadores:
        progresso = int(j.posicao / POSICAO_FINAL * 30)
        barra = "█" * progresso + "░" * (30 - progresso)
        print(f"  │ {j.nome[:14]:<14} {j.posicao:3d}/130  {barra} │")
        print("  └─────────────────────────────────────────────┘")


def _aplicar_efeitos(texto: str, jogador_atual: Jogador, todos: list) -> bool:
    t = texto.lower()

    if "avance" in t and "casa" in t:
        try:
            num = int(next(s for s in t.split() if s.isdigit()))
            jogador_atual.posicao = min(
    POSICAO_FINAL,
    jogador_atual.posicao + num
)
            print(f"  ➜  {jogador_atual.nome} avançou {num} casa(s)! → posição {jogador_atual.posicao}")
        except StopIteration:
            pass
        return True

    if "volte" in t and "casa" in t:
        try:
            num = int(next(s for s in t.split() if s.isdigit()))
            jogador_atual.posicao = max(0, jogador_atual.posicao - num)
            print(f"  ➜  {jogador_atual.nome} voltou {num} casa(s)! → posição {jogador_atual.posicao}")
        except StopIteration:
            pass
        return True

    if "perca sua vez" in t:
        jogador_atual.perde_turno = True
        print(f"  ➜  {jogador_atual.nome} perde o próximo turno!")
        return True

    if "um palpite a qualquer hora" in t:
        jogador_atual.palpite_qualquer_hora = True
        print(f"  ➜  {jogador_atual.nome} ganhou um PALPITE A QUALQUER HORA!")
        return True

    if "escolha 1 jogador para" in t:
        _efeito_escolher_jogador(t, jogador_atual, todos)
        return True

    return False


def _efeito_escolher_jogador(texto: str, jogador_atual: Jogador, todos: list):
    """Efeito: escolha um jogador para avançar/voltar X casas."""
    outros = [j for j in todos if j is not jogador_atual]
    if not outros:
        return

    sinal = +1 if "avan" in texto else -1
    acao = "avançar" if sinal == 1 else "voltar"

    try:
        num = int(next(s for s in texto.split() if s.isdigit()))
    except StopIteration:
        num = 1

    print(f"🃏  {jogador_atual.nome} escolhe quem vai {acao} {num} casa(s):")
    for i, j in enumerate(outros, 1):
        print(f"       {i} - {j.nome}  (posição {j.posicao})")

    if jogador_atual.eh_humano:
        idx = _ler_inteiro("  Sua escolha: ", validos=list(range(1, len(outros) + 1))) - 1
    else:
        idx = 0
        time.sleep(0.8)
        print(f"  🤖  {jogador_atual.nome} escolheu {outros[idx].nome}")

    alvo = outros[idx]
    alvo.posicao = max(0, alvo.posicao + sinal * num)
    verbo = "avançou" if sinal == 1 else "voltou"
    print(f"  ➜  {alvo.nome} {verbo} {num} casa(s) → posição {alvo.posicao}")


def _dica_bloqueada_no_modo_especial(texto: str) -> bool:
    """Na casa '?', efeitos especiais são ignorados e a dica deve ser trocada."""
    t = texto.lower()
    bloqueios = (
        "avance",
        "volte",
        "perca sua vez",
        "um palpite a qualquer hora",
        "escolha 1 jogador para",
    )
    return any(item in t for item in bloqueios)


def _mostrar_dica_especial(carta: dict, indice: int) -> bool:
    """
    Mostra a dica da rodada especial.
    Retorna True se a dica pode valer normalmente, False se ela for bloqueada.
    """
    dica = carta["dicas"][indice - 1]
    if _dica_bloqueada_no_modo_especial(dica):
        print(f"  Dica {indice}: {dica}")
        print("  Essa dica tem efeito de carta e não vale na casa '?'. Escolha outro número.")
        return False

    print(f"  Dica {indice}: {dica}")
    return True


def _casas_por_acerto_no_especial(numero_da_dica: int) -> int:
    ganhos = {1: 10, 2: 8, 3: 6, 4: 4, 5: 2}
    return ganhos[numero_da_dica]


def _numeros_validos_no_especial(
    carta,
    usados
):

    retorno = []

    for i in range(
        1,
        21
    ):

        if i in usados:

            continue

        dica = carta[
            "dicas"
        ][
            i - 1
        ]

        if (
            _dica_bloqueada_no_modo_especial(
                dica
            )
        ):
            continue

        retorno.append(
            i
        )

    return retorno

def _verificar_palpite_qualquer_hora(jogador_atual, todos, carta, num_dica):
    for outro in todos:
        if outro is jogador_atual or not outro.palpite_qualquer_hora:
            continue

        if outro.eh_humano:
            print(f"⚡  {outro.nome}, você tem um PALPITE A QUALQUER HORA!")
            op = _ler_inteiro("     Quer usar agora? (1 = Sim / 2 = Não): ", validos=[1, 2])
            if op != 1:
                continue
            palpite = _ler_texto(f"  {outro.nome}, seu palpite: ")
            outro.palpite_qualquer_hora = False
            if palpite.lower() == carta["nome"].lower():
                casas = max(
    1,
    21 - num_dica
)
                outro.posicao += casas
                print(f"  ✅  {outro.nome} ACERTOU! +{casas} casas → posição {outro.posicao}")
                if outro.posicao >= POSICAO_FINAL:
                    return outro
            else:
                print(f"  ❌  {outro.nome} errou! Era: {carta['nome']}. Palpite perdido.")
        else:
            if outro.quer_palpitar(num_dica):
                outro.palpite_qualquer_hora = False
                casas = max(1, 20 - num_dica)
                outro.posicao += casas
                print(f" 🤖  {outro.nome} usou PALPITE A QUALQUER HORA! +{casas} → {outro.posicao}")
                if outro.posicao >= POSICAO_FINAL:
                    return outro
    return None

def rodada_normal(jogador, todos):

    if jogador.perde_turno:
        print(f"\n{jogador.nome} perdeu a vez.")
        jogador.perde_turno = False
        return None

    carta = pegar_carta()

    usadas = set()

    print("\n" + "═" * 60)
    print(f"VEZ DE {jogador.nome}")
    print(f"TIPO: {carta['tipo']}")
    print("═" * 60)

    for numero_dica in range(1, 21):

        # ==================================================
        # TURNO HUMANO
        # ==================================================
        if jogador.eh_humano:

            while True:

                if usadas:
                    print(f"\nDicas usadas: {sorted(usadas)}")

                escolha = _ler_inteiro(
                    "\nEscolha dica (0=palpite): ",
                    validos=list(range(21))
                )

                if escolha == 0:
                    break

                if escolha in usadas:
                    print("Essa dica já foi usada.")
                    continue

                usadas.add(escolha)

                dica = carta["dicas"][escolha - 1]

                print(f"\nDICA {escolha}")
                print(dica)

                _aplicar_efeitos(
                    dica,
                    jogador,
                    todos
                )

                vencedor = _verificar_palpite_qualquer_hora(
                    jogador,
                    todos,
                    carta,
                    numero_dica
                )

                if vencedor:
                    return vencedor

                break

            if escolha == 0:

                palpite = _ler_texto("\nPalpite: ")

                jogador.palpites += 1

                if palpite.lower() == carta["nome"].lower():

                    ganho = 21 - numero_dica

                    jogador.posicao += ganho

                    print(f"\n✅ ACERTOU! +{ganho}")

                    if jogador.posicao >= POSICAO_FINAL:
                        return jogador

                else:

                    print(f"\n❌ Errou. Era {carta['nome']}")

                return None

        # ==================================================
        # TURNO COMPUTADOR
        # ==================================================
        else:

            time.sleep(1)

            disponiveis = [
                i
                for i in range(1, 21)
                if i not in usadas
            ]

            escolha = random.choice(
                disponiveis
            )

            usadas.add(escolha)

            print(
                f"\n🤖 {jogador.nome} escolheu a dica {escolha}"
            )

            time.sleep(1)

            dica = carta["dicas"][escolha - 1]

            print(f"DICA {escolha}")
            print(dica)

            _aplicar_efeitos(
                dica,
                jogador,
                todos
            )

            vencedor = _verificar_palpite_qualquer_hora(
                jogador,
                todos,
                carta,
                numero_dica
            )

            if vencedor:
                return vencedor

            # ==========================
            # DIFICULDADE
            # ==========================

            base = {
                "facil": 0.03,
                "normal": 0.10,
                "dificil": 0.18
            }

            chance = (
                base.get(
                    jogador.dificuldade,
                    0.10
                )
                +
                (
                    numero_dica * 0.05
                )
            )

            chance = min(
                chance,
                0.95
            )

            if random.random() < chance:

                print(
                    f"\n🤖 {jogador.nome} resolveu palpitar..."
                )

                time.sleep(1)

                acertou = (
                    random.random()
                    <
                    chance
                )

                jogador.palpites += 1

                if acertou:

                    ganho = (
                        21
                        -
                        numero_dica
                    )

                    jogador.posicao += ganho

                    print(
                        f"✅ {jogador.nome} ACERTOU! +{ganho}"
                    )

                    if (
                        jogador.posicao
                        >=
                        POSICAO_FINAL
                    ):
                        return jogador

                else:

                    print(
                        f"❌ {jogador.nome} errou."
                    )

                return None

    print(
        f"\n🤖 {jogador.nome} usou todas as dicas e errou."
    )

    return None

def rodada_extra(jogador: Jogador, todos: list):
    """
    Rodada especial da casa '?'.
    Até 5 dicas, 1 único palpite.
    Casas: 1ª=10 | 2ª=8 | 3ª=6 | 4ª=4 | 5ª=2

    # TODO – configurar o '?' completamente (responsável tarefa 5)
    """
    if jogador.perde_turno:
        print(f"{jogador.nome} perdeu este turno!")
        jogador.perde_turno = False
        return None

    carta = pegar_carta()
    dicas_escolhidas = set()
    dicas_validas = 0

    print(f"{'═' * 54}")
    print(f"  ❓  CARTA ESPECIAL  —  {jogador.nome}")
    print(f"  Tipo: {carta['tipo']}")
    print("  Regras: até 5 dicas válidas, apenas 1 palpite.")
    print("  Dicas com efeitos de carta são bloqueadas aqui.")
    print("  Acerto: 1ª=10 | 2ª=8 | 3ª=6 | 4ª=4 | 5ª=2 casas")
    print(f"  {'═' * 54}")

    while dicas_validas < 5:
        numero_da_dica = dicas_validas + 1

        if jogador.eh_humano:
            print(f"Dicas escolhidas até agora: {sorted(dicas_escolhidas) if dicas_escolhidas else 'nenhuma'}")

            if numero_da_dica == 5:
                print("5ª dica válida: escolha um número e depois o palpite será obrigatório.")
                escolha = _ler_inteiro("  Escolha a última dica (1-20): ", validos=list(range(1, 21)))
            else:
                print(f"Dica válida {numero_da_dica}/5. Digite um número de 1 a 20 ou 0 para palpitar:")
                escolha = _ler_inteiro("  > ", validos=list(range(0, 21)))

                if escolha == 0:
                    palpite = _ler_texto("  Seu palpite: ")
                    jogador.palpites += 1
                    if palpite.lower() == carta["nome"].lower():
                        casas = _casas_por_acerto_no_especial(numero_da_dica)
                        jogador.posicao += casas
                        print(f"  ✅  Acertou! +{casas} casas → posição {jogador.posicao}")
                        return jogador if jogador.posicao >= POSICAO_FINAL else None
                    print(f"  ❌  Errou! Era: {carta['nome']}. Não anda nada.")
                    return None

            if escolha in dicas_escolhidas:
                print("  Esse número já foi escolhido nessa rodada especial. Tente outro.")
                continue

            if not _mostrar_dica_especial(carta, escolha):
                continue

            dicas_escolhidas.add(escolha)
            dicas_validas += 1
            if dicas_validas == 5:
                palpite = _ler_texto("  Palpite final obrigatório: ")
                jogador.palpites += 1
                if palpite.lower() == carta["nome"].lower():
                    casas = _casas_por_acerto_no_especial(5)
                    jogador.posicao += casas
                    print(f"  ✅  Acertou! +{casas} casas → posição {jogador.posicao}")
                    return jogador if jogador.posicao >= POSICAO_FINAL else None
                print(f"  ❌  Errou! Era: {carta['nome']}. Não anda nada.")
                return None

        else:
            time.sleep(0.5)
            numeros_disponiveis = _numeros_validos_no_especial(carta, dicas_escolhidas)
            if not numeros_disponiveis:
                print("  Não há mais dicas válidas nessa carta especial. Rodada encerrada sem avanço.")
                return None

            if numero_da_dica == 5:
                escolha = numeros_disponiveis[0]
                dicas_escolhidas.add(escolha)
                _mostrar_dica_especial(carta, escolha)
                dicas_validas += 1
                chance = min(0.08 + 0.18 * (numero_da_dica - 1), 0.95)
                acertou = random.random() < chance
                print(f"  🤖  {jogador.nome} é obrigado a palpitar.")
                time.sleep(0.4)
                if acertou:
                    casas = _casas_por_acerto_no_especial(5)
                    jogador.posicao += casas
                    print(f"  ✅  Acertou! +{casas} casas → posição {jogador.posicao}")
                    return jogador if jogador.posicao >= POSICAO_FINAL else None
                print(f"  ❌  Errou! Era: {carta['nome']}")
                return None

            chance = 0.08 + 0.18 * (numero_da_dica - 1)
            if random.random() < chance:
                acertou = random.random() < chance
                print(f"  🤖  {jogador.nome} vai palpitar na dica válida {numero_da_dica}...")
                time.sleep(0.4)
                if acertou:
                    casas = _casas_por_acerto_no_especial(numero_da_dica)
                    jogador.posicao += casas
                    print(f"  ✅  Acertou! +{casas} casas → posição {jogador.posicao}")
                    return jogador if jogador.posicao >= POSICAO_FINAL else None
                print(f"  ❌  Errou! Era: {carta['nome']}")
                return None

            escolha = numeros_disponiveis[0]
            dicas_escolhidas.add(escolha)
            _mostrar_dica_especial(carta, escolha)
            dicas_validas += 1

    return None

def _configurar_multiplayer() -> list:
    """Coleta nicks de 2 a 6 jogadores humanos."""
    print("  ╔══════════════════════════════════╗")
    print("  ║       MODO MULTIPLAYER           ║")
    print("  ╚══════════════════════════════════╝")

    qtd = _ler_inteiro("Quantas pessoas vão jogar? (2-6): ",
    validos=list(range(2, 7)))
    
    jogadores = []
    nicks_usados = set()

    for i in range(1, qtd + 1):
        while True:
            nick = input(f"  Nick do jogador {i}: ").strip()
            if not nick:
                print("  Nick não pode ser vazio.")
            elif nick.lower() in nicks_usados:
                print("  Esse nick já está em uso.")
            else:
                nicks_usados.add(nick.lower())
                jogadores.append(Jogador(nick))
                break

    return jogadores


def _configurar_vs_computador() -> list:
    """Coleta nick do humano e dificuldade do computador."""
    print("  ╔══════════════════════════════════╗")
    print("  ║      MODO VS COMPUTADOR          ║")
    print("  ╚══════════════════════════════════╝")

    nick = _ler_texto(" Seu nick: ")
    
    print("Dificuldade do computador:")
    print("    1 - Fácil   (acerta raramente no começo)")
    print("    2 - Normal  (equilibrado)")
    print("    3 - Difícil (acerta desde as primeiras dicas)")
    op = _ler_inteiro("  Escolha: ", validos=[1, 2, 3])
    dificuldades = {1: "facil", 2: "normal", 3: "dificil"}

    return [Jogador(nick), Computador(dificuldade=dificuldades[op])]

def _loop_jogo(jogadores):

    especiais = criar_tabuleiro()

    turno = 0

    print("\nJogo iniciado.")
    print(f"Objetivo: chegar na casa {POSICAO_FINAL}")

    _pausar()

    while True:

        jogador_atual = jogadores[
            turno % len(jogadores)
        ]

        _exibir_posicoes(
            jogadores
        )

        desenhar_tabuleiro(
            jogadores,
            especiais,
            total_casas=POSICAO_FINAL
        )

        vencedor = None

        if (
            jogador_atual.posicao
            in especiais
        ):

            vencedor = rodada_extra(
                jogador_atual,
                jogadores
            )

        else:

            vencedor = rodada_normal(
                jogador_atual,
                jogadores
            )

        if (
            vencedor
            and vencedor.posicao >= POSICAO_FINAL
        ):

            _exibir_posicoes(
                jogadores
            )

            print(
                f"\n🏆 {vencedor.nome} venceu!"
            )

            return vencedor

        if (
            jogador_atual.posicao
            >= POSICAO_FINAL
        ):

            _exibir_posicoes(
                jogadores
            )

            print(
                f"\n🏆 {jogador_atual.nome} venceu!"
            )

            return jogador_atual

        turno += 1

        _pausar()

def iniciar_jogo() -> bool:
    """
    Exibe menu de modos e inicia o jogo.
    Retorna True se o vencedor for humano (compatível com o main.py original).

    # TODO – adicionar opção Tutorial aqui
    # TODO – integrar ranking após o jogo 
    """
    print("  ╔════════════════════════════════════════════════════╗")
    print("  ║                   🎲  PERFIL  🎲                   ║")
    print("  ╠════════════════════════════════════════════════════╣")
    print("  ║  1 - Solo                                          ║")
    print("  ║      Jogue sozinho e avance pelo tabuleiro.        ║")
    print("  ║  2 - Multiplayer                                   ║")
    print("  ║      De 2 a 6 jogadores, cada um com seu nick.     ║")
    print("  ║  3 - VS Computador                                 ║")
    print("  ║      Enfrente o computador em dificuldade livre.   ║")
    print("  ╚════════════════════════════════════════════════════╝")

    op = _ler_inteiro("  Modo: ", validos=[1, 2, 3])

    if op == 1:
        nick = input("  Seu nick: ").strip() or "Jogador"
        jogadores = [Jogador(nick)]
    elif op == 2:
        jogadores = _configurar_multiplayer()
    else:
        jogadores = _configurar_vs_computador()

    vencedor = _loop_jogo(jogadores)

    # Monta o resultado: vencedor primeiro, demais ordenados por posição no tabuleiro
    outros = sorted([j for j in jogadores if j is not vencedor],
                    key=lambda j: j.posicao, reverse=True)
    resultado = [(vencedor.nome, True)] + [(j.nome, False) for j in outros]

    ranking = Ranking()
    ranking.mostrar_pontos_partida(resultado)
    ranking.registrar_partida(resultado)
    ranking.mostrar_ranking()

    return vencedor.eh_humano

def validar_numero_dica(
    valor,
    usados
):

    if valor < 0:

        return False

    if valor > 20:

        return False

    if valor in usados:

        return False

    return True