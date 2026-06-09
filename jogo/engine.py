import time
import random

from jogo.jogador import Jogador, Computador
from jogo.cartas import pegar_carta
from jogo.tabuleiro import criar_tabuleiro

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
            jogador_atual.posicao += num
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
                casas = max(1, 20 - num_dica)
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

def rodada_normal(jogador: Jogador, todos: list):
    """Rodada padrão (casa comum). Retorna vencedor ou None."""
    if jogador.perde_turno:
        print(f"{jogador.nome} perdeu este turno!")
        jogador.perde_turno = False
        return None

    carta = pegar_carta()
    print(f"{'─' * 54}")
    print(f"  🎴  Vez de {jogador.nome}   |   Posição: {jogador.posicao}")
    print(f"  Tipo da carta: {carta['tipo']}")
    print(f"  {'─' * 54}")

    dicas_vistas = set()

    for num_dica in range(1, 21):
        vencedor = _verificar_palpite_qualquer_hora(jogador, todos, carta, num_dica)
        if vencedor:
            return vencedor

        if jogador.eh_humano:
            print(f"Dicas já vistas: {sorted(dicas_vistas) if dicas_vistas else 'nenhuma'}")
            print("  Número da dica (1-20)  ou  0 para dar palpite:")
            escolha = _ler_inteiro("  > ", validos=list(range(0, 21)))

            if escolha == 0:
                palpite = _ler_texto(f"  {jogador.nome}, seu palpite: ")
                jogador.palpites += 1
                if palpite.lower() == carta["nome"].lower():
                    casas = max(1, 21 - num_dica)
                    jogador.posicao += casas
                    print(f"✅  ACERTOU! A resposta era: {carta['nome']}")
                    print(f"       +{casas} casas → posição {jogador.posicao}")
                    return jogador if jogador.posicao >= POSICAO_FINAL else None
                else:
                    print(f"  ❌  Errou! A resposta era: {carta['nome']}")
                    return None

            dica = carta["dicas"][escolha - 1]
            dicas_vistas.add(escolha)
            print(f"Dica {escolha}: {dica}")
            _aplicar_efeitos(dica, jogador, todos)
            if jogador.posicao >= POSICAO_FINAL:
                return jogador

        else:
            time.sleep(0.6)
            if jogador.quer_palpitar(num_dica):
                casas = max(1, 21 - num_dica)
                jogador.posicao += casas
                print(f"  🤖  {jogador.nome} arrisca na dica {num_dica} e acerta!")
                print(f"       +{casas} casas → posição {jogador.posicao}")
                return jogador if jogador.posicao >= POSICAO_FINAL else None
            else:
                dica = carta["dicas"][num_dica - 1]
                print(f"  🤖  {jogador.nome} pede a dica {num_dica}: {dica}")
                _aplicar_efeitos(dica, jogador, todos)
                if jogador.posicao >= POSICAO_FINAL:
                    return jogador

        if num_dica == 20:
            print(f"Dica 20! {jogador.nome} é obrigado a palpitar.")
            if jogador.eh_humano:
                palpite = _ler_texto("  Palpite final: ")
                jogador.palpites += 1
                if palpite.lower() == carta["nome"].lower():
                    jogador.posicao += 1
                    print(f"  ✅  Acertou! +1 casa → posição {jogador.posicao}")
                    return jogador if jogador.posicao >= POSICAO_FINAL else None
                else:
                    print(f"  ❌  Errou! Era: {carta['nome']}")
            else:
                jogador.posicao += 1
                print(f"  🤖  {jogador.nome} acerta na última! → posição {jogador.posicao}")
                return jogador if jogador.posicao >= POSICAO_FINAL else None

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
    ganhos = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2}

    print(f"{'═' * 54}")
    print(f"  ❓  CARTA ESPECIAL  —  {jogador.nome}")
    print(f"  Tipo: {carta['tipo']}")
    print("  Regras: até 5 dicas, apenas 1 palpite.")
    print("  Acerto: 1ª=10 | 2ª=8 | 3ª=6 | 4ª=4 | 5ª=2 casas")
    print(f"  {'═' * 54}")

    for tentativa in range(5):
        if jogador.eh_humano:
            if tentativa == 4:
                print(f"5ª tentativa: você é obrigado a palpitar.")
                idx = _ler_inteiro("  Escolha a última dica (1-20): ",
                                   validos=list(range(1, 21)))
                print(f"  Dica {idx}: {carta['dicas'][idx - 1]}")
                palpite = _ler_texto("  Palpite final: ")
                jogador.palpites += 1
                if palpite.lower() == carta["nome"].lower():
                    jogador.posicao += ganhos[4]
                    print(f"  ✅  Acertou! +{ganhos[4]} casas → posição {jogador.posicao}")
                    return jogador if jogador.posicao >= POSICAO_FINAL else None
                else:
                    print(f"  ❌  Errou! Era: {carta['nome']}. Não anda nada.")
                return None

            print(f"Tentativa {tentativa + 1}/5. Dica (1-20) ou 0 para palpitar:")
            escolha = _ler_inteiro("  > ", validos=list(range(0, 21)))
            if escolha == 0:
                palpite = _ler_texto("  Seu palpite: ")
                jogador.palpites += 1
                if palpite.lower() == carta["nome"].lower():
                    jogador.posicao += ganhos[tentativa]
                    print(f"  ✅  Acertou! +{ganhos[tentativa]} casas → posição {jogador.posicao}")
                    return jogador if jogador.posicao >= POSICAO_FINAL else None
                else:
                    print(f"  ❌  Errou! Era: {carta['nome']}. Não anda nada.")
                return None

            print(f"  Dica {escolha}: {carta['dicas'][escolha - 1]}")
            _aplicar_efeitos(carta["dicas"][escolha - 1], jogador, todos)

        else:
            time.sleep(0.5)
            chance = 0.10 + 0.18 * tentativa
            if tentativa == 4 or random.random() < chance:
                acertou = random.random() < chance or tentativa == 4
                print(f"  🤖  {jogador.nome} vai palpitar na tentativa {tentativa + 1}...")
                time.sleep(0.4)
                if acertou:
                    jogador.posicao += ganhos[tentativa]
                    print(f"  ✅  Acertou! +{ganhos[tentativa]} casas → posição {jogador.posicao}")
                    return jogador if jogador.posicao >= POSICAO_FINAL else None
                else:
                    print(f"  ❌  Errou! Era: {carta['nome']}")
                return None
            else:
                dica = carta["dicas"][tentativa]
                print(f"  🤖  {jogador.nome} pede dica {tentativa + 1}: {dica}")
                _aplicar_efeitos(dica, jogador, todos)

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

def _loop_jogo(jogadores: list) -> Jogador:
    """Alterna turnos até alguém chegar à posição 130."""
    especiais = criar_tabuleiro()
    turno = 0

    print(f"Jogo iniciado! Jogadores: {', '.join(j.nome for j in jogadores)}")
    print(f"  Objetivo: chegar primeiro à casa {POSICAO_FINAL}!")
    _pausar()

    while True:
        jogador_atual = jogadores[turno % len(jogadores)]
        _exibir_posicoes(jogadores)

        #exibir tabuleiro visual aqui

        if jogador_atual.posicao in especiais:
            vencedor = rodada_extra(jogador_atual, todos=jogadores)
        else:
            vencedor = rodada_normal(jogador_atual, todos=jogadores)

        if vencedor:
            _exibir_posicoes(jogadores)
            print(f" 🏆  {vencedor.nome} VENCEU O JOGO! Parabéns!")
            return vencedor

        if jogador_atual.posicao >= POSICAO_FINAL:
            _exibir_posicoes(jogadores)
            print(f" 🏆  {jogador_atual.nome} VENCEU O JOGO! Parabéns!")
            return jogador_atual

        _pausar()
        turno += 1

def iniciar_jogo() -> bool:
    """
    Exibe menu de modos e inicia o jogo.
    Retorna True se o vencedor for humano (compatível com o main.py original).

    # TODO – adicionar opção Tutorial aqui
    # TODO – integrar ranking após o jogo 
    """
    print("  ╔══════════════════════════════════════════╗")
    print("  ║            🎲  PERFIL  🎲               ║")
    print("  ╠══════════════════════════════════════════╣")
    print("  ║  1 - Solo (1 jogador)                    ║")
    print("  ║  2 - Multiplayer (2 a 6 jogadores)       ║")
    print("  ║  3 - VS Computador                       ║")
    print("  ╚══════════════════════════════════════════╝")

    op = _ler_inteiro("  Modo: ", validos=[1, 2, 3])

    if op == 1:
        nick = input("  Seu nick: ").strip() or "Jogador"
        jogadores = [Jogador(nick)]
    elif op == 2:
        jogadores = _configurar_multiplayer()
    else:
        jogadores = _configurar_vs_computador()

    vencedor = _loop_jogo(jogadores)

    #registrar vitória no ranking aqui

    return vencedor.eh_humano