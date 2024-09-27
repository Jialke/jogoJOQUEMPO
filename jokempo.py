from random import choice #importar randomização
#Inicialização de variáveis
jogar = True
pontosJogador1 = 0
pontosJogador2 = 0

# Tradução de jogada de int para string, para ser exibida na tela
listaJogadasTrad = ["pedra", "papel", "tesoura"]

#declaração listaJogadas para jogadas de CPU
listaJogadas = [0,1,2]

#matriz resultados, levando em conta 0-pedra 1-papel 2-tesoura.
m = [["empate","jogador 2", "jogador 1"], ["jogador 1", "empate", "jogador 2"], ["jogador 2", "jogador 1", "empate"]]

#Inicio do Jogo
print('JOgo - Joquempo!')
modoJogo = int(input('Qual modalidade deseja jogar: \n [1] Jogador x Jogador \n [2] Jogador x Computador \n [3] Computador x Computador \n'))
while modoJogo < 1 or modoJogo > 3: #Verificação de existência do modo de jogo
    print('Modo de jogo inválido!')
    modoJogo = int(input('Digite novamente: '))

#Modo Jogador x Jogador
while jogar:
    if modoJogo == 1:
        print('\nJOGADOR X JOGADOR')

        opcaoJogador1 = int(input('\nJogador 1, selecione sua jogada: \n [0] pedra \n [1] papel \n [2] tesoura\n')) #Opção de jogada 1
        while opcaoJogador1 < 0 or opcaoJogador1 > 2: #Verificação de existência da opção de jogada
            print('Opção inválida!')
            opcaoJogador1 = int(input('\nJogador 1, selecione sua jogada: \n [0] pedra \n [1] papel \n [2] tesoura\n'))

        opcaoJogador2 = int(input('Jogador 2, selecione sua jogada: \n [0] pedra \n [1] papel \n [2] tesoura\n')) #Opção de jogada 2
        while opcaoJogador2 < 0 or opcaoJogador2 > 2: #Verificação de existência da opção de jogada
            print('Opção inválida!')
            opcaoJogador2 = int(input('\nJogador 2, selecione sua jogada: \n [0] pedra \n [1] papel \n [2] tesoura\n'))

        print('\nJO QUEM PO!') #Exibir jogada
        print('Jogador 1:', listaJogadasTrad[opcaoJogador1],'\nJogador 2:', listaJogadasTrad[opcaoJogador2])

        #comparações de jogadas
        resultado = m[opcaoJogador1][opcaoJogador2]
        print(resultado)
        if resultado == "jogador 1":
            pontosJogador1 += 1
        elif resultado == "jogador 2":
            pontosJogador2 += 1
        print('\nPlacar do jogo:\n Jogador 1:', pontosJogador1, '\n Jogador 2:', pontosJogador2)

        continuar = int(input('Deseja jogar novamente? \n [1] sim \n [2] não\n')) #Opção de sair ou continuar jogando
        while continuar < 1 or continuar > 2: #Verificação de validação de opção de sair ou continuar
            print('Resposta inválida!')
            continuar = int(input('Deseja jogar novamente? \n [1] sim \n [2] não\n'))
        if continuar == 2:
            jogar = False
            print('\nPlacar final do jogo:\n Jogador 1:', pontosJogador1,'\n Jogador 2:', pontosJogador2)


#Modo Jogador x Computador
    elif modoJogo == 2:
        print('\nJOGADOR X COMPUTADOR')

        opcaoJogador1 = int(input('\nSelecione sua jogada: \n [0] pedra \n [1] papel \n [2] tesoura\n')) #Opção de jogada
        while opcaoJogador1 < 0 or opcaoJogador1 > 2: #Verificação de existência da opção de jogada
            print('Opção inválida!')
            opcaoJogador1 = int(input('\nSelecione sua jogada: \n [0] pedra \n [1] papel \n [2] tesoura\n'))

        opcaoCpu1 = choice(listaJogadas)

        print('\nJO QUEM PO!') #Exibir jogada
        print('Jogador:', listaJogadasTrad[opcaoJogador1],'\nComputador:', listaJogadasTrad[opcaoCpu1])

        #comparações de jogadas
        resultado = m[opcaoJogador1][opcaoCpu1]
        print(resultado)
        if resultado == "jogador 1":
            pontosJogador1 += 1
        elif resultado == "jogador 2":
            pontosJogador2 += 1
        print('\nPlacar do jogo:\n Jogador 1:', pontosJogador1, '\n Jogador 2:', pontosJogador2)

        continuar = int(input('Deseja jogar novamente? \n [1] sim \n [2] não\n')) #Opção de sair ou continuar jogando
        while continuar < 1 or continuar > 2: #Verificação de validação de opção de sair ou continuar
            print('Resposta inválida!')
            continuar = int(input('Deseja jogar novamente? \n [1] sim \n [2] não\n'))
        if continuar == 2:
            jogar = False
            print('\nPlacar final do jogo:\n Jogador:', pontosJogador1,'\n Computador:', pontosJogador2)

#Modo Computador x Computador
    elif modoJogo == 3:
        print('\nCOMPUTADOR X COMPUTADOR')

        opcaoCpu1 = choice(listaJogadas)
        opcaoCpu2 = choice(listaJogadas)

        print('\nJO QUEM PO!') #Exibir jogada
        print('Computador 1:', listaJogadasTrad[opcaoCpu1], '\nComputador 2:', listaJogadasTrad[opcaoCpu2])

        # comparações de jogadas
        resultado = m[opcaoCpu1][opcaoCpu2]
        print(resultado)
        if resultado == "jogador 1":
            pontosJogador1 += 1
        elif resultado == "jogador 2":
            pontosJogador2 += 1
        print('\nPlacar do jogo:\n Jogador 1:', pontosJogador1, '\n Jogador 2:', pontosJogador2)

        continuar = int(input('Deseja jogar novamente? \n [1] sim \n [2] não\n')) #Opção de sair ou continuar jogando
        while continuar < 1 or continuar > 2: #Verificação de validação de opção de sair ou continuar
            print('Resposta inválida!')
            continuar = int(input('Deseja jogar novamente? \n [1] sim \n [2] não\n'))
        if continuar == 2:
            jogar = False
            print('\nPlacar final do jogo:\n Computador 1:', pontosJogador1, '\n Computador 2:', pontosJogador2)

print('\nObrigado por jogar!\nCréditos: Lucas da Costa Paula')