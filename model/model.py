def finalisar(jogo):

    jogo["JogadorA"] = None
    jogo["JogadorB"] = None
    jogo["Nivel"] = None
    jogo["tabuleiro"] = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]

    return jogo

def roubar (jogo, poço, ultimo, tirar):
    
    jogo["tabuleiro"][poço] = jogo["tabuleiro"][poço] + jogo["tabuleiro"][ultimo] + jogo["tabuleiro"][tirar] 
    jogo["tabuleiro"][ultimo] = 0
    jogo["tabuleiro"][tirar] = 0

def vencedor (vencedor, derrotado):

    vencedor["NumJogos"] = vencedor["NumJogos"] + 1
    vencedor["NumVitórias"] = vencedor["NumVitórias"] + 1

    derrotado["NumJogos"] = derrotado["NumJogos"] + 1
    derrotado["NumDerrotas"] = derrotado["NumDerrotas"] + 1