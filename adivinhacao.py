import random
def jogar():
    print('*'*33)
    print('bem vindo ao jogo de adivinhaçâo!')
    print('*'*33)

    numero_secreto = random.randint(1, 100)
    pontos = 1000
    total_tentativas = 0
    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Dificil')
    nivel = int(input('Qual nível: '))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas+1):
        print(f'\ntentativas {rodada} de {total_tentativas}')
        chute = int(input('digite o seu número entre 1 e 100: '))
        print('Você chutou', chute)
        
        if (chute <1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('\nVocê acertou!')
            print(f'Você fez {pontos} pontos')
            break
        else:
            if (maior):
                print('Você errou, seu chute foi maior que número secreto\n')
            elif (menor):
                print('Você errou, seu chute foi menor que número secreto\n')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print('\nfim de jogo!')

if (__name__ == '__main__'):
    jogar()