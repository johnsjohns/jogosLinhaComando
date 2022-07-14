import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    while (True):
        print("(1) Forca (2) Adivinhação")
        print ("(0) para sair")

        jogo = int(input("Qual jogo? "))

        if(jogo == 1):
            print("Jogando forca")
            forca.jogar()
            escolhe_jogo()
        elif(jogo == 2):
            print("Jogando adivinhação")
            adivinhacao.jogar()
        elif(jogo == 0):
            exit(0)
        print("Pressione ENTER para continuar ...")
        input()
if(__name__ == "__main__"):
    escolhe_jogo()
