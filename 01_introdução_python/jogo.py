import adivinhacao
import forca

escolha = int(input('Escolha um kogo \n (1) Adivinhçao (2) Forca'))

if escolha == 1:
    adivinhacao.jogar()
else:
    forca.jogar()