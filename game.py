import random

gabarito = ['Nome', 'Ataque', 'Velocidade', 'Defesa']

baralho = [
    ['Urso', 200, 150, 100],
    ['Tigre', 200, 250, 50],
    ['Leão', 150, 150, 150],
    ['Lobo', 150, 200, 50],
    ['Crocodilo', 200, 150, 50],
    ['Elefante', 100, 50, 250],
    ['Jabuti', 100, 150, 250],
    ['Gorila', 250, 100, 100]
]


def configurar_jogo():

    baralho_copia = baralho.copy()

    random.shuffle(baralho_copia)

    metade = len(baralho_copia) // 2

    mao_j1 = baralho_copia[:metade]
    mao_j2 = baralho_copia[metade:]

    monte_espera = []

    return mao_j1, mao_j2, monte_espera


def exibir_carta(carta):

    print('\n----- CARTA -----')
    print(f'NOME: {carta[0]}')
    print(f'1 - ATAQUE: {carta[1]}')
    print(f'2 - VELOCIDADE: {carta[2]}')
    print(f'3 - DEFESA: {carta[3]}')


def jogar_single_player():

    mao_j1, mao_j2, monte_espera = configurar_jogo()

    rodada = 1

    while len(mao_j1) > 0 and len(mao_j2) > 0:

        print(f'\n========== RODADA {rodada} ==========')

        carta_j1 = mao_j1[0]
        carta_j2 = mao_j2[0]

        exibir_carta(carta_j1)

        atributo = int(input('\nEscolha um atributo: '))

        valor_j1 = carta_j1[atributo]
        valor_j2 = carta_j2[atributo]

        print(f'\nCarta do computador: {carta_j2[0]}')
        print(f'Valor jogador: {valor_j1}')
        print(f'Valor computador: {valor_j2}')

        if valor_j1 > valor_j2:

            print('\nJogador venceu a rodada!')

            carta_vencedora = mao_j1.pop(0)
            carta_perdedora = mao_j2.pop(0)

            mao_j1.append(carta_vencedora)
            mao_j1.append(carta_perdedora)

            while len(monte_espera) > 0:
                mao_j1.append(monte_espera.pop(0))

        elif valor_j2 > valor_j1:

            print('\nComputador venceu a rodada!')

            carta_vencedora = mao_j2.pop(0)
            carta_perdedora = mao_j1.pop(0)

            mao_j2.append(carta_vencedora)
            mao_j2.append(carta_perdedora)

            while len(monte_espera) > 0:
                mao_j2.append(monte_espera.pop(0))

        else:

            print('\nEMPATE!')

            monte_espera.append(mao_j1.pop(0))
            monte_espera.append(mao_j2.pop(0))

            print('Cartas adicionadas ao monte de espera.')

        print(f'\nCartas Jogador: {len(mao_j1)}')
        print(f'Cartas Computador: {len(mao_j2)}')

        rodada += 1

    print('\n========== FIM DE JOGO ==========')

    if len(mao_j1) > 0:
        print('Jogador venceu o jogo!')

    else:
        print('Computador venceu o jogo!')


def jogar_multiplayer():

    mao_j1, mao_j2, monte_espera = configurar_jogo()

    rodada = 1

    while len(mao_j1) > 0 and len(mao_j2) > 0:

        print(f'\n========== RODADA {rodada} ==========')

        carta_j1 = mao_j1[0]
        carta_j2 = mao_j2[0]

        print('\nVEZ DO JOGADOR 1')
        exibir_carta(carta_j1)

        atributo = int(input('\nEscolha um atributo: '))

        valor_j1 = carta_j1[atributo]
        valor_j2 = carta_j2[atributo]

        print('\nCARTA DO JOGADOR 2')
        exibir_carta(carta_j2)

        if valor_j1 > valor_j2:

            print('\nJogador 1 venceu a rodada!')

            carta_vencedora = mao_j1.pop(0)
            carta_perdedora = mao_j2.pop(0)

            mao_j1.append(carta_vencedora)
            mao_j1.append(carta_perdedora)

            while len(monte_espera) > 0:
                mao_j1.append(monte_espera.pop(0))

        elif valor_j2 > valor_j1:

            print('\nJogador 2 venceu a rodada!')

            carta_vencedora = mao_j2.pop(0)
            carta_perdedora = mao_j1.pop(0)

            mao_j2.append(carta_vencedora)
            mao_j2.append(carta_perdedora)

            while len(monte_espera) > 0:
                mao_j2.append(monte_espera.pop(0))

        else:

            print('\nEMPATE!')

            monte_espera.append(mao_j1.pop(0))
            monte_espera.append(mao_j2.pop(0))

            print('Cartas adicionadas ao monte de espera.')

        print(f'\nCartas Jogador 1: {len(mao_j1)}')
        print(f'Cartas Jogador 2: {len(mao_j2)}')

        rodada += 1

    print('\n========== FIM DE JOGO ==========')

    if len(mao_j1) > 0:
        print('Jogador 1 venceu o jogo!')

    else:
        print('Jogador 2 venceu o jogo!')


def menu():

    opcao = 0

    while opcao != 3:

        print('\n======= SUPER TRUNFO =======')
        print('1 - Single Player')
        print('2 - Multiplayer')
        print('3 - Sair')

        opcao = int(input('\nEscolha uma opção: '))

        if opcao == 1:
            jogar_single_player()

        elif opcao == 2:
            jogar_multiplayer()

        elif opcao == 3:
            print('\nSaindo do jogo...')

        else:
            print('\nOpção inválida!')

menu()