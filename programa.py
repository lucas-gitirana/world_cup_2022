resposta = 0

def gravar_equipe(pais):
    with open("selecoes.csv", "a") as arquivo:
        arquivo.write(str(pais).strip('[]')+'\n')

def gravar_partida(jogo):
    with open("partidas.csv", "a") as arquivo:                            
        arquivo.write('\n' + str(jogo).strip('[]'))

def verificar_equipe(sigla):
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

def verificar_jogo(fase, time1, time2):
    with open("partidas.csv", "r") as arquivo:
        linhas = arquivo.readlines()

        aparicoes = 0
        for linha in linhas:
            vetor = linha.split(',')
            if (str(fase) in vetor[0]) and (time1 in vetor[3] or time1 in vetor[4]) and (time2 in vetor[3] or time2 in vetor[4]):
                aparicoes += 1

        if aparicoes == 0:
            return False
        else:
            return True 

def listar_jogos():
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
        vetores = []

        for linha in linhas:
            vetor = linha.split(',')
            if sigla in vetor[1]:
                return vetor[2]

def listar_grupos():
    with open("selecoes.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        vetores = []

        for i in range(1, len(linhas)):       
            vetor = linhas[i].split(',')
            vetores.append(vetor[2])
        
        conjunto = set(vetores)
        print(conjunto)
        return list(conjunto)

def listar_equipes():
    with open("selecoes.csv", "r") as arquivo:
        linhas = arquivo.readlines()
        vetores = []

        for linha in linhas:
            vetor = linha.split(',')
            vetores.append(vetor)
        
        return vetores

def relatorio_resultados():
    with open("resultados.txt", "w") as arquivo:
        arquivo.write('################# Fase de Grupos #################\n\n\n')
        for grupo in listar_grupos():
            arquivo.write(f'---- GRUPO {grupo} \n')
            for jogo in listar_jogos():
                if '1' in str(jogo[0]):                                    
                    if str(consultar_grupo(jogo[3])) in grupo:
                        arquivo.write(f'{jogo[3]} X {jogo[4]}: \n')
                        arquivo.write(f'Placar: {jogo[5]} x {jogo[6]}\n')
                        arquivo.write(f'Faltas cometidas: {jogo[7]} x {jogo[8]}\n')

# Menu do programa
while resposta != 1 :
    print('---------------- MENU ----------------')
    print('1. Sair do programa\n 2. Cadastrar equipe\n 3. Cadastrar jogo\n 4. Exibir resultados jogos\n 5. Exibir total de equipes\n 6. Listar jogos da Copa\n')
    print('--------------------------------------')
    resposta = int(input('Digite o número da operação: '))

    if resposta == 1:
        print('Até logo! :)')
    elif resposta < 1 or resposta > 7:
        print('RESPOSTA INVÁLIDA! \n Digite um número correponde a alguma operação acima')


    match resposta:
        ########################## Cadastro de nova equipe ##########################
        case 2:
            selecoes = []                    
            continuar = 'S'
            while continuar == 'S':                        
                selecao = []
                
                #LEITURA                
                print('---------------- CADASTRO DE SELEÇÃO ----------------')
                abreviacao = input('Abreviação do país: ').upper()
                if verificar_equipe(abreviacao):
                    print(f'O país {abreviacao} já foi cadastrado!')
                else:
                    pais = input('Nome do país:').upper()             
                    grupo = input('Grupo em que o país está: ').upper()
                    selecao.append(pais)
                    selecao.append(abreviacao)
                    selecao.append(grupo)
                    selecoes.append(selecao)
                    print(selecoes)                
                                
                continuar = input('Deseja cadastrar nova seleção? (S - Sim; N - Não): ').upper()
                if continuar != 'S' and continuar != 'N':
                    print('RESPOSTA INVÁLIDA! Digite somente S ou N')

            # GRAVAÇÃO
            for selecao in selecoes:
                gravar_equipe(selecao)                                                    
        
        ########################## Cadastro de novo jogo ##########################
        case 3:
            jogos = []
            continuar = 'S'
            while continuar == 'S':
                jogo = []

                #LEITURA                
                print('---------------- CADASTRO DE JOGO ----------------')
                fase = 0
                rodada = 0
                etapa = 0
                while (fase < 1) or (fase > 2):
                    print('1 - Fase de grupos \n2 - Eliminatórias')
                    fase = int(input('Informe a fase da competição: '))
                    
                    if fase < 1 or fase > 2:
                        print('Fase inválida! Digite apenas números de 1 a 2.')

                if fase == 1:                
                    while (rodada < 1) or (rodada > 3):
                        rodada = int(input(f'Número da rodada: '))       
                        if rodada < 1 or rodada > 3:
                            print('Rodada inválida! Digite apenas números de 1 a 3.')
                else:
                    rodada = 0
                    while etapa < 1 or etapa > 4:
                        print('1 - Oitavas de final\n2 - Quartas de final \n3 - Semifinal \n4 - Final')
                        etapa = int(input('Informe a etapa das eliminatórias: '))

                        if etapa < 1 or etapa > 4:
                            print('Etapa inválida! Digite apenas números de 1 a 4.')
                
                abreviacao1 = input('Abreviação da seleção 1: ').upper()
                abreviacao2 = ''
                if not verificar_equipe(abreviacao1):
                    print(f'A equipe com a sigla {abreviacao1} não foi encontrada')
                    break
                else:
                    abreviacao2 = input('Abreviação da seleção 2: ').upper()
                    if not verificar_equipe(abreviacao2):
                        print(f'A equipe {abreviacao2} não está na Copa')
                        break
                    else:
                        if not(verificar_jogo(fase, abreviacao1, abreviacao2)):
                
                            print(f'######### {abreviacao1.upper()} X {abreviacao2.upper()} #########')                
                            gols_eq1 = int(input(f'Gols do(a) {abreviacao1}: '))
                            gols_eq2 = int(input(f'Gols do(a) {abreviacao2}: '))
                            faltas_eq1 = int(input(f'Faltas cometidas por {abreviacao1}: '))
                            faltas_eq2 = int(input(f'Faltas cometidas por {abreviacao2}: '))

                            jogo.append(fase)
                            jogo.append(etapa)
                            jogo.append(rodada)
                            jogo.append(abreviacao1)
                            jogo.append(abreviacao2)
                            jogo.append(gols_eq1)
                            jogo.append(gols_eq2)
                            jogo.append(faltas_eq1)
                            jogo.append(faltas_eq2)
                            jogos.append(jogo)
                            jogos.append
                            print(jogos)
                        else:
                            print(f'A partida entre {abreviacao1} e {abreviacao2}, pela fase {fase} já foi cadastrada.')

                continuar = input('Deseja cadastrar novo jogo? (S - Sim; N - Não): ').upper()
                if continuar != 'S' and continuar != 'N':
                    print('RESPOSTA INVÁLIDA! Digite somente S ou N')
                
            # GRAVAÇÃO
            for jogo in jogos:
                gravar_partida(jogo)

        ########################## Listagem dos jogos ##########################
        case 4:
            relatorio_resultados()
                


