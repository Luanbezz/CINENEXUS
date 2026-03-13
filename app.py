from flask import Flask, render_template, request

app = Flask(__name__)

# --- BANCO DE ATORES (Fotos Reais TMDB) ---
BANCO_DE_ATORES = {
    101: {
        "nome": "Cillian Murphy",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/llkbyWKwpfowZ6C8peBjIV9jj99.jpg",
        "bio": "Cillian Murphy (Douglas, 25 de maio de 1976) é um ator e músico irlandês de teatro, cinema e televisão. Murphy é conhecido por suas colaborações com o diretor Christopher Nolan, interpretando o Espantalho na trilogia de The Dark Knight (2005-2012) e aparecendo no thriller de ação e ficção científica Inception (2010) e no drama de guerra Dunkirk (2017). Em 2023, interpretou J. Robert Oppenheimer no filme Oppenheimer, que lhe rendeu o BAFTA, Globo de Ouro, Screen Actors Guild e Oscar de Melhor Ator.",
        "filmes_ids": [1, 4, 7]
    },
    102: {
        "nome": "Robert Downey Jr.",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/5qHNjhtjMD4YWH3UP0rm4tKwxCL.jpg",
        "bio": "Robert John Downey, Jr. (Nova Iorque, 4 de abril de 1965) é um ator americano. Downey fez sua estréia na tela em 1970, aos cinco anos de idade, quando apareceu no filme de seu pai, Pound, e trabalhou consistentemente no cinema e na televisão desde então. Durante a década de 1980, ele teve papéis em uma série de filmes de amadurecimento associados ao Brat Pack. Less Than Zero (1987) é particularmente notável. Ele interpretou Charlie Chaplin no filme de 1992 Chaplin, pelo qual recebeu uma indicação ao Oscar de Melhor Ator. Foi o ator mais bem pago do mundo durante três anos seguidos (2013, 2014, 2015).",
        "filmes_ids": [1]
    },
    103: {
        "nome": "Matthew McConaughey",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/lCySuYjhXix3FzQdS4oceDDrXKI.jpg",
        "bio": "Matthew David McConaughey (Uvalde, 4 de novembro de 1969) é um ator, produtor, realizador, cenógrafo e professor estadunidense vencedor do Oscar de Melhor Ator. Além de fazer uma ponta em The Wolf of Wall Street (2013), participou como protagonista tanto na série de sucesso da HBO, True Detective, recebendo ótimas críticas, como no premiado filme Dallas Buyers Club (2013). Por seu desempenho, Matthew foi aclamado pela crítica especializada, levando, entre tantos outros prêmios, o Oscar de Melhor Ator, Globo de Ouro de Melhor Ator em filme dramático e SAG Award de Melhor Ator.",
        "filmes_ids": [2, 12]
    },
    104: {
        "nome": "Leonardo DiCaprio",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/vo4fltT9zZ1kH8nhLetz8MED6jp.jpg",
        "bio": "Leonardo Wilhelm DiCaprio (Los Angeles, 11 de novembro de 1974) é um ator, produtor e filantropo norte-americano ganhador do Oscar de melhor ator por The Revenant. Começou sua carreira aparecendo em comerciais de televisão. É conhecido pela sua participação em filmes como Inception, Titanic, Blood Diamond, The Aviator, Catch Me If You Can, Gangs of New York, The Departed, Django Unchained, The Wolf of Wall Street, The Great Gatsby e The Revenant, entre outros. Além da representação, DiCaprio tem a sua própria companhia de produção, a Appian Way Productions e é um reconhecido ativista da defesa do meio ambiente.",
        "filmes_ids": [4, 10, 12]
    },
    105: {
        "nome": "Keanu Reeves",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/8RZLOyYGsoRe9p44q3xin9QkMHv.jpg",
        "bio": "Keanu Charles Reeves (Beirute, 2 de setembro de 1964) é um ator, cineasta, escritor, produtor cinematográfico e músico canadense, nascido no Líbano. Em 2006, 12 anos depois de atuarem juntos em Speed, Keanu volta às telonas com a atriz Sandra Bullock em 'A Casa do Lago', dirigido por Alejandro Agresti. Foi um grande sucesso, principalmente no Japão.Keanu voltará a interpretar Neo em Matrix 4 com filmagens previstas para 2020. Em 2003, passou a morar em Hollywood, Califórnia. No dia 31 de janeiro de 2005, Keanu recebeu uma estrela na Calçada da Fama de Los Angeles.",
        "filmes_ids": [5]
    },
    106: {
        "nome": "Joaquin Phoenix",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/u38k3hQBDwNX0VA22aQceDp9Iyv.jpg",
        "bio": "Joaquin Rafael Phoenix, nascido Joaquin Rafael Bottom (San Juan, Porto Rico, 28 de outubro de 1974) é um ator, produtor e ativista Portoriquenho. Por seu trabalho como ator, Phoenix recebeu um Grammy, dois Globo de Ouro e quatro indicações ao Óscar, vencendo como melhor ator na cerimônia de 2020 por sua atuação em Joker (2019). Ele recebeu atenção internacional por sua interpretação de Commodus no épico histórico Gladiador (2000), que lhe rendeu uma indicação ao Óscar de Melhor Ator Coadjuvante. Posteriormente, recebeu indicações para Melhor Ator por interpretar o músico Johnny Cash na cinebiografia Walk the Line (2005).",
        "filmes_ids": [6]
    },
     107: {
        "nome": "Naomie Harris",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/41TVAcYqKKF7PGf3x7QfaLvkLSW.jpg",
        "bio": "Naomie Melanie Harris (born 6 September 1976) is an English screen actress of Jamaican and Trinidadian heritage. She is known for her roles as Justin Falls on The Man Who Fell to Earth, Frances Louise Barrison / Shriek in Venom: Let There Be Carnage, Eve Moneypenny in the James Bond (Daniel Craig) franchise, Tia Dalma in the second and third Pirates of the Caribbean films, Nisha in Mowgli: Legend of the Jungle, Dr. Kate Caldwell in Rampage, Madeleine in Collateral Beauty, Paula in Moonlight - for which she received a nomination for the Academy Award for Best Supporting Actress, Winnie Madikizela in Mandela: Long Walk to Freedom, Alison Wade on the drama series Accused (2010), Det. Trudy Joplin in Miami Vice (2006), Sophie in After the Sunset, Selena in 28 Days, Ami on the series The Tomorrow People (1992), and Shuku on the series Runaway Bay (1992).",
        "filmes_ids": [7]
    },
    108: {
        "nome": "Brendan Gleeson",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/ctPPJu5ZYDZr1IPmzoNpezczrm0.jpg",
        "bio": "Brendan Gleeson (nascido em 29 de março de 1955) é um ator e diretor de cinema irlandês. Ele recebeu três prêmios IFTA, dois BIFA e um prêmio Primetime Emmy e foi indicado duas vezes ao prêmio BAFTA, cinco vezes ao Globo de Ouro e uma vez ao Oscar. Em 2020, ele foi listado em 18º lugar na lista do The Irish Times dos maiores atores de cinema da Irlanda. Ele é o pai dos atores Domhnall Gleeson e Brian Gleeson.",
        "filmes_ids": [7]},
    109: {
        "nome": "Christopher Eccleston",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/v6ezjezzDo6xP2wlONO5ZzBciwl.jpg",
        "bio": "Christopher Eccleston (born 16 February 1964) is an English stage, film and television actor. His films include Let Him Have It, Shallow Grave, Elizabeth, 28 Days Later, Gone in 60 Seconds, The Others, and G.I. Joe: The Rise of Cobra. In 2005, he became the ninth incarnation of The Doctor in the British television series Doctor Who.",
        "filmes_ids": [7]},
    110: {
        "nome": "Emily Blunt",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/5nCSG5TL1bP1geD8aaBfaLnLLCD.jpg",
        "bio": "Emily Blunt começou sua carreira no teatro mas logo foi para a televisão, quando interpretou Isolda no filme A Rainha da Era do Bronze (2003) e também a Rainha Catalina Howard, na minissérie Henry VIII (2003). Sua estréia no cinema aconteceu só em 2005 no drama Meu Amor de Verão, mas seu reconhecimento veio mesmo no ano seguinte, quando teve papéis de destaque em A Filha de Gideon (que lhe rendeu um Globo de Ouro) e O Diabo Veste Prada (por esse, recebeu uma indicação ao BAFTA).",
        "filmes_ids": [1]},
     111: {
        "nome": "Matt Damon",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/nbccV2pMoyLTCeg5DQip24Eq0Jp.jpg",
        "bio": "Matthew 'Matt' Paige Damon (Cambridge, 8 de outubro de 1970) é um ator, roteirista, produtor e filantropo norte-americano, cuja carreira foi lançada após o sucesso do filme de drama Good Will Hunting (1997) a partir do roteiro que ele co-escreveu com o amigo e ator Ben Affleck. A dupla ganhou o Oscar de melhor roteiro original e o Globo de Ouro de melhor roteiro por seu trabalho. Por sua atuação no filme, Damon recebeu indicações para o Oscar, Globo de Ouro, Satellite Award, e o Screen Actors Guild Awards de Melhor Ator. No filme 'Onze Homens e Um Segredo', Damon atuou ao lado de grandes estrelas de Hollywood como George Clooney, Andy Garcia e Brad Pitt.",
        "filmes_ids": [1]},
    112: {
        "nome": "Anne Hathaway",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/nbccV2pMoyLTCeg5DQip24Eq0Jp.jpg",
        "bio": "Anne Jacqueline Hathaway (Nova Iorque, 12 de novembro de 1982) é uma atriz norte-americana. Recebedora de vários elogios, incluindo um Oscar, um Globo de Ouro e um Prêmio Primetime Emmy, ela estava entre as atrizes mais bem pagas do mundo em 2015. Seus filmes arrecadaram mais de US$6,8 bilhões em todo o mundo, e ela apareceu na lista Forbes Celebrity 100 em 2009. A comédia-drama O Diabo Veste Prada (2006), no qual ela interpretou uma assistente de uma editora de revista de moda, foi seu maior sucesso comercial até aquele momento.",
        "filmes_ids": [2]},
    113: {
        "nome": "Michael Caine",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/bVZRMlpjTAO2pJK6v90buFgVbSW.jpg",
        "bio": "Michael Caine, nascido Maurice Joseph Micklewhite (Londres, 14 de março de 1933), é um ator e produtor de cinema britânico, duas vezes vencedor do Oscar da Academia para Melhor Ator Coadjuvante (por suas atuações em Hannah and Her Sisters e The Cider House Rules) e famoso por interpretar Alfred Pennyworth, o mordomo de Bruce Wayne/Batman na trilogia de filmes de Cristopher Nolan (batman). Caine foi nominado para cinco Óscars, sendo que ele e Jack Nicholson são os únicos atores a terem sido nominados a um Óscar de atuação em cada uma das últimas cinco décadas (situação em 2007). Além deste, outro feito de Caine é estar presente em mais de cem filmes ao longo de sua carreira.",
        "filmes_ids": [2]},
    114: {
        "nome": "Jessica Chastain",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/lodMzLKSdrPcBry6TdoDsMN3Vge.jpg",
        "bio": "Jessica Michelle Chastain (Sacramento, 24 de março de 1977) é uma atriz, profissional de dublagem e produtora norte-americana. Chastain nasceu e cresceu no norte da Califórnia, desenvolvendo desde cedo um interesse pela atuação. Ela estreou profissionalmente no teatro em 1998 como Julieta em uma produção de Romeu e Julieta. Estudou atuação na Escola Juilliard e depois disso assinou um contrato com o produtor televisivo John Wells. Chastain fez aparições coadjuvantes em diversas séries de televisão, incluindo ER e Law & Order.",
        "filmes_ids": [2]},
    115: {
        "nome": "Finn Wolfhard",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/dQ1Fj2gCwko0Jnt3QEj1GLseXSh.jpg",
        "bio": "Finn Wolfhard (nascido em 23 de dezembro de 2002) é um ator, músico, roteirista e diretor canadense. Seus papéis de ator incluem Mike Wheeler na série Stranger Things da Netflix (2016-2025), pela qual ganhou o Screen Actors Guild Award por Melhor Desempenho por um Conjunto em Série Dramática em três nomeações. Seus papéis no cinema incluem Richie Tozier na adaptação cinematográfica do romance de terror de Stephen King, It (2017) e sua sequência It: Chapter Two (2019), Boris Pavlivosky no filme dramático The Goldfinch (2019), a voz de Pugsley Addams em The Addams Família (2019) e Trevor no filme sobrenatural Ghostbusters: Afterlife (2021). Wolfhard fará sua estreia na direção com o curta-metragem de comédia Night Shifts (2020). Como músico, ele foi o vocalista e guitarrista da banda de rock Calpurnia, e atualmente é membro do The Aubreys.",
        "filmes_ids": [8, 9]},    
    116: {
        "nome": "Jaeden Martell",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/oR7ZJsOHMNFzM1HeugV4a4qCMSF.jpg",
        "bio": "Jaeden Martell (né Lieberher; born January 4, 2003) is an American actor. He began his career as a child actor, with roles in the comedy drama St. Vincent (2014) and science fiction film Midnight Special (2016). His performance in St. Vincent earned him a nomination for the Critics' Choice Movie Award for Best Young Performer. After playing the title character in the drama The Book of Henry (2017), Martell's breakthrough came with his portrayal of Bill Denbrough in the supernatural horror films It (2017) and It Chapter Two (2019). This led to further leading roles in horror films, such as The Lodge (2019) and Mr. Harrigan's Phone (2022).",
        "filmes_ids": [8, 9]},    
    117: {
        "nome": "Jeremy Ray Taylor",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/czfmzjsDrGqIvDA3kkq62h9RCA1.jpg",
        "bio": "Jeremy Raymond Taylor (born June 2, 2003) is an American actor. He is known for his role as Ben Hanscom in the 2017 adaptation of Stephen King's novel It and its 2019 sequel, as well as the role of Sonny Quinn in Goosebumps 2: Haunted Halloween (2018).Taylor was raised in Bluff City, Tennessee, the youngest of four boys of Tracy, a band manager, and Michael Taylor. He traveled with his mother and developed a stage persona that intrigued his family. At the age of 8, he was signed to a talent manager and began his acting career.",
        "filmes_ids": [8, 9]},    
    118: {
        "nome": "Sophia Lillis",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/5aAw3KFixZSsMfo0BWrxtBLVsXN.jpg",
        "bio": "Sophia Lillis (born February 13, 2002), is an American actress. She is known for her role as Beverly Marsh in the horror films It (2017) and It: Chapter Two (2019) and for her starring role as a teenager with telekinetic abilities in the Netflix drama series I Am Not Okay with This (2020). Lillis has also appeared in the HBO psychological thriller miniseries Sharp Objects (2018), in which she portrayed the younger version of Amy Adams' character in flashbacks.",
        "filmes_ids": [8, 9]},    
    119: {
        "nome": "Bill Skarsgård",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/xBXLx1m0uzhXIbY3wN8lmPGeUHl.jpg",
        "bio": "Bill Istvan Günther Skarsgård (Swedish: born 9 August 1990) is a Swedish actor. He is known for portraying Pennywise in the horror films It (2017) and It Chapter Two (2019), along with the 2025 prequel series It: Welcome to Derry. Other horror appearances were in the series Hemlock Grove (2013,2015) and Castle Rock (2018,2019) and the films Barbarian (2022) and Nosferatu (2024).",
        "filmes_ids": [8, 9]},    
    120: {
        "nome": "Brad Pitt",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/cckcYc2v0yh1tc9QjRelptcOBko.jpg",
        "bio": "William Bradley 'Brad' Pitt (Shawnee, 18 de dezembro de 1963) é um ator e produtor americano. É vencedor de diversos prêmios, dentre os quais um Oscar, dois Globos de Ouro, dois Screen Actors Guild e um BAFTA por atuação, e um Oscar, um BAFTA e um Emmy como produtor; é citado um dos mais bem pagos atores de de Hollywood. Pitt começou sua carreira de ator aparecendo em algumas séries de televisão como Dallas (1987). Posteriormente, ganhou reconhecimento como o cowboy J.D no filme Thelma and Louise (1991).",
        "filmes_ids": [10, 11]},       
    121: {
        "nome": "Jon Bernthal",
        "foto": "https://media.themoviedb.org/t/p/w300_and_h450_face/o0t6EVkJOrFAjESDilZUlf46IbQ.jpg",
        "bio": "Bernthal nasceu e cresceu em Washington onde graduou-se na Sidwell Friends School. Ele estudou no Skidmore College, e em seguida, na Moscow Art Theatre na Rússia, instituição pela qual também jogou baseball profissional, filiado à federação de beisebol profissional europeu. Enquanto em Moscou, foi notado pelo diretor da Formação Avançada de Teatro da Universidade Harvard no American Repertory Theatre.",
        "filmes_ids": [11, 12]}      
}

# --- BANCO DE FILMES (Posters Reais TMDB) ---
BANCO_DE_FILMES = {
    1: {
        "titulo": "Oppenheimer", "ano": 2023, "nota": "9.3", "genero": "Drama", 
        "trailer": "uYPbbksJxIg", "atores_ids": [101, 102, 110, 111],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/1OsQJEoSXBjduuCvDOlRhoEUaHu.jpg",
        "descricao": "A história do físico americano J. Robert Oppenheimer, seu papel no Projeto Manhattan e no desenvolvimento da bomba atômica durante a Segunda Guerra Mundial, e o quanto isso mudaria a história do mundo para sempre."
    },
    2: {
        "titulo": "Interestelar", "ano": 2014, "nota": "9.5", "genero": "Sci-Fi",
        "trailer": "zSWdZVtXT7E", "atores_ids": [103, 112, 113, 114],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/6ricSDD83BClJsFdGB6x7cM0MFQ.jpg",
        "descricao": "As reservas naturais da Terra estão chegando ao fim e um grupo de astronautas recebe a missão de verificar possíveis planetas para receberem a população mundial, possibilitando a continuação da espécie. Cooper é chamado para liderar o grupo e aceita a missão sabendo que pode nunca mais ver os filhos. Ao lado de Brand, Jenkins e Doyle, ele seguirá em busca de um novo lar."
    },
    3: {
        "titulo": "Duna: Parte 2", "ano": 2024, "nota": "9.1", "genero": "Sci-Fi", 
        "trailer": "Way9Dexny3w", "atores_ids": [101],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/8LJJjLjAzAwXS40S5mx79PJ2jSs.jpg",
        "descricao": "A jornada de Paul Atreides continua. Ele está determinado a buscar vingança contra aqueles que destruíram sua família e seu lar. Com a ajuda de Chani e dos Fremen, ele embarca em uma jornada espiritual, mística e marcial. Se torna Muad'Dib, o líder messiânico dos Fremen, enquanto luta para evitar um futuro sombrio que ele testemunhou em visões. No entanto, suas ações inadvertidamente desencadeiam uma Guerra Santa em seu nome, que se espalha pelo universo conhecido. Enquanto enfrenta escolhas difíceis entre o amor por Chani e o destino de seu povo, Paul precisa usar suas habilidades e conhecimentos para evitar o terrível futuro que previu."
    },
    4: {
        "titulo": "A Origem", "ano": 2010, "nota": "8.8", "genero": "Sci-Fi", 
        "trailer": "YoHD9XEInc0", "atores_ids": [104, 101],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/9e3Dz7aCANy5aRUQF745IlNloJ1.jpg",
        "descricao": "Cobb é um ladrão habilidoso que comete espionagem corporativa infiltrando-se no subconsciente de seus alvos durante o estado de sono. Impedido de retornar para sua família, ele recebe a oportunidade de se redimir ao realizar uma tarefa aparentemente impossível: plantar uma ideia na mente do herdeiro de um império. Para realizar o crime perfeito, ele conta com a ajuda do parceiro Arthur, o discreto Eames e a arquiteta de sonhos Ariadne. Juntos, eles correm para que o inimigo não antecipe seus passos."
    },
    5: {
        "titulo": "John Wick - De Volta ao Jogo", "ano": 2014, "nota": "8.5", "genero": "Ação", 
        "trailer": "C0BMx-qxsP4", "atores_ids": [105],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/lBcQGk1ygGM2wYmpypFrPp0YohN.jpg",
        "descricao": "John Wick é um lendário assassino de aluguel aposentado, lidando com o luto após perder o grande amor de sua vida. Quando um gângster invade sua casa, mata seu cachorro e rouba seu carro, ele é forçado a voltar à ativa e inicia sua vingança."
    },
    6: {
        "titulo": "Coringa", "ano": 2019, "nota": "9.0", "genero": "Drama", 
        "trailer": "t433PEQGErc", "atores_ids": [106],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/xLxgVxFWvb9hhUyCDDXxRPPnFck.jpg",
        "descricao": "Isolado, intimidado e desconsiderado pela sociedade, o fracassado comediante Arthur Fleck inicia seu caminho como uma mente criminosa após assassinar três homens em pleno metrô. Sua ação inicia um movimento popular contra a elite de Gotham City, da qual Thomas Wayne é seu maior representante."
    },
    7: {
        "titulo": "Extermínio", "ano": 2003, "nota": "7.2", "genero": "Terror", 
        "trailer": "mWEhfF27O0c", "atores_ids": [101, 107, 108, 109],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/pVTtJSvJoOofD1YoyPSGwWEWmJd.jpg",
        "descricao": "Um poderoso vírus está a solta. Transmitido em uma gota de sangue e com efeito devastador em alguns segundos, o vírus mantém os infectados em um estado permanente de descontrole assassino. Dentro de 28 dias, o país está tomado e um punhado de sobreviventes inicia esforços para garantir algum futuro à raça humana, mas o que não percebem é que o vírus mortal não é a única coisa que os ameaça."
    },
     8: {
        "titulo": "It: A Coisa", "ano": 2017, "nota": "7.2", "genero": "Terror", 
        "trailer": "UllUiLEXB_g", "atores_ids": [115, 116, 117, 118, 119],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/uYxz0lIiNgErrPhQbSjUdwYxtFc.jpg",
        "descricao": "Na cidade de Derry, no Maine, sete jovens se juntam para combater uma criatura sobrenatural que está assombrando a sua cidade por séculos. Chamado de Pennywise – O Palhaço Dançarino, a Coisa é um monstro de força absoluta que toma a forma dos medos mais horrorosos das pessoas. Ameaçados por seus piores pesadelos, a única maneira dos jovens amigos sobreviverem à Coisa é se continuarem juntos."
    },
     9: {
        "titulo": "IT: Capítulo Dois", "ano": 2019, "nota": "6.8", "genero": "Terror", 
        "trailer": "9hTiR6qD3Ow", "atores_ids": [115, 116, 117, 118, 119],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/qjKvLv6Z2D9QWEOdnsrffguazHk.jpg",
        "descricao": "Vinte e sete anos após o Clube dos Otários derrotar Pennywise, It está de volta. Agora adultos Os Otários seguiram com suas vidas, mas com os recentes desaparecimentos em Derry, Mike resolve reunir o grupo novamente. Perturbados pelo passado, eles precisam vencer seus medos para destruir Pennywise, que está ainda mais perigoso, de uma vez por todas."
    },
     10: {
        "titulo": "Era Uma Vez em… Hollywood ", "ano": 2019, "nota": "7.4", "genero": "Comédia", 
        "trailer": "Bbk_ZSh5BWQ", "atores_ids": [104, 120],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/zgr02U2Fh0sR5JtaAXY5yBU1wka.jpg",
        "descricao": "Los Angeles, 1969. O astro de TV Rick Dalton, um ator em dificuldades especializado em faroestes, e o dublê Cliff Booth, seu melhor amigo, tentam sobreviver em uma indústria cinematográfica em constante mudança. Dalton é vizinho da jovem e promissora atriz e modelo Sharon Tate, que acaba de se casar com o prestigiado diretor polonês Roman Polanski."
    },
    11: {
        "titulo": "Corações de Ferro  ", "ano": 2014, "nota": "7.5", "genero": "Guerra", 
        "trailer": "OoKSKzqpPy4", "atores_ids": [120, 121 ],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/tVZXsjBC9HIoKv6WnAv0nWObbrT.jpg",
        "descricao": "Durante o final da Segunda Guerra Mundial, um grupo de cinco soldados americanos é encarregado de atacar os nazistas dentro da própria Alemanha. Apesar de estarem em quantidade inferior e terem poucas armas, eles são liderados pelo enfurecido Wardaddy, sargento que pretende levá-los à vitória, enquanto ensina o novato Norman a lutar."
    },
    12: {
        "titulo": "O Lobo de Wall Street", "ano": 2013, "nota": "8.0", "genero": "Crime", 
        "trailer": "PoSCUsNQVtw", "atores_ids": [121, 104, 103  ],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/sIy0jXDkaMf3SDZGaWcmkC2IOl.jpg",
        "descricao": "Durante seis meses, Jordan Belfort trabalhou duro em uma corretora de Wall Street, seguindo os ensinamentos de seu mentor Mark Hanna. Quando finalmente consegue ser contratado como corretor da firma, acontece o Black Monday, que faz com que as bolsas de vários países caiam repentinamente. Sem emprego e bastante ambicioso, ele acaba trabalhando para uma empresa de fundo de quintal que lida com papéis de baixo valor, que não estão na bolsa de valores. É lá que Belfort tem a idéia de montar uma empresa focada neste tipo de negócio, cujas vendas são de valores mais baixos mas, em compensação, o retorno para o corretor é bem mais vantajoso. Ao lado de Donnie e outros amigos dos velhos tempos, ele cria a Stratton Oakmont, uma empresa que faz com que todos enriqueçam rapidamente e, também, levem uma vida dedicada ao prazer."
    },
    12: {
        "titulo": "Crepúsculo", "ano": 2008, "nota": "6.3", "genero": "Fantasia", 
        "trailer": "nowfetk7su0", "atores_ids": [ ],
        "imagem": "https://media.themoviedb.org/t/p/w300_and_h450_face/o4ki1gYHkP6IWNdwjHvI9vzfpuC.jpg",
        "descricao": "Isabella Swan é uma adolescente que vai morar com seu pai em uma nova cidade depois que sua mãe decide casar-se novamente. No colégio, ela fica fascinada por Edward Cullen, um garoto que esconde um segredo obscuro. Eles se apaixonam, mas Edward sabe que quanto mais avançam no relacionamento, mais ele está colocando Bella e aqueles à sua volta em perigo."
    },
}

@app.route('/')
def home():
    query = request.args.get('q', '').lower()
    if query:
        resultados = {id: f for id, f in BANCO_DE_FILMES.items() if query in f['titulo'].lower()}
    else:
        resultados = BANCO_DE_FILMES
    return render_template('index.html', filmes=resultados, busca=query)

@app.route('/filme/<int:filme_id>')
def detalhes(filme_id):
    filme = BANCO_DE_FILMES.get(filme_id)
    if filme:
        atores_f = {aid: BANCO_DE_ATORES[aid] for aid in filme["atores_ids"]}
        recoms = {id: f for id, f in BANCO_DE_FILMES.items() if f['genero'] == filme['genero'] and id != filme_id}
        return render_template('detalhes.html', filme=filme, atores=atores_f, recomendados=recoms)
    return "Filme não encontrado", 404

@app.route('/ator/<int:ator_id>')
def ator(ator_id):
    ator_d = BANCO_DE_ATORES.get(ator_id)
    if ator_d:
        filmes_at = {fid: BANCO_DE_FILMES[fid] for fid in ator_d["filmes_ids"]}
        return render_template('ator.html', ator=ator_d, filmes=filmes_at)
    return "Ator não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
    # No final do seu app.py, deixe apenas:
if __name__ == '__main__':

    app.run(debug=True)
