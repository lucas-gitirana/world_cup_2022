# Estudante: Lucas Emanoel Gitirana
# Turma: BSI22

resposta = 0
from funcoes import *
selecoes = []
jogos = []

# Menu do programa
while resposta != 1:
    print('---------------- MENU ----------------')
    print('1. Sair do programa\n 2. Nova equipe\n 3. Novo jogo\n 4. Número total de jogos armazenados\n 5. Número total de equipes armazenadas\n 6. Gravar equipes cadastradas\n 7. Gravar jogos cadastrados\n 8. Listar os jogos que constam no banco\n 9. Gerar relatório de jogos da Copa\n')
    print('--------------------------------------')
    resposta = int(input('Digite o número da operação: '))

    if resposta == 1:
        print('Até logo! :)')
    elif resposta < 1 or resposta > 9:
        print('RESPOSTA INVÁLIDA! \n Digite um número correponde a alguma operação acima')

    match resposta:
        ########################## Cadastro de nova equipe ##########################
        case 2:
            selecoes = []
            continuar = 'S'
            while continuar == 'S':
                selecao = []

                # LEITURA
                print('---------------- CADASTRO DE SELEÇÃO ----------------')
                abreviacao = input('Abreviação do país: ').upper()
                if verificar_equipe(abreviacao) or verificar_equipe_vetor(abreviacao, selecoes):
                    print(f'O país {abreviacao} já foi cadastrado!')
                else:
                    pais = input('Nome do país:').upper()
                    grupo = input('Grupo em que o país está: ').upper()
                    selecao.append(pais)
                    selecao.append(abreviacao)
                    selecao.append(grupo)
                    selecoes.append(selecao)
                    print(selecoes)

                continuar = ''
                while continuar != 'S' and continuar != 'N':
                    continuar = input(
                        'Deseja cadastrar nova seleção? (S - Sim; N - Não): ').upper()
                    if continuar != 'S' and continuar != 'N':
                        print('RESPOSTA INVÁLIDA! Digite somente S ou N')

            

        ########################## Cadastro de novo jogo ##########################
        case 3:
            jogos = []
            continuar = 'S'
            while continuar == 'S':
                jogo = []

                # LEITURA
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
                        print(
                            '1 - Oitavas de final\n2 - Quartas de final \n3 - Semifinal \n4 - Final')
                        etapa = int(
                            input('Informe a etapa das eliminatórias: '))

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
                        print(f'A equipe {abreviacao2} não foi encontrada')
                        break
                    elif fase == 1 and verificar_jogo_grupo(abreviacao1, abreviacao2):
                        print('As equipes não estão no mesmo grupo')
                    elif not verificar_jogo(fase, abreviacao1, abreviacao2) and not verificar_jogo_vetor(fase, abreviacao1, abreviacao2, jogos):

                        print(
                            f'######### {abreviacao1.upper()} X {abreviacao2.upper()} #########')
                        gols_eq1 = int(input(f'Gols do(a) {abreviacao1}: '))
                        gols_eq2 = int(input(f'Gols do(a) {abreviacao2}: '))
                        faltas_eq1 = int(
                            input(f'Faltas cometidas por {abreviacao1}: '))
                        faltas_eq2 = int(
                            input(f'Faltas cometidas por {abreviacao2}: '))

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
                        print(
                            f'Não é possível realizar esse jogo duas vezes pela fase 2')

                continuar = ''
                while continuar != 'S' and continuar != 'N':
                    continuar = input(
                        'Deseja cadastrar novo jogo? (S - Sim; N - Não): ').upper()
                    if continuar != 'S' and continuar != 'N':
                        print('RESPOSTA INVÁLIDA! Digite somente S ou N')

        ########################## Total de jogos ##########################
        case 4:
            print(f'Número total de jogos cadastrados: {total_jogos()}')
            input("Pressione ENTER para continuar: ")

        ########################## Total de equipes ##########################
        case 5:
            print(f'Número total de equipes cadastradas: {total_equipes()}')
            input("Pressione ENTER para continuar: ")

        ########################## Gravação das EQUIPES no banco ##########################
        case 6:
            # Seleções
                for selecao in selecoes:
                    gravar_equipe(selecao)
                    selecoes = []
        
        ########################## Gravação dos JOGOS no banco ##########################
        case 7:          
            # Partidas
                for jogo in jogos:
                    gravar_partida(jogo)
                    jogos = []
        
        ########################## Listar os JOGOS no banco ##########################
        case 8:
            listar_jogos_terminal()
            input("Pressione ENTER para continuar: ")
        
        ########################## Relatório dos jogos ##########################
        case 9:
            relatorio_resultados()
            input("Pressione ENTER para continuar: ")