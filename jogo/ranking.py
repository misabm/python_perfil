import json
import os


ARQUIVO_RANKING = "ranking.json"


PONTOS_POR_POSICAO = {

    1: 100,
    2: 60,
    3: 40,
    4: 25,
    5: 15,
    6: 10

}


class JogadorRanking:

    def __init__(self, nome):

        self.nome = nome

        self.pontos_totais = 0

        self.partidas_jogadas = 0

        self.vitorias = 0

    def adicionar_pontos(
        self,
        pontos
    ):

        self.pontos_totais += pontos

        self.partidas_jogadas += 1

    def taxa_vitoria(
        self
    ):

        if self.partidas_jogadas == 0:

            return 0

        return round(

            (

                self.vitorias

                /

                self.partidas_jogadas

            )

            *

            100,

            1

        )

    def para_dict(
        self
    ):

        return {

            "nome":
            self.nome,

            "pontos_totais":
            self.pontos_totais,

            "partidas_jogadas":
            self.partidas_jogadas,

            "vitorias":
            self.vitorias

        }

    @classmethod
    def do_dict(
        cls,
        dados
    ):

        jogador = cls(

            dados.get(
                "nome",
                "Desconhecido"
            )

        )

        jogador.pontos_totais = (

            dados.get(

                "pontos_totais",

                0

            )

        )

        jogador.partidas_jogadas = (

            dados.get(

                "partidas_jogadas",

                0

            )

        )

        jogador.vitorias = (

            dados.get(

                "vitorias",

                0

            )

        )

        return jogador


class Ranking:

    def __init__(self):

        self.jogadores = {}

        self.carregar()

    def carregar(
        self
    ):

        if not os.path.exists(
            ARQUIVO_RANKING
        ):

            return

        try:

            with open(

                ARQUIVO_RANKING,

                "r",

                encoding="utf8"

            ) as arquivo:

                dados = json.load(
                    arquivo
                )

        except (

            json.JSONDecodeError,

            OSError

        ):

            self.jogadores = {}

            return

        for item in dados:

            jogador = (

                JogadorRanking
                .do_dict(
                    item
                )

            )

            if (

                jogador.nome
                .lower()

                !=

                "computador"

            ):

                self.jogadores[
                    jogador.nome
                ] = jogador

    def salvar(
        self
    ):

        try:

            with open(

                ARQUIVO_RANKING,

                "w",

                encoding="utf8"

            ) as arquivo:

                json.dump(

                    [

                        j.para_dict()

                        for j

                        in self.jogadores.values()

                    ],

                    arquivo,

                    indent=4,

                    ensure_ascii=False

                )

        except OSError:

            print(
                "\nFalha ao salvar ranking."
            )

    def registrar_partida(
        self,
        resultado
    ):

        for posicao, (
            nome,
            vencedor
        ) in enumerate(

            resultado,

            start=1

        ):

            if (

                nome
                .lower()

                ==

                "computador"

            ):

                continue

            if (

                nome

                not in

                self.jogadores

            ):

                self.jogadores[
                    nome
                ] = (

                    JogadorRanking(
                        nome
                    )

                )

            jogador = (

                self.jogadores[
                    nome
                ]

            )

            pontos = (

                PONTOS_POR_POSICAO.get(

                    posicao,

                    5

                )

            )

            jogador.adicionar_pontos(
                pontos
            )

            if vencedor:

                jogador.vitorias += 1

        self.salvar()

    def mostrar_pontos_partida(
        self,
        resultado
    ):

        print()

        print(
            "PONTUAÇÃO"
        )

        print(
            "─" * 40
        )

        for posicao, (
            nome,
            _
        ) in enumerate(

            resultado,

            start=1

        ):

            if (

                nome
                .lower()

                ==

                "computador"

            ):

                continue

            pontos = (

                PONTOS_POR_POSICAO.get(

                    posicao,

                    5

                )

            )

            print(

                f"{posicao}º "

                +

                nome

                +

                f" (+{pontos})"

            )

        print()

    def mostrar_ranking(
        self
    ):

        jogadores = sorted(

            self.jogadores.values(),

            key=lambda j:

            (

                j.pontos_totais,

                j.vitorias

            ),

            reverse=True

        )

        if not jogadores:

            print(
                "\nSem ranking ainda."
            )

            return

        print()

        print(
            "═"
            * 82
        )

        print(
            "RANKING"
            .center(
                82
            )
        )

        print(
            "═"
            * 82
        )

        print(

            f'{"#":<4}'

            f'{"Nome":<20}'

            f'{"Pts":<10}'

            f'{"Partidas":<12}'

            f'{"Vitórias":<12}'

            f'{"Taxa":<10}'

        )

        print(
            "─"
            * 82
        )

        for i, j in enumerate(
            jogadores,
            start=1
        ):

            print(

                f"{i:<4}"

                f"{j.nome[:18]:<20}"

                f"{j.pontos_totais:<10}"

                f"{j.partidas_jogadas:<12}"

                f"{j.vitorias:<12}"

                f"{str(j.taxa_vitoria())+'%':<10}"

            )

        print()

        print(
            "═"
            * 82
        )


if __name__ == "__main__":

    r = Ranking()

    r.mostrar_ranking()