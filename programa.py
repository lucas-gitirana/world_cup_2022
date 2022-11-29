resposta = 0
from funcoes import *

# Menu do programa
while resposta != 1:
    print('---------------- MENU ----------------')
    print('1. Sair do programa\n 2. Cadastrar equipe\n 3. Cadastrar jogo\n 4. Número total de jogos\n 5. Exibir total de equipes\n 6. Gerar relatório de jogos da Copa\n')
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

                # LEITURA
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

                continuar = input(
                    'Deseja cadastrar nova seleção? (S - Sim; N - Não): ').upper()
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
                    print(
                        f'A equipe com a sigla {abreviacao1} não foi encontrada')
                    break
                else:
                    abreviacao2 = input('Abreviação da seleção 2: ').upper()
                    if not verificar_equipe(abreviacao2):
                        print(f'A equipe {abreviacao2} não está na Copa')
                        break
                    elif fase == 1 and verificar_jogo_grupo(abreviacao1, abreviacao2):
                        print('As equipes não estão no mesmo grupo')

                    elif not (verificar_jogo(fase, abreviacao1, abreviacao2)):

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
                            f'Não é possível realizar esse jogo pela fase {fase}')

                continuar = input(
                    'Deseja cadastrar novo jogo? (S - Sim; N - Não): ').upper()
                if continuar != 'S' and continuar != 'N':
                    print('RESPOSTA INVÁLIDA! Digite somente S ou N')

            # GRAVAÇÃO
            for jogo in jogos:
                gravar_partida(jogo)

        ########################## Total de jogos ##########################
        case 4:
            print(f'Número total de jogos cadastrados: {total_jogos()}')

        ########################## Total de equipes ##########################
        case 5:
            print(f'Número total de equipes cadastradas: {total_equipes()}')

        ########################## Listagem dos jogos ##########################
        case 6:
            relatorio_resultados()
