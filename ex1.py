import random

sorteio = random.randint(0,20)

#print(sorteio)

numero = input("Escolha um numero entre 1 e 20: ")
    
while(numero != str(sorteio)):

    if(numero > str(sorteio)):
        print("Numero muito alto")
    if(numero < str(sorteio)):
        print("Numero muito baixo")
        
    numero = input("Escolha um numero entre 1 e 20: ")

if(numero == str(sorteio)):
    print("Parabens, voce acertou")

