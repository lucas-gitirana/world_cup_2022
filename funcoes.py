def gravar_equipe(pais):
    with open("selecoes.csv", "a") as arquivo:
        arquivo.write(str(pais).strip('[]')+'\n')


def gravar_partida(jogo):
    with open("partidas.csv", "a") as arquivo:
        arquivo.write(str(jogo).strip('[]') + '\n')


def verificar_equipe(sigla):
    verificar_arquivo_selecoes('selecoes.csv')
    with open('selecoes.csv', 'r') as arq_selecoes:
        linhas = arq_selecoes.readlines()

        aparicoes = 0
        for linha in linhas:
            vetor = linha.split(',')
            if sigla in vetor[1]:
                aparicoes = aparicoes + 1

    if aparicoes == 0:
        return False
    else:
        return True

def verificar_equipe_vetor(sigla, vetor):
    aparicoes = 0
    for item in vetor:
        if sigla in item[1]:
            aparicoes += 1
    
    if aparicoes == 0:
        return False
    else:
        return True


def verificar_jogo_grupo(sigla1, sigla2):
    if (consultar_grupo(sigla1)) in (consultar_grupo(sigla2)):
        return False
    else:
        return True


def verificar_jogo(fase, time1, time2):
    verificar_arquivo_partidas("partidas.csv")
    with open("partidas.csv", "r") as arquivo:
        linhas = arquivo.readlines()

        aparicoes = 0
        for linha in linhas:
            vetor = linha.split(',')
            if (str(fase) in vetor[0]) and ((time1 in vetor[3] or time1 in vetor[4]) and (time2 in vetor[3] or time2 in vetor[4])):
                aparicoes += 1

        if aparicoes == 0:
            return False
        else:
            return True

def verificar_jogo_vetor(fase, time1, time2, vetor):
    aparicoes = 0

    for item in vetor:            
        if (str(fase) in str(item[0])) and ((time1 in item[3] or time1 in item[4]) and (time2 in item[3] or time2 in item[4])):
            aparicoes += 1            
        
    if aparicoes == 0:
        return False
    else:
        return True


def verificar_arquivo_partidas(nome):
    try:
        arquivo = open(nome, 'r')
    except:
        arquivo = open(nome, 'w')
        arquivo.write(
            'FASE,ETAPA,RODADA,EQUIPE_1,EQUIPE_2,GOLS_EQ1,GOLS_EQ2,FALTAS_EQ1,FALTAS_EQ2\n')

    arquivo.close()


def verificar_arquivo_selecoes(nome):
    try:
        arquivo = open(nome, 'r')
    except:
        arquivo = open(nome, 'w')
        arquivo.write('PAIS,SIG,GRUPO\n')

    arquivo.close()


def listar_jogos():
    verificar_arquivo_partidas("partidas.csv")
    with open("partidas.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        vetores = []

        for linha in linhas:
            vetor = linha.split(',')
            vetores.append(vetor)

        return vetores


def consultar_grupo(sigla):
    with open("selecoes.csv", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            vetor = linha.split(',')
            if sigla in vetor[1]:
                return vetor[2]


def listar_grupos():
    verificar_arquivo_selecoes("selecoes.csv")
    with open("selecoes.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        vetores = []

        for i in range(1, len(linhas)):
            vetor = linhas[i].split(',')
            vetores.append(vetor[2])

        conjunto = set(vetores)
        print(conjunto)
        return sorted(list(conjunto))


def listar_equipes():
    verificar_arquivo_selecoes("selecoes.csv")
    with open("selecoes.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        vetores = []

        for linha in linhas:
            vetor = linha.split(',')
            vetores.append(vetor)

        return vetores


def relatorio_resultados():
    with open("resultados.txt", "w") as arquivo:
        arquivo.write('################# Fase de Grupos #################\n\n')
        for grupo in listar_grupos():
            arquivo.write(f'\n\n GRUPO {grupo} ------------------\n')
            for jogo in listar_jogos():
                if '1' in str(jogo[0]):
                    if str(consultar_grupo(jogo[3])) in grupo:
                        arquivo.write(f'{jogo[3]} X {jogo[4]}: \n')
                        arquivo.write(f'Placar: {jogo[5]} x {jogo[6]}\n')
                        arquivo.write(
                            f'Faltas cometidas: {jogo[7]} x {jogo[8]}\n')

        arquivo.write(
            '\n ################# Oitavas de final #################\n\n\n')
        for jogo in listar_jogos():
            if '2' in str(jogo[0]) and '1' in str(jogo[1]):
                arquivo.write(f'{jogo[3]} X {jogo[4]}: \n')
                arquivo.write(f'Placar: {jogo[5]} x {jogo[6]}\n')
                arquivo.write(f'Faltas cometidas: {jogo[7]} x {jogo[8]}\n')

        arquivo.write(
            '\n ################# Quartas de final #################\n\n\n')
        for jogo in listar_jogos():
            if '2' in str(jogo[0]) and '2' in str(jogo[1]):
                arquivo.write(f'{jogo[3]} X {jogo[4]}: \n')
                arquivo.write(f'Placar: {jogo[5]} x {jogo[6]}\n')
                arquivo.write(f'Faltas cometidas: {jogo[7]} x {jogo[8]}\n')

        arquivo.write(
            '\n ################# Semifinais #################\n\n\n')
        for jogo in listar_jogos():
            if '2' in str(jogo[0]) and '3' in str(jogo[1]):
                arquivo.write(f'{jogo[3]} X {jogo[4]}: \n')
                arquivo.write(f'Placar: {jogo[5]} x {jogo[6]}\n')
                arquivo.write(f'Faltas cometidas: {jogo[7]} x {jogo[8]}\n')

        arquivo.write('\n ################# FINAL #################\n\n\n')
        for jogo in listar_jogos():
            if '2' in str(jogo[0]) and '4' in str(jogo[1]):
                arquivo.write(f'{jogo[3]} X {jogo[4]}: \n')
                arquivo.write(f'Placar: {jogo[5]} x {jogo[6]}\n')
                arquivo.write(f'Faltas cometidas: {jogo[7]} x {jogo[8]}\n')


def total_jogos():
    verificar_arquivo_partidas("partidas.csv")
    with open("partidas.csv", "r") as arquivo:
        return len(arquivo.readlines()) - 1


def total_equipes():
    verificar_arquivo_selecoes("selecoes.csv")
    with open("selecoes.csv", "r") as arquivo:
        return len(arquivo.readlines()) - 1