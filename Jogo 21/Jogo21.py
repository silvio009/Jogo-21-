import Baralho

def imprime(carta):
    if carta[0] == 1:
        return "A" + carta[1]
    elif carta[0] == 11:
        return "J" + carta[1]
    elif carta[0] == 12:
        return "Q" + carta[1]
    elif carta[0] == 13:
        return "K" + carta[1]
    else:
        return str(carta[0]) + carta[1]

def somaPontos(mao):
    pontos = 0
    for carta in mao:
        if carta[0] > 10:
            pontos = pontos + 10
        else:
            pontos = pontos + carta[0]
    return pontos

def querCarta(mao):
    resp = ""
    for c in mao:
        resp = resp + " " + imprime(c)
    print(resp)    
    print("Pontos: ", somaPontos(mao))

    resp = input("Quer carta (s/n)?")
    if resp == 's':
        return True
    return False

def querCartaCpu(mao):
    if somaPontos(mao) < 16:
        return True
    else:
        return False
    
monte = Baralho.cria()
Baralho.embaralha(monte)

mao_jog = Baralho.distribui(monte, 2)
mao_cpu = Baralho.distribui(monte, 2)

while querCarta(mao_jog):
    c = Baralho.compra(monte)
    mao_jog.append(c)

while querCartaCpu(mao_cpu):
    c = Baralho.compra(monte)
    mao_cpu.append(c)

pontos_hum = somaPontos(mao_jog)    
pontos_cpu = somaPontos(mao_cpu)
if pontos_hum > 21:
    print("CPU venceu!")
elif pontos_cpu > 21:
    print("Você ganhou!")
elif pontos_cpu >= pontos_hum:
    print("CPU ganhou!")
else:
    print("Você ganhou!")        

aux = ""
for c in mao_cpu:
    aux = aux + " " + imprime(c)
print(aux)
print("Pontos CPU: ", somaPontos(mao_cpu))