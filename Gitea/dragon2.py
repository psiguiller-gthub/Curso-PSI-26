import random
import time

class Dragon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = random.randint(80, 120)
        self.fuerzaBase = random.randint(15, 25)

    def atacar(self, oponente):
        dano = random.randint(self.fuerzaBase - 5, self.fuerzaBase + 5)
        oponente.vida -= dano
        print(f"\n{self.nombre} lanza un ataque feroz!")
        print(f"{oponente.nombre} recibe {dano} de daño. HP: {max(0, oponente.vida)}")
        time.sleep(0)
    
    def elegir_atacado(self, oponente):
        oponente = random.choice(oponente)
        return oponente

dragon_1 = Dragon("Smaug")
dragon_2 = Dragon("Drogon")
dragon_3 = Dragon("Vilhelm")

luchadores = [dragon_1, dragon_2, dragon_3]

random.shuffle(luchadores) # Mezcla el orden de los luchadores para determinar quién ataca primero.

atacante_inicial = luchadores[0] # yo elijo empezar por luchadores[0].
segundo_atacante = luchadores[1]
tercer_atacante = luchadores[2]

print("--- ¡COMIENZA LA BATALLA! ---")

print(f"{atacante_inicial.nombre} tiene la iniciativa y ataca primero.") 

while len(luchadores) >= 2:
    
    # Elegir aleatoriamente un oponente distinto al atacante
    # posibles_oponentes = [d for d in luchadores if d != atacante_inicial]
    oponente = atacante_inicial.elegir_atacado(luchadores)

    atacante_inicial.atacar(oponente)

    if oponente.vida > 0:
        oponente.atacar(atacante_inicial) # ----------------------- 

    if atacante_inicial.vida <= 0:
        print(f"{atacante_inicial.nombre} ha sido derrotado.")
        luchadores.remove(atacante_inicial)

    if oponente.vida <= 0:
        print(f"{oponente.nombre} ha sido derrotado.")
        luchadores.remove(oponente)

print(f"\n" + "="*30)
print(f"¡EL VENCEDOR ES {luchadores[0].nombre.upper()}!")
print(f"Vida restante: {luchadores[0].vida}")
print("="*30)


            