# Jogo da Forca

from pes import read
from random import seed, choice
from unidecode import unidecode
from datetime import datetime


# recebe um dataFrame com os nome
df = read.Read.read("names.csv")
#retorna a quantidade de nomes no dataFrame
dfCount = int(df["name"].describe().count())


while(True):
    # inicia a semente dos número pseudo randômicos
    seed(datetime.now().microsecond)
    # pega um nome aleatório do DataFrame
    nameOrg = df["name"].values[choice(df.index)].upper()
    # Remove os acentos
    name = unidecode(nameOrg)
    # tamanho da string nome
    tam = len(name)
    # coloca na string _ para cada caractere da string name
    nameDig = "_" *tam
    # armazena os caracteres que formam o boneco
    palito = ["Ô", "|", "/", "\\", "/", "\\"]
    forca = [" ", " ", " ", " ", " ", " "]
    # variáveis a serem utilizadas
    cont = 0
    err = 0
    letra = ""
    letras = []
    while True:
        print('''
             ____
             {}   |
            {}{}{}  |
            {} {}  |
           ......!.....
        '''.format(forca[0], forca[2], forca[1], forca[3], forca[4], forca[5]))

        print("letras já escolhidas: {}".format(letras))
        print("Nome: {}\n\n".format(nameDig))


        # verifica se pode continuar ou se  o jogo
        if err > 5 or forca[5] == "\\" or name == nameDig:
            if err > 5 or forca[5] == "\\":
                print("********************Continue tentando\n********************O nome era: {}".format(nameOrg))
                print('''
                ****************************************
                ****************************************
                **************            **************
                **********    **        **    **********
                ******                            ******
                ***                 /                ***
                *                                      *
                *                 ****                 *
                ***            **      **            ***
                ******     **              **     ******
                ******** **                  ** ********
                **************            **************
                ******************   *******************   
                ****************************************             
                ''')
            else:
                print("********************Parabéns!!!\n********************Você acertou o nome {}".format(nameOrg))
                print('''
                *****          *****
                ***** ******** *****
                *****  ******  *****
                *****    **    *****
                *****    **    *****
                *****    **    *****
                *****  ******  *****
                ||||||||||||||||||||
                
                ''')
            break

        # recebe um caractere
        while True:
            try:
                letra = unidecode(str(input("Escolha uma letra de A a Z: ").upper()))
                if letra.isalpha() and len(letra) == 1 and letras.count(letra) == 0:
                    break
            except:
                print("Não é um caractere válido, digite uma letra de A a Z.")

        # armazena a letra para que não volte a ser digitada
        letras.append(letra)
        cont = name.count(letra)
        # verifica se o nome contém a letra
        if cont > 0:
            nametemp=""
            # caso exista a letra no nome, varre as posições e armazena a(s) letra(s) no nome a ser digitado
            for i in range(0, tam):
                if name[i] == letra:
                    nametemp += letra
                else:
                    nametemp += nameDig[i]
            nameDig = nametemp
            cont = 0
        # caso não tenha a remove uma parte do boneco
        else:
            forca[err] = palito[err]
            err += 1
            print("Infelismente voce errou.")

        print("Erros: "+str(err))

    # recebe um caractere para continuar ounão jogando
    while True:
        try:
            letra = str(input("\n\nDeseja continuar jogando? (S/N): ").upper())
            if letra == "S" or letra == "N":
                break
        except:
            print("Não é (S/N) digite novamente.")

    if letra == "N":
        break
