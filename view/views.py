from controller import controller
from model import model

def main ():

    lista_jogadores = [{'NomeJogador': "CPU", 'NumJogos': 0, 'NumVitórias': 0, 'NumEmpates': 0, 'NumDerrotas': 0}]
                                                                           # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 
    jogo = {'JogadorA': None, 'JogadorB': None, 'Nivel': None, 'tabuleiro': [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]}
                                                                           #14 15 16 17 18 19 20 21 22 23 24 25 26 27
    jogo_atual = {"lista_jogadores":lista_jogadores, "jogo": jogo}
                                                                        
    while True:

        comandos = input().split(" ")

        if comandos[0] == "RJ" and  len(comandos) == 2:
            RJ(lista_jogadores, comandos[1])

        elif comandos[0] == "LJ" and  len(comandos) == 1:
            LJ(lista_jogadores)

        elif comandos[0] == "IJ"  and len(comandos) == 3:
            IJ(lista_jogadores,comandos[1], comandos[2], jogo)

        elif comandos[0] == "IJA" and len(comandos) == 3:
            if comandos[2] == "Normal" or comandos[2] == "Avançado":
                IJA(lista_jogadores,comandos[1], comandos[2], jogo)

        elif comandos[0] == "DJ" and  len(comandos) == 1:
            DJ(jogo)

        elif comandos[0] == "J" and len(comandos) == 3:
            J(lista_jogadores,comandos[1], int(comandos[2]), jogo)

        elif comandos[0] == "D" and len(comandos) == 2:
            D(lista_jogadores,comandos[1], jogo)

        elif comandos[0] == "G" and len(comandos) == 2:
            G(comandos[1], jogo_atual)
            
        elif comandos[0] == "L" and len(comandos) == 2:
            jogo_atual = L(comandos[1])
            jogo = jogo_atual["jogo"]
            lista_jogadores = jogo_atual["lista_jogadores"]

        else:
            print("Instrução inválida.")

def RJ (lista_jogadores, NomeJogador):

    verify = controller.verificar_jogador(lista_jogadores,NomeJogador)

    if verify == NomeJogador:
        print ("Jogador existente.")
    else:
        controller.registar_jogador(lista_jogadores,NomeJogador)
        print("Jogador registado com sucesso.")

def LJ (lista_jogadores):

    lista_jogadores = controller.bubblesort(lista_jogadores)

    if len(lista_jogadores) == 0:
        print("Sem jogadores registados.")
    else:

        for posicao in lista_jogadores:
            print(posicao["NomeJogador"],posicao["NumJogos"],posicao["NumVitórias"],posicao["NumEmpates"],posicao["NumDerrotas"])

def IJ (lista_jogadores, NomeJogadorA, NomeJogadorB, jogo):

    NomeJogadorA = controller.verificar_jogador(lista_jogadores,NomeJogadorA)
    NomeJogadorB = controller.verificar_jogador(lista_jogadores,NomeJogadorB)

    if jogo["JogadorA"] == None and jogo["JogadorB"] == None :
        if NomeJogadorA != False and NomeJogadorB != False:

            controller.jogo_iniciado (NomeJogadorA, NomeJogadorB, jogo)
            print("Jogo iniciado com sucesso.")

        else:
            print("Jogador inexistente.")
    else:
        print("Existe um jogo em curso.")

def IJA (lista_jogadores, NomeJogador, Nivel, jogo):

    NomeJogadorA = controller.verificar_jogador(lista_jogadores,NomeJogador)

    if jogo["JogadorA"] == None and jogo["JogadorB"] == None :
        if NomeJogadorA != False:

            controller.jogo_iniciado_auto(NomeJogador, jogo, Nivel)
            print("Jogo automático de nível", Nivel, "iniciado com sucesso.")

        else:
           print("Jogador inexistente.") 
    else:
        print("Existe um jogo em curso.")
        
def DJ (jogo):

    if jogo["JogadorA"] == None and jogo["JogadorB"] == None :
        print("Não existe jogo em curso.")
    else:

        print (jogo["JogadorA"],  "[",jogo['tabuleiro'][1],"]   [",jogo['tabuleiro'][2],"]   [",jogo['tabuleiro'][3],"]   [",jogo['tabuleiro'][4],"]   [",jogo['tabuleiro'][5],"]   [",jogo['tabuleiro'][6],"]   (",jogo['tabuleiro'][7],")")
        print (jogo["JogadorB"],  "[",jogo['tabuleiro'][8],"]   [",jogo['tabuleiro'][9],"]   [",jogo['tabuleiro'][10],"]   [",jogo['tabuleiro'][11],"]   [",jogo['tabuleiro'][12],"]   [",jogo['tabuleiro'][13],"]   (",jogo['tabuleiro'][0],")")

def J (lista_jogadores, NomeJogador, Posiçao, jogo):

    verify1 = controller.verificar_jogador(lista_jogadores,NomeJogador)
    verify2 = controller.jogador_jogando(NomeJogador, jogo)

    if jogo["JogadorA"] != None and  jogo["JogadorB"] != None:
        if verify1 == NomeJogador:
            if verify2 == NomeJogador:
                play = controller.jogada (NomeJogador,jogo, Posiçao)
                fim = controller.fila_vazia(lista_jogadores, jogo)
                if fim == True:
                    print("Jogo terminado.")
                    print(jogo["JogadorA"], jogo["tabuleiro"][7])
                    print(jogo["JogadorB"], jogo["tabuleiro"][0])
                    model.finalisar(jogo)
                else:
                    if play == True:
                        print ("O jogador" ,NomeJogador, "tem direito a outra jogada.")
                    else:
                        print ("Jogada efetuada com sucesso.")
            else:
                print("Jogador não participa no jogo em curso.")
        else:
            print("Jogador inexistente.")
    else:
        print("Não existe jogo em curso.")

def D (lista_jogadores, NomeJogador, jogo): 

    verify1 = controller.verificar_jogador(lista_jogadores,NomeJogador)
    verify2 = controller.jogador_jogando(NomeJogador, jogo)

    if jogo["JogadorA"] != None and  jogo["JogadorB"] != None:
        if verify1 == NomeJogador:
            if verify2 == NomeJogador:

                controller.desistir (lista_jogadores, NomeJogador,jogo,)
                print ("Jogo terminado com sucesso.")

            else:
                print("Jogador não participa no jogo em curso.")
        else:
            print("Jogador inexistente.")
    else:
        print("Não existe jogo em curso.")

def G(nome_ficheiro, jogo_atual):
    controller.escrever_ficheiro(nome_ficheiro, jogo_atual)
    print ("Jogo gravado com sucesso.")

def L(nome_ficheiro):
    jogo = controller.ler_ficheiro(nome_ficheiro)
    print("Jogo lido com sucesso.")
    return jogo
