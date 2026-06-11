import random

# ─────────────────────────────────────────────────────────────────────────────
# cartas.py
# Banco de cartas do jogo Perfil.
# Para adicionar mais cartas: basta incluir novos dicionários na lista `cartas`
# seguindo o mesmo formato {"tipo": ..., "nome": ..., "dicas": [...]}.
# Responsável por adicionar cartas: Allyn
# ─────────────────────────────────────────────────────────────────────────────

cartas = [
    {
        "tipo": "LUGAR",
        "nome": "CENTRAL PARK",
        "dicas": [
            "Perca sua vez",
            "Sou um ponto turístico",
            "As pessoas costumam realizar piqueniques aqui",
            "Sou considerado o pulmão verde dos nova-iorquinos",
            "Sou o maior parque urbano do mundo",
            "Estou localizado no distrito de Manhattan, em Nova York",
            "Avance 3 casas",
            "Tenho uma flora diversificada",
            "Tenho um zoológico como uma das atrações",
            "Escolha 1 jogador para avançar 1 casa",
            "No inverno fico coberto de gelo",
            "Sou habitat de alguns mamíferos, como os esquilos",
            "Aqui há duas pistas de patinação no gelo",
            "Sou cenário de muitos filmes e programas de televisão",
            "Fui inaugurado em 1857",
            "Possuo uma área de 3,41 km²",
            "Um dos meus pontos famosos é conhecido por Strawberry Fields",
            "Tenho 23 estátuas",
            "Recebo aproximadamente 42 milhões de visitantes por ano",
            "Frederick Law Olmsted foi um dos responsáveis pela minha construção",
        ],
    },
    {
        "tipo": "PESSOA",
        "nome": "PRESIDENTE",
        "dicas": [
            "Indico autoridade máxima",
            "Escolha 1 jogador para avançar 3 casas",
            "Posso ser um cargo político ou um cargo de uma empresa",
            "Tenho o mesmo significado do termo CEO",
            "Escolha 1 jogador para voltar 1 casa",
            "No Facebook, Mark Zuckerberg ocupa o meu cargo",
            "Quem ocupou meu 44º cargo nos Estados Unidos foi Barack Obama",
            "Perca sua vez",
            "Tenho um papel importante de liderança",
            "Posso ser homem ou mulher",
            "Abaixo de mim sempre existe um vice",
            "Fernando Collor de Mello e José Sarney ocuparam meu cargo em 1990",
            "A maioria dos países me tem",
            "George Washington foi o meu primeiro nos Estados Unidos",
            "Tenho origem no latim e significo aquele que se senta à frente",
            "No Brasil sou Chefe de Estado e Comandante Supremo das Forças Armadas",
            "Sou eleito por um sistema majoritário",
            "Represento uma nação",
            "A primeira mulher a ocupar meu cargo à frente de um país foi Vigdís Finnbogadóttir",
            "Sebastian Kurz foi o meu mais jovem eleito do mundo",
        ],
    },
    {
        "tipo": "COISA",
        "nome": "STRANGER THINGS",
        "dicas": [
            "Sou uma série de TV streaming",
            "Avance 3 casas",
            "Estou disponível na plataforma Netflix",
            "Minha história tem início com o desaparecimento de Will Byers",
            "Tenho algo a ver com outra dimensão, chamada de mundo invertido",
            "Dustin é o nome de um dos meus personagens",
            "Aqui a atriz Millie Bobby Brown interpreta Eleven",
            "Escolha 1 jogador para avançar 1 casa",
            "Fui lançada em 2016",
            "Em 2022 eu estava com 4 temporadas",
            "Jim Hopper é o chefe de polícia daqui",
            "O monstro Demogorgon está por aqui",
            "A atriz Winona Ryder participa do meu elenco",
            "Sou ambientada na cidade fictícia de Hawkins",
            "Sou baseada nos anos 80",
            "Aqui acontece o Baile do Floco de Neve",
            "Fui criada pelos Duffer Brothers",
            "Ganhei o prêmio de série do ano na MTV Awards em 2017",
            "Um palpite a qualquer hora",
            "Minha trilha sonora foi criada por integrantes da banda Survive",
        ],
    },
    {
        "tipo": "DIGITAL",
        "nome": "BUG",
        "dicas": [
            "Sou uma palavra de origem inglesa",
            "Perca sua vez",
            "Acredita-se que meu termo foi criado por Thomas Edison",
            "Sou uma palavra usada em informática",
            "Sou uma falha ou erro",
            "Volte 2 casas",
            "Minha correção evita invasões de vírus de computador",
            "Vanellope, do filme Detona Ralph, é um exemplo",
            "Falaram muito sobre mim às vésperas do ano 2000",
            "Sou uma gíria para expressar confusão ou esquecimento momentâneo",
            "Posso causar travamento ou mau funcionamento",
            "Já aconteci no Facebook e no WhatsApp",
            "Geralmente sou reportado para equipes de desenvolvimento",
            "Posso ocorrer por diversos motivos",
            "Os aplicativos sempre tentam me eliminar",
            "Geralmente as empresas usam versões de teste para me evitar",
            "Sou encontrado em computadores",
            "Quando sou detectado, ocorrem atualizações",
            "Volte 2 casas",
            "Significo inseto",
        ],
    },
    {
        "tipo": "ANO",
        "nome": "1896",
        "dicas": [
            "Perca sua vez",
            "Estou numa década de 1800",
            "Ocorre a 1ª edição dos Jogos Olímpicos Modernos em Atenas",
            "Termino com 6",
            "Sou um ano bissexto",
            "Faço parte do século 19",
            "Estão sendo realizadas as Olimpíadas de Atenas",
            "O arraial de Canudos é uma ameaça à República",
            "Avance 2 casas",
            "Estamos na época da política do café com leite",
            "Tem início a Guerra de Canudos",
            "Daqui a um ano será fundada a Academia Brasileira de Letras",
            "Sou um ano da Era Moderna",
            "Escolha 1 jogador para avançar 1 casa",
            "Acontece a tragédia de Khodynka em Moscou",
            "MDCCCXCVI é a minha numeração romana",
            "Faz cinco anos que Deodoro da Fonseca foi obrigado a renunciar",
            "Nasce o pensador suíço Jean Piaget",
            "A Princesa Isabel está fazendo 50 anos",
            "Prudente de Moraes é o presidente do Brasil",
        ],
    },
    {
        "tipo": "COISA",
        "nome": "SANGUE",
        "dicas": [
            "Sou um dos componentes do corpo humano",
            "Quando doado, ajudo a salvar vidas",
            "Apareço quando as pessoas se cortam",
            "Em minha composição é possível encontrar plaquetas",
            "Em animais vertebrados apresento uma coloração avermelhada",
            "Transporto substâncias fundamentais pelo organismo",
            "Perca sua vez",
            "Sou um fluído corporal",
            "O coração é responsável por me bombear",
            "Escolha 1 jogador para voltar 1 casa",
            "Um dos meus tipos é conhecido como AB",
            "Circulo através de veias e artérias",
            "Sou viscoso",
            "Escolha 1 jogador para avançar 3 casas",
            "Sou produzido na medula óssea",
            "Tenho um volume de 5 litros, em média, numa pessoa adulta",
            "Faço parte do sistema circulatório",
            "Sou composto por plasma",
            "Sou alimento das sanguessugas",
            "Sou um dos ingredientes da linguiça conhecida como morcela",
        ],
    },
    {
        "tipo": "PESSOA",
        "nome": "THANOS",
        "dicas": [
            "Penso que estou fazendo o bem",
            "Sou grande e forte",
            "Sou um supervilão",
            "Sou da lua Titã",
            "Parti em busca das seis joias",
            "Tenho duas filhas adotivas",
            "Desintegrei metade dos seres do universo",
            "Usei a Manopla do Infinito",
            "Minha filha e eu fomos até Vormir",
            "O meu estalar de dedos pode ser mortal",
            "Eu lutei contra os Vingadores",
            "Eu destruí o Visão",
            "Decidi que iria destruir o universo",
            "Minha pele é roxa",
            "Avance 1 casa",
            "Eu sou inevitável",
            "Tony morreu para me destruir",
            "Avance 1 casa",
            "Volte 1 casa",
            "Falce de Ébano é fiel a mim",
        ],
    },
    {
        "tipo": "DIGITAL",
        "nome": "WHATSAPP",
        "dicas": [
            "Tenho grupos",
            "Muitas fake news foram disseminadas por aqui",
            "Posso gravar áudios",
            "Tenho criptografia",
            "Muitas empresas me utilizam como meio de comunicação",
            "Sou uma mídia social",
            "Escolha 1 jogador para voltar 1 casa",
            "Sou um aplicativo",
            "Tenho emojis",
            "Posso compartilhar vídeos",
            "Escolha 1 jogador para avançar 1 casa",
            "Facilito a comunicação",
            "Meu símbolo é um balão",
            "Sou multiplataforma",
            "Mando mensagens instantâneas",
            "Sou muito utilizado nos smartphones",
            "Fui comprado pelo Facebook",
            "Bilhões de pessoas me utilizam",
            "Perca sua vez",
            "Possuo código fechado",
        ],
    },
    {
        "tipo": "DIGITAL",
        "nome": "LIVE",
        "dicas": [
            "Posso ser vista por milhares de pessoas",
            "Escolha 1 jogador para avançar 1 casa",
            "Alok fez um show de luzes para eu surpreender seus fãs",
            "Sou um serviço streaming",
            "Durante uma das minhas, a cantora Ludmilla caiu na piscina",
            "Tive uma ajuda imensa do ZOOM",
            "Geralmente sou feita por meio das redes sociais",
            "Ganhei popularidade durante a pandemia da Covid-19",
            "Muitos artistas recorrem a mim",
            "Significo ao vivo na tradução do inglês",
            "Sou conhecida mundialmente",
            "Já causei críticas a Gusttavo Lima",
            "Avance 3 casas",
            "Enviam notificações aos seguidores quando vou ocorrer",
            "Uma das minhas mais vistas no mundo foi a da cantora Marília Mendonça",
            "A banda BTS me realizou com venda de ingressos",
            "Se apresento conteúdo inadequado, posso ser derrubada",
            "Posso ficar gravada ou não",
            "Sou uma alternativa para eventos presenciais",
            "Perca sua vez",
        ],
    },
    {
        "tipo": "COISA",
        "nome": "ESQUELETO",
        "dicas": [
            "Avance 2 casas",
            "Posso ser uma fantasia para o Halloween",
            "Dou sustentação ao corpo",
            "Uma das minhas doenças mais comuns é a osteoporose",
            "Sou um conjunto de ossos",
            "Uma de minhas funções é proteger os órgãos",
            "Armazeno a maior parte de cálcio do organismo",
            "Meu formato pode variar de acordo com a espécie",
            "No filme Viva - A vida é uma Festa, apareço como personagem",
            "Praticar atividades físicas me mantém forte",
            "Perca sua vez",
            "Os animais invertebrados não me têm",
            "O maior osso da minha estrutura é o fêmur",
            "Volte 3 casas",
            "Começo a ser formado entre 15 e 20 semanas da gravidez",
            "Sou uma das estruturas internas do corpo humano",
            "No adulto, tenho 206 ossos",
            "Sou dividido em axial e apendicular",
            "Represento 15% do peso corporal",
            "Meu desenvolvimento vai até os 22 anos",
        ],
    },
    {
        "tipo": "PESSOA",
        "nome": "MULAN",
        "dicas": [
            "Sou uma heroína chinesa",
            "Cortei meu cabelo comprido com uma espada",
            "Mushu é meu guardião, enviado pelos antepassados",
            "Avance 1 casa",
            "Também sou um desenho",
            "Finjo ser um homem para entrar no exército",
            "Sou corajosa e desastrada",
            "Sou considerada a oitava princesa da Disney",
            "Perca sua vez",
            "O nome de meu pai é Fa Zhou",
            "Um de meus companheiros no filme é o grilo Gri-Li",
            "A música Reflection de Christina Aguilera toca no meu filme",
            "A atriz Liu Yifei me interpreta na adaptação em live action",
            "Sou dublada originalmente pela atriz Ming-Na",
            "Sou inspirada em uma lenda chinesa",
            "Fiz uma aparição na série Princesinha Sofia",
            "Meu nome significa flor de magnólia em chinês",
            "Fui destaque na edição 100 da revista Disney Adventures",
            "Fui ferida por Shan Yu",
            "Escolha 1 jogador para avançar 2 casas",
        ],
    },
    {
        "tipo": "ANO",
        "nome": "2017",
        "dicas": [
            "É lançada a música Despacito",
            "Neymar é contratado pelo PSG",
            "Sou um ano do século 21",
            "Escolha 1 jogador para avançar 3 casas",
            "Sou um ano antes da Copa do Mundo da Rússia",
            "Donald Trump assume a presidência dos EUA",
            "Um palpite a qualquer hora",
            "É lançado o filme It - A Coisa no Brasil",
            "Acontece o Tiroteio de Las Vegas Strip",
            "Forte terremoto atinge o México, deixando mais de 300 mortos",
            "Morre o jornalista Marcelo Rezende",
            "Desprende-se de Larsen C, na Antártida, um dos maiores icebergs",
            "Avance 3 casas",
            "A soma dos meus números dá 10",
            "No ano passado ocorreu o impeachment da presidente Dilma",
            "O primeiro-ministro libanês Saad Hariri é demitido",
            "Robert Mugabe renuncia à presidência do Zimbábue",
            "Está havendo uma rebelião no Complexo Penitenciário de Manaus",
            "Harvey Weinstein é acusado de assédio sexual por Angelina Jolie",
            "Há 100 anos acontecia na Rússia a revolução que depôs o Czar Nicolau II",
        ],
    },
    {
        "tipo": "ANO",
        "nome": "1521",
        "dicas": [
            "Faço parte do século 16",
            "Escolha 1 jogador para voltar 3 casas",
            "Papa Leão X excomuna Martinho Lutero",
            "Celebra-se a primeira missa nas Filipinas",
            "Pamplona rende-se aos castelhanos",
            "Pedro Álvares Cabral morreu há um ano",
            "Há 100 anos Pequim tornou-se capital do Império Chinês",
            "Morre Fernando de Magalhães",
            "Fernão Magalhães chega às Filipinas",
            "Cabral chegou ao Brasil há 21 anos",
            "A soma dos meus números dá 9",
            "Liderados por Solimão, o Magnífico, os otomanos invadem Belgrado",
            "O último imperador Azteca rende-se ao conquistador Fernando Cortés",
            "Perca sua vez",
            "Sou um ano do calendário juliano",
            "Carlos, o rei da Espanha, expulsa os franceses de Milão",
            "Escolha 1 jogador para avançar 1 casa",
            "Começo e termino com o número 1",
            "Daqui a 500 anos, a Anvisa aprovará as vacinas Coronavac e AstraZeneca",
            "Minha numeração em algarismos romanos é MDXXI",
        ],
    },
    {
        "tipo": "LUGAR",
        "nome": "COACHELLA",
        "dicas": [
            "Aqui, um evento que se faz uma vez por ano já durou três dias",
            "Sou uma cidade",
            "Escolha 1 jogador para avançar 2 casas",
            "Desde 1999 sou sede de um festival de música que leva meu nome",
            "Perca sua vez",
            "Fico na Califórnia",
            "Estou num vale",
            "Aqui há várias tendas",
            "No meu festival há diversos palcos",
            "Meu principal evento é organizado pela Goldenvoice",
            "Durante o dia aqui pode fazer mais de 40 graus",
            "Um dos gêneros apreciados aqui é o Hip Hop",
            "Vários artistas brasileiros estiveram aqui em 2022",
            "Em 2010 mais de 75 mil pessoas vieram para cá",
            "A cantora brasileira Céu já se apresentou aqui",
            "Em 2018 Beyoncé elevou ainda mais meu festival",
            "Escolha 1 jogador para voltar 1 casa",
            "As pessoas capricham nos looks quando vêm aqui",
            "Estou em um deserto",
            "Lady Gaga já se apresentou aqui",
        ],
    },
    {
        "tipo": "PESSOA",
        "nome": "MAGNETO",
        "dicas": [
            "Sou um personagem dos X-Men",
            "Escolha 1 jogador para avançar 1 casa",
            "Escolha 1 jogador para avançar 3 casas",
            "Sou um mutante",
            "Uso um capacete",
            "Fui criado e publicado pela editora Marvel Comics",
            "Sou o Mestre do Magnetismo",
            "Sou interpretado pelo ator Michael Fassbender",
            "Sou conhecido também como Erik Lehnsherr",
            "Posso voar",
            "Tirei o adamantium de Wolverine",
            "Sou um personagem do jogo Lego Marvel Super Heroes",
            "Escolha 1 jogador para avançar 2 casas",
            "Fui amigo do Professor X",
            "Paul McCartney se inspirou em mim para compor uma música",
            "Sou de origem judaica",
            "Minha primeira aparição foi em Quarteto Fantástico, de 1978",
            "Fiquei preso no Pentágono",
            "Sou alemão",
            "Fui apaixonado por Magda",
        ],
    },
    {
        "tipo": "DIGITAL",
        "nome": "LINKEDIN",
        "dicas": [
            "Perca sua vez",
            "Sou uma rede social",
            "Fui lançado antes do Facebook",
            "Volte 3 casas",
            "Sou utilizado na maior parte do mundo",
            "Avance 1 casa",
            "Por aqui é comum encontrar a hashtag OpenToWork",
            "Posso estabelecer conexões com outras pessoas",
            "Ofereço cursos gratuitos",
            "Estou praticamente no mundo todo, com mais de meio bilhão de usuários",
            "Incentivo o networking profissional",
            "As pessoas me utilizam para conseguir emprego",
            "Ofereço uma versão premium",
            "Sou utilizado por profissionais de diversas áreas",
            "Fui fundado em dezembro de 2002",
            "Os EUA é um dos países que mais me utiliza",
            "Em 2016 fui comprado pela Microsoft",
            "Reid Hoffman é um dos meus fundadores",
            "Posso servir como um currículo digital",
            "Minha sede fica em Mountain View, na Califórnia",
        ],
    },
    {
"tipo":"DIGITAL",
"nome":"DISCORD",
"dicas":[
"Sou uma plataforma digital",
"Tenho servidores",
"Sou muito usado por jogadores",
"Permito chamadas de voz",
"Tenho canais",
"Volte 1 casa",
"Posso compartilhar tela",
"Tenho bots",
"Sou gratuito",
"Escolha 1 jogador para avançar 1 casa",
"Tenho versão mobile",
"Fiquei popular durante a pandemia",
"Possuo cargos",
"Posso transmitir jogos",
"Fui criado em 2015",
"Minha logo é azul",
"Tenho chats privados",
"Avance 2 casas",
"Meu fundador é Jason Citron",
"Sou concorrente do TeamSpeak"
]
},

{
"tipo":"COISA",
"nome":"CAFÉ",
"dicas":[
"Sou consumido no mundo todo",
"Posso ser quente",
"Tenho cafeína",
"Sou comum pela manhã",
"Perca sua vez",
"Posso ser expresso",
"Sou produzido no Brasil",
"Tenho aroma marcante",
"Posso vir com leite",
"Escolha 1 jogador para voltar 1 casa",
"Tenho versão descafeinada",
"Sou uma bebida",
"Meu grão é torrado",
"Tenho sabor amargo",
"Avance 1 casa",
"Posso causar insônia",
"Sou servido em cafeterias",
"Faço parte do cotidiano",
"Tenho cor escura",
"Meu cultivo ocorre em fazendas"
]
},

{
"tipo":"PESSOA",
"nome":"BATMAN",
"dicas":[
"Sou um personagem",
"Tenho capa",
"Protejo uma cidade",
"Não tenho poderes",
"Sou bilionário",
"Escolha 1 jogador para avançar 2 casas",
"Tenho um mordomo",
"Meu símbolo é um morcego",
"Já fui interpretado por vários atores",
"Uso tecnologia",
"Minha cidade é Gotham",
"Meu nome verdadeiro é Bruce Wayne",
"Combato o Coringa",
"Tenho um carro famoso",
"Avance 2 casas",
"Faço parte da DC",
"Sou conhecido como cavaleiro das trevas",
"Perca sua vez",
"Tenho um parceiro chamado Robin",
"Sou o Batman"
]
},

{
"tipo":"COISA",
"nome":"PIANO",
"dicas":[
"Sou um instrumento",
"Tenho teclas",
"Posso ser grande",
"Sou usado em apresentações",
"Escolha 1 jogador para avançar 1 casa",
"Produzo notas musicais",
"Tenho cordas",
"Fui criado há séculos",
"Posso ser digital",
"Tenho pedais",
"Avance 1 casa",
"Sou usado em música clássica",
"Tenho versão de cauda",
"Posso acompanhar cantores",
"Tenho teclas brancas e pretas",
"Perca sua vez",
"Sou muito usado em estudos musicais",
"Posso ser afinado",
"Meu som é harmônico",
"Sou tocado com as mãos"
]
},

{
"tipo":"ANO",
"nome":"2007",
"dicas":[
"Ocorri no século XXI",
"Foi lançado o primeiro iPhone",
"Escolha 1 jogador para voltar 1 casa",
"O Brasil sediaria Copa anos depois",
"Tenho soma igual 9",
"Sou posterior a 2006",
"Avance 2 casas",
"Steve Jobs fez apresentação histórica",
"Sou anterior a 2008",
"Sou um ano comum",
"Tenho quatro dígitos",
"Perca sua vez",
"Marco início dos smartphones modernos",
"Tenho dois zeros",
"Meu último dígito é 7",
"Tenho um número repetido",
"Fiquei conhecido pela tecnologia",
"Sou recente",
"Tenho um 2",
"Sou 2007"
]
},

{
"tipo":"LUGAR",
"nome":"TORRE EIFFEL",
"dicas":[
"Sou turístico",
"Estou na Europa",
"Recebo milhões de visitantes",
"Fico em uma capital",
"Tenho estrutura metálica",
"Escolha 1 jogador para avançar 2 casas",
"Sou francesa",
"Tenho elevadores",
"Avance 3 casas",
"Fui inaugurada no século XIX",
"Tenho mais de 300 metros",
"Meu nome é de um engenheiro",
"Estou em Paris",
"Tenho iluminação noturna",
"Perca sua vez",
"Sou um símbolo nacional",
"Fui construída para exposição",
"Sou famosa mundialmente",
"Apareço em filmes",
"Sou a Torre Eiffel"
]
},
{
"tipo":"PESSOA",
"nome":"HOMEM-ARANHA",
"dicas":[
"Sou um personagem",
"Escolha 1 jogador para avançar 1 casa",
"Tenho sentidos apurados",
"Uso máscara",
"Vivo em Nova York",
"Tenho poderes",
"Fui mordido",
"Volte 1 casa",
"Combato vilões",
"Meu uniforme geralmente é vermelho",
"Já participei dos Vingadores",
"Tenho um lançador de teias",
"Sou jovem",
"Perca sua vez",
"Meu criador foi Stan Lee",
"Tenho amizade com Ned",
"Minha tia se chama May",
"Meu alter ego é estudante",
"Meu nome verdadeiro é Peter Parker",
"Sou o Homem-Aranha"
]
},

{
"tipo":"PESSOA",
"nome":"SHERLOCK HOLMES",
"dicas":[
"Sou um personagem",
"Resolvo mistérios",
"Uso lógica",
"Tenho um companheiro",
"Avance 2 casas",
"Moro em Londres",
"Sou detetive",
"Meu criador foi Arthur Conan Doyle",
"Uso observação",
"Tenho fama mundial",
"Perca sua vez",
"Já fui adaptado para filmes",
"Uso dedução",
"Tenho um inimigo famoso",
"Meu amigo é Watson",
"Fumo cachimbo",
"Sou britânico",
"Costumo investigar crimes",
"Escolha 1 jogador para voltar 1 casa",
"Sou Sherlock Holmes"
]
},

{
"tipo":"DIGITAL",
"nome":"YOUTUBE",
"dicas":[
"Sou digital",
"Tenho vídeos",
"Permito comentários",
"Escolha 1 jogador para avançar 1 casa",
"Tenho criadores de conteúdo",
"Sou muito acessado",
"Permito transmissões",
"Tenho anúncios",
"Posso monetizar",
"Avance 2 casas",
"Tenho inscritos",
"Fui criado em 2005",
"Tenho botão vermelho",
"Tenho vídeos curtos",
"Perca sua vez",
"Sou do Google",
"Tenho bilhões de usuários",
"Posso ensinar coisas",
"Meu símbolo é um play",
"Sou o YouTube"
]
},

{
"tipo":"DIGITAL",
"nome":"SPOTIFY",
"dicas":[
"Sou um serviço digital",
"Tenho playlists",
"Reproduzo áudio",
"Escolha 1 jogador para avançar 2 casas",
"Tenho versão gratuita",
"Tenho versão premium",
"Sou usado em celulares",
"Posso tocar músicas",
"Tenho podcasts",
"Avance 1 casa",
"Minha logo é verde",
"Fui criado na Suécia",
"Tenho recomendações",
"Perca sua vez",
"Posso baixar conteúdo",
"Sou muito popular",
"Uso streaming",
"Tenho milhões de músicas",
"Posso tocar offline",
"Sou o Spotify"
]
},

{
"tipo":"DIGITAL",
"nome":"CHATGPT",
"dicas":[
"Sou digital",
"Respondo perguntas",
"Uso inteligência artificial",
"Tenho conversas",
"Escolha 1 jogador para voltar 1 casa",
"Posso ajudar estudos",
"Posso escrever textos",
"Avance 1 casa",
"Posso gerar ideias",
"Tenho versões diferentes",
"Perca sua vez",
"Posso programar",
"Sou usado no navegador",
"Fui lançado em 2022",
"Sou treinado com dados",
"Posso resumir conteúdos",
"Sou um assistente virtual",
"Fui criado pela OpenAI",
"Uso IA generativa",
"Sou o ChatGPT"
]
},

{
"tipo":"COISA",
"nome":"CHOCOLATE",
"dicas":[
"Sou consumido no mundo inteiro",
"Posso ser doce",
"Tenho versões diferentes",
"Escolha 1 jogador para avançar 1 casa",
"Posso derreter",
"Sou feito com cacau",
"Posso ser amargo",
"Sou comum em sobremesas",
"Avance 1 casa",
"Tenho barras",
"Perca sua vez",
"Posso ser branco",
"Tenho origem antiga",
"Sou vendido em lojas",
"Posso virar bebida",
"Tenho açúcar",
"Sou popular na Páscoa",
"Posso ser recheado",
"Sou um alimento",
"Sou chocolate"
]
},

{
"tipo":"COISA",
"nome":"FOGUETE",
"dicas":[
"Posso voar",
"Uso combustível",
"Sou veloz",
"Escolha 1 jogador para avançar 2 casas",
"Posso chegar ao espaço",
"Avance 3 casas",
"Tenho motores",
"Levo cargas",
"Posso ser reutilizado",
"Tenho lançamento vertical",
"Perca sua vez",
"Tenho estágio",
"Uso engenharia avançada",
"Posso levar satélites",
"Sou usado por agências espaciais",
"Posso levar astronautas",
"Tenho grande potência",
"Sou usado em missões",
"Meu destino pode ser órbita",
"Sou um foguete"
]
},

{
"tipo":"LUGAR",
"nome":"COLISEU",
"dicas":[
"Sou um lugar histórico",
"Fico na Europa",
"Recebo turistas",
"Escolha 1 jogador para voltar 1 casa",
"Tenho formato oval",
"Sou muito antigo",
"Fico na Itália",
"Avance 2 casas",
"Recebi eventos",
"Tenho ruínas",
"Fui palco de batalhas",
"Perca sua vez",
"Sou romano",
"Tenho arquibancadas",
"Sou famoso mundialmente",
"Tenho milhares de visitantes",
"Fui construído há séculos",
"Estou em Roma",
"Sou patrimônio histórico",
"Sou o Coliseu"
]
},

{
"tipo":"LUGAR",
"nome":"MACHU PICCHU",
"dicas":[
"Sou turístico",
"Fico na América do Sul",
"Estou em altitude elevada",
"Escolha 1 jogador para avançar 1 casa",
"Tenho ruínas",
"Sou patrimônio histórico",
"Avance 2 casas",
"Tenho ligação com povos antigos",
"Perca sua vez",
"Recebo turistas",
"Fui redescoberto",
"Estou no Peru",
"Tenho montanhas",
"Sou um sítio arqueológico",
"Sou muito fotografado",
"Tenho pedra",
"Tenho vista famosa",
"Fui construído pelos incas",
"Sou uma cidade antiga",
"Sou Machu Picchu"
]
},

{
"tipo":"ANO",
"nome":"1969",
"dicas":[
"Sou um ano",
"Sou do século XX",
"Escolha 1 jogador para avançar 1 casa",
"Avance 2 casas",
"Tenho quatro dígitos",
"Aconteceu algo histórico",
"Fui antes de 1970",
"Perca sua vez",
"Meu último número é 9",
"Marquei a exploração espacial",
"Neil Armstrong ficou famoso",
"Tenho soma 25",
"Sou conhecido mundialmente",
"Fui um ano importante",
"Milhões acompanharam um evento",
"Foi transmitido pela TV",
"O homem pisou na Lua",
"Apollo 11 aconteceu",
"Foi corrida espacial",
"Sou 1969"
]
},

{
"tipo":"ANO",
"nome":"2020",
"dicas":[
"Sou recente",
"Sou do século XXI",
"Perca sua vez",
"Escolha 1 jogador para voltar 1 casa",
"Fiquei conhecido mundialmente",
"Muitas pessoas ficaram em casa",
"Avance 1 casa",
"Tive trabalho remoto",
"Tive ensino remoto",
"Tenho dois números repetidos",
"Comecei uma década",
"Usei máscaras",
"Tive videoconferências",
"Tive mudanças globais",
"Fiquei marcado",
"Minha soma é 4",
"Tenho dois zeros",
"Sou posterior a 2019",
"Fui antes de 2021",
"Sou 2020"
]
},
]

def validar_cartas():

    nomes = set()

    for indice, carta in enumerate(cartas):

        if carta["nome"] in nomes:

            raise ValueError(
                f"Carta duplicada: {carta['nome']}"
            )

        nomes.add(
            carta["nome"]
        )

        if len(carta["dicas"]) != 20:

            raise ValueError(
                f"Carta {indice+1} inválida"
            )

        if len(
            [
                d
                for d
                in carta["dicas"]
                if d.strip()
            ]
        ) != 20:

            raise ValueError(
                f"Dicas vazias em {carta['nome']}"
            )


_cartas_usadas = []


def pegar_carta():

    global _cartas_usadas

    if len(
        _cartas_usadas
    ) >= len(
        cartas
    ):

        _cartas_usadas.clear()

    disponiveis = [

        carta

        for carta

        in cartas

        if carta
        not in
        _cartas_usadas

    ]

    sorteada = random.choice(
        disponiveis
    )

    _cartas_usadas.append(
        sorteada
    )

    return sorteada

    TIPOS_VALIDOS = {

    "PESSOA",

    "LUGAR",

    "COISA",

    "DIGITAL",

    "ANO"

}


