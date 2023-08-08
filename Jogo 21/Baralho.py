import random

def cria():
    cartas = []
    naipes = ('♣', '♥', '♦️', '♠️')
    for n in naipes:   
        for i in range(1, 14):
            cartas.append((i, n))
    #print(cartas)
    return cartas

def compra(monte: list):
    return monte.pop()

def distribui(monte: list, qtd: int):
    mao = []
    while qtd > 0:
        c = compra(monte)
        mao.append(c)
        qtd = qtd - 1
    return mao

def embaralha(monte: list):
    outra_lista = []
    while len(monte) > 0:
        pos = random.randint(0, len(monte) - 1)
        outra_lista.append(monte.pop(pos))

    for c in outra_lista:    
        monte.append(c)
    #print(monte)

bar = cria()    
embaralha(bar)
c = compra(bar)
print(c)