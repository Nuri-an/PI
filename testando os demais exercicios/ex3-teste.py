'''necessario baixar esses pacotes. Use os comandos no propt de comando:
    python -m pip install -U pip
    python -m pip install -U matplotlib'''
import pylab as pl
import numpy as np

# Cria uma figura de tamanho 8x6 pontos, 80 pontos por polegada
pl.figure(figsize=(8, 6), dpi=80)

# Cria uma nova subplotagem a partir de um grid de 1x1
pl.subplot(1, 1, 1)


# X sera um array numpy, 
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C = np.cos(X)
S = np.sin(X)

# Plota o cosseno: (em qual grid, var que possui a funcao, cor&tipo)
pl.plot(X, C, 'g^')

# Plota o seno: (em qual grid, var que possui a funcao, cor&tipo)
pl.plot(X, S, 'rs')

 #cor&tipo
        #cor:[r: red; g: green; b:blue]
        #tipo: [--: dashed; -: solid; s: squares; ^: triangles; o: circle; :: points; -.: dashed whith points; ...:]

# Define os limites em x
pl.xlim(-4.0, 4.0)

# Define as marcas em x
pl.xticks(np.linspace(-4, 4, 9, endpoint=True))

# Define os limites em y
pl.ylim(-1.0, 1.0)

# Define as marcas em y
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Salva a figura usando 72 pontos por polegada
# savefig("sencos.png", dpi=72)

# Mostra o resultado na tela
pl.show()
