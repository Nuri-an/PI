import random

sorteio = random.randint(0,20)

print(sorteio)

numero = int(input("Escolha um numero entre 0 e 20: "))
    
while(numero != sorteio):

    if(numero > sorteio):
        print("Numero muito alto")
    if(numero < sorteio):
        print("Numero muito baixo")
        
    numero = int(input("Escolha um numero entre 1 e 20: "))

if(numero == sorteio):
    print("Parabens, voce acertou")

