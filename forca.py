import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo =  open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ['_' for letras in palavra_secreta]

    enforcou = False
    acertou = False


    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ").strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Vocẽ ganhou!")
    else:
        print("Vocẽ perdeu!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
