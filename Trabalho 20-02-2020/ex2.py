import random

cont = 1;

usuario = input("Escolha entre pedra, papel e tesoura: ")
    
while(cont == 1):
    
    computador = random.choice( ['pedra', 'papel', 'tesoura'] )

    if((usuario == 'pedra') or (usuario == 'papel') or (usuario == 'tesoura')):
        if(usuario == 'pedra'):
            if(computador == 'papel'):
                print("O computador ganhou.")
            if(computador == 'tesoura'):
                print("Voce ganhou!")
            if(computador == 'pedra'):
                print("Empate!")
        if(usuario == 'papel'):
            if(computador == 'tesoura'):
                print("O computador ganhou.")
            if(computador == 'pedra'):
                print("Voce ganhou!")
            if(computador == 'papel'):
                print("Empate!")
        if(usuario == 'tesoura'):
            if(computador == 'pedra'):
                print("O computador ganhou.")
            if(computador == 'papel'):
                print("Voce ganhou!")
            if(computador == 'tesoura'):
                print("Empate!")
    else:
        print("Palavra invalida")
    
    print("O computador jogou: " + str(computador))

    cont = int(input("Para continuar digite 1: "))
    print(cont)

    if cont == 1:
        usuario = input("Escolha entre pedra, papel e tesoura: ")
    
