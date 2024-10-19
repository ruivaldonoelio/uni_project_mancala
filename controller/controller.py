from model import model
import pickle

def registar_jogador(lista_jogadores, nome_jogador):
    utilizador = {'NomeJogador': nome_jogador, 'NumJogos': 0, 'NumVitórias': 0, 'NumEmpates': 0, 'NumDerrotas': 0}
    lista_jogadores.append(utilizador)

def bubblesort(lista_jogadores):
    
    for i in range(len(lista_jogadores)):
        for j in range(len(lista_jogadores)-i-1):
            if lista_jogadores[j]['NumVitórias'] < lista_jogadores[j+1]['NumVitórias']:
                variavel_temporaria = lista_jogadores[j+1]
                lista_jogadores[j+1] = lista_jogadores[j]
                lista_jogadores[j] = variavel_temporaria
            elif lista_jogadores[j]['NumVitórias'] == lista_jogadores[j+1]['NumVitórias']:
                if lista_jogadores[j]['NomeJogador'] > lista_jogadores[j+1]['NomeJogador']:
                    variavel_temporaria = lista_jogadores[j+1]
                    lista_jogadores[j+1] = lista_jogadores[j]
                    lista_jogadores[j] = variavel_temporaria
                pass
    return lista_jogadores

def verificar_jogador(lista_jogadores,NomeJogador):

    for jogador in lista_jogadores:
        if NomeJogador == jogador["NomeJogador"]:
            return jogador["NomeJogador"]
    return False

def jogo_iniciado(NomeJogadorA, NomeJogadorB, jogo):

    jogo["JogadorA"] = NomeJogadorA
    jogo["JogadorB"] = NomeJogadorB

def jogo_iniciado_auto(NomeJogadorA, jogo, Nivel):

    jogo["JogadorA"] = NomeJogadorA
    jogo["JogadorB"] = "CPU"
    jogo["Nivel"] = Nivel

def jogador_jogando(NomeJogador, jogo):

    if NomeJogador == jogo["JogadorA"] or  NomeJogador == jogo["JogadorB"]:
        return NomeJogador
    return False

def jogada(NomeJogador,jogo, Posiçao):

    if jogo["JogadorA"] == NomeJogador:
        
        mover = sementes(jogo, Posiçao, NomeJogador) 

        if jogo["JogadorB"] == "CPU" and mover != True:
            CPU(jogo, jogo["Nivel"], jogo["JogadorB"])

        if mover == True:
            return True
        else:
            return False
        
    if jogo["JogadorB"] == NomeJogador:

        Posiçao = Posiçao + 7
        mover = sementes(jogo, Posiçao, NomeJogador)

        if mover == True:
            return True
        else:
            return False

def sementes(jogo, Posiçao, Nomejogador):

    inicio = Posiçao + 1
    fim = Posiçao + jogo["tabuleiro"][Posiçao]

    for n in range (inicio, fim + 1):

        if n <= 13 :    
            jogo["tabuleiro"][n] = jogo["tabuleiro"][n] + 1 

        if n >= 14:
            jogo["tabuleiro"][n-14] = jogo["tabuleiro"][n-14] + 1

    jogo["tabuleiro"][Posiçao] = 0

    if fim >= 14:
        fim = fim - 14

    regras = regra_x1(fim, jogo, Nomejogador)

    if regras == True:
        return True
    else:
        return False

def regra_x1(ultimo, jogo, Nomejogador):

    if jogo["JogadorA"] == Nomejogador:
        if ultimo >= 1 and ultimo <= 6:
            if jogo["tabuleiro"][ultimo] == 1:

                tirar = ultimo + 7

                if jogo["tabuleiro"][tirar] != 0:

                    model.roubar (jogo, 7, ultimo, tirar)

                    return False

    if jogo["JogadorB"] == Nomejogador:
        if ultimo >= 8 and ultimo <= 13:
            if jogo["tabuleiro"][ultimo] == 1:

                tirar = ultimo - 7

                if jogo["tabuleiro"][tirar] != 0:

                    model.roubar (jogo, 0, ultimo, tirar)

                    return False

    if ultimo == 7 or ultimo == 0 :
        return True

def CPU(jogo, Nivel, NomeJogador):

    denovo = 0

    if Nivel == "Normal":

        while denovo == 0:

            for posiçao in range (8, 13 + 1):

                casa = jogo['tabuleiro'][posiçao]

                if casa != 0:
                    break
            
            mover = sementes(jogo, posiçao, NomeJogador)
            
            if mover == False:
                denovo = 1

    if Nivel == "Avançado":
        
        while denovo == 0:
                
            posiçao = 14

            for n in range (8, 13 + 1):

                posiçao -= 1

                casa = jogo['tabuleiro'][posiçao]

                if casa != 0:
                    break
    
            mover = sementes(jogo, posiçao, NomeJogador)  

            if mover == False:
                denovo = 1

def desistir(lista_jogadores, NomeJogador,jogo):

    for utilizador in lista_jogadores:
        if utilizador["NomeJogador"] == jogo["JogadorA"]:
            A = utilizador

        if utilizador["NomeJogador"] == jogo["JogadorB"]:
            B = utilizador

    if jogo["JogadorA"] == NomeJogador:

        model.vencedor (B, A)

        model.finalisar(jogo)
            
    if jogo["JogadorB"] == NomeJogador:

        model.vencedor (A, B)

        model.finalisar(jogo)

def fila_vazia(lista_jogadores, jogo):

    for utilizador in lista_jogadores:
        if utilizador["NomeJogador"] == jogo["JogadorA"]:
            A = utilizador

        if utilizador["NomeJogador"] == jogo["JogadorB"]:
            B = utilizador


    if jogo["tabuleiro"][1] == 0 and jogo["tabuleiro"][2] == 0 and jogo["tabuleiro"][3] == 0 and jogo["tabuleiro"][4] == 0 and jogo["tabuleiro"][5] == 0 and jogo["tabuleiro"][6] == 0:

        jogo["tabuleiro"][0] = jogo["tabuleiro"][0] + jogo["tabuleiro"][8] + jogo["tabuleiro"][9] + jogo["tabuleiro"][10] + jogo["tabuleiro"][11] + jogo["tabuleiro"][12] + jogo["tabuleiro"][13]

        dar_pontos(jogo, A, B)

        return True

    if jogo["tabuleiro"][8] == 0 and jogo["tabuleiro"][9] == 0 and jogo["tabuleiro"][10] == 0 and jogo["tabuleiro"][11] == 0 and jogo["tabuleiro"][12] == 0 and jogo["tabuleiro"][13] == 0:
    
        jogo["tabuleiro"][7] = jogo["tabuleiro"][7] + jogo["tabuleiro"][1] + jogo["tabuleiro"][2] + jogo["tabuleiro"][3] + jogo["tabuleiro"][4] + jogo["tabuleiro"][5] + jogo["tabuleiro"][6]

        dar_pontos(jogo, A, B)

        return True

def dar_pontos(jogo, A, B):

    if jogo["tabuleiro"][7] > jogo["tabuleiro"][0]:

        model.vencedor(A, B)

    if jogo["tabuleiro"][7] < jogo["tabuleiro"][0]:

        model.vencedor(B, A)

    if jogo["tabuleiro"][7] == jogo["tabuleiro"][0]:

        B["NumJogos"] = B["NumJogos"] + 1
        B["NumEmpates"] = B["NumEmpates"] + 1

        A["NumJogos"] = A["NumJogos"] + 1
        A["NumEmpates"] = A["NumEmpates"] + 1

def ler_ficheiro(nome_ficheiro):

    with open(nome_ficheiro +'.save', 'rb') as f:
        jogo = pickle.load(f)
        return jogo

def escrever_ficheiro(nome_ficheiro, jogo):

    with open(nome_ficheiro + '.save', 'wb') as f:
        pickle.dump(jogo, f)

