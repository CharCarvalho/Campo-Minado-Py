import random

def geraBombas():
    tab = []
    i = 0
    while i < 10:
        tab.append([0] * 10)
        i += 1
    minas = random.sample(range(100), 10)
    for bombas in minas:
        linha = bombas // 10
        coluna = bombas % 10
        tab[linha][coluna] = -1
    return tab

def geraNumeros(tab):
    i = 0
    while i < 10:
        j=0
        while j < 10:
            if tab[i][j] == -1:
                if i > 0 and j > 0 and tab[i-1][j-1] != -1:
                    tab[i-1][j-1] += 1
                if i > 0 and tab[i-1][j] != -1:
                    tab[i-1][j] += 1
                if i > 0 and j < 9 and tab[i-1][j+1] != -1:
                    tab[i-1][j+1] += 1
                if j > 0 and tab[i][j-1] != -1:
                    tab[i][j-1] += 1
                if j < 9 and tab[i][j+1] != -1:
                    tab[i][j+1] += 1
                if i < 9 and j > 0 and tab[i+1][j-1] != -1:
                    tab[i+1][j-1] += 1
                if i < 9 and tab[i+1][j] != -1:
                    tab[i+1][j] += 1
                if i < 9 and j < 9 and tab[i+1][j+1] != -1:
                    tab[i+1][j+1] += 1
            j += 1
        i += 1
    return tab 
def imprimeTabuleiro(tab):
    return tab
def geraTela():
    tab = []
    i = 0
    while i < 10:
        tab.append([0] * 10)
        i += 1
    return tab                
       

bombas = geraBombas()
numerosTabuleiro = geraNumeros(bombas)
tabuleiro_jogador = geraTela()

while True:
    iniciar = input("Deseja iniciar o jogo? (s/n): ")
    print("Bem-vindo ao Campo Minado!")
    print("Abaixo se encontra o tabuleiro, digite a linha e a coluna que deseja jogar.")
    print("Lembre-se: As linhas e colunas vão de 1 a 10.")
    print("Boa sorte!")
    for linha in tabuleiro_jogador:
        print(linha)
    cont = 0            
    if iniciar.lower() == "s":
        while True:
            linha = int(input("Digite a linha: "))
            linha_tab = linha - 1
            coluna = int(input("Digite a coluna: "))
            coluna_tab = coluna - 1
            if numerosTabuleiro[linha_tab][coluna_tab] == -1:
                print("EXPLODIU!")
                print("Revelando o jogo...")
                tabuleiro_jogador[linha_tab][coluna_tab] = numerosTabuleiro[linha_tab][coluna_tab]
                for linha in numerosTabuleiro:
                    print(linha)                
                break
            else:
                tabuleiro_jogador[linha_tab][coluna_tab] = numerosTabuleiro[linha_tab][coluna_tab]
                if tabuleiro_jogador[linha_tab][coluna_tab] == 0:
                    if linha_tab > 0 and coluna_tab > 0 and tabuleiro_jogador[linha_tab-1][coluna_tab-1] == 0:
                        tabuleiro_jogador[linha_tab-1][coluna_tab-1] = numerosTabuleiro[linha_tab-1][coluna_tab-1]
                    if linha_tab > 0 and tabuleiro_jogador[linha_tab-1][coluna_tab] == 0:
                        tabuleiro_jogador[linha_tab-1][coluna_tab] = numerosTabuleiro[linha_tab-1][coluna_tab]
                    if linha_tab > 0 and coluna_tab < 9 and tabuleiro_jogador[linha_tab-1][coluna_tab+1] == 0:
                        tabuleiro_jogador[linha_tab-1][coluna_tab+1] = numerosTabuleiro[linha_tab-1][coluna_tab+1]
                    if coluna_tab > 0 and tabuleiro_jogador[linha_tab][coluna_tab-1] == 0:
                        tabuleiro_jogador[linha_tab][coluna_tab-1] = numerosTabuleiro[linha_tab][coluna_tab-1]
                    if coluna_tab < 9 and tabuleiro_jogador[linha_tab][coluna_tab+1] == 0:
                        tabuleiro_jogador[linha_tab][coluna_tab+1] = numerosTabuleiro[linha_tab][coluna_tab+1]
                    if linha_tab < 9 and coluna_tab > 0 and tabuleiro_jogador[linha_tab+1][coluna_tab-1] == 0:
                        tabuleiro_jogador[linha_tab+1][coluna_tab-1] = numerosTabuleiro[linha_tab+1][coluna_tab-1]
                    if linha_tab < 9 and tabuleiro_jogador[linha_tab+1][coluna_tab] == 0:
                        tabuleiro_jogador[linha_tab+1][coluna_tab] = numerosTabuleiro[linha_tab+1][coluna_tab]
                    if linha_tab < 9 and coluna_tab < 9 and tabuleiro_jogador[linha_tab+1][coluna_tab+1] == 0:
                        tabuleiro_jogador[linha_tab+1][coluna_tab+1] = numerosTabuleiro[linha_tab+1][coluna_tab+1]
                for linha in tabuleiro_jogador:
                    print(linha)
                cont += 1
                if cont == 3:
                    continuar = input("Deseja continuar? (s/n): ")
                    if continuar.lower() == "n":
                        print("Obrigado pelo tempo!")
                        break
                    elif continuar.lower() == "s":
                        cont = 0
                        continue        
        break
    elif iniciar.lower() == "n":
        print("Obrigado pelo tempo!")
        break
    else:
        print("Opção inválida, digite novamente.")        
        
