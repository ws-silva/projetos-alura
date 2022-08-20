def jogar():
    print('*'*33)
    print('bem vindo ao jogo da forca!')
    print('*'*33)

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_' ]
    enforcou = False
    acertou = False

    #enquanto nao enforcou e nao acertou
    while(not enforcou and not acertou):
        chute = input('Qual letra??')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                
            index += 1
        print(letras_acertadas)

    print('Fim de jogo')    

if (__name__ == '__main__'):
    jogar()