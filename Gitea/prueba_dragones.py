import random
import time

class Dragon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = random.randint(80, 120)
        self.fuerzaBase = random.randint(15, 25)

    def atacar(self, oponente):
        daño = random.randint(self.fuerzaBase - 5, self.fuerzaBase + 5)
        oponente.vida -= daño
        print(f"\n{self.nombre} lanza un ataque feroz!")
        print(f"{oponente.nombre} recibe {daño} de daño. HP: {max(0, oponente.vida)}")
        time.sleep(1)

def elegir_atacado(self, oponente):
        oponente = random.choice(oponente)
        return oponente

    def victima(self, luchadores):
        for luchador in luchadores:
            if luchador.nombre == victima.nombre:
                luchadores.remove(luchador)


num_dragones = 80
luchadores = []

for i in range(num_dragones):
    luchadores.append(Dragon(i))

print(len(luchadores))

luchadores[70].vida = 0
print(luchadores[70].vida)


while len(luchadores) >= 2:
    for luchador in luchadores:
        print(luchador.victima(luchadores))

        if luchador.victima(luchadores):
            luchadores.remove(luchador)

for luchador in luchadores:
    if luchador.vida <= 0:
        victima = luchador

# victima = oponente.vida <= 0: