import random

aventureros = [
    {"nombre": "Guerrero", "vida": 120, "ataque": 15, "defensa": 10},
    {"nombre": "Arquero",  "vida": 90,  "ataque": 20, "defensa": 5},
    {"nombre": "Mago",     "vida": 70,  "ataque": 30, "defensa": 2}
]

enemigo = {"nombre": "Monstruo", "vida": 150, "ataque": 12, "defensa": 5}

def calcular_daño(puntos_ataque, puntos_defensa, accion_defensor):
    if accion_defensor == "defender":
        return max(0, puntos_ataque - puntos_defensa)
    return puntos_ataque

def ejecutar_turno(jugador, accion_j, rival, accion_r):
    daño_al_rival = calcular_daño(jugador["ataque"], rival["defensa"], accion_r)
    rival["vida"] -= daño_al_rival
    print(f"-> {jugador['nombre']} {accion_j} y causa {daño_al_rival} de daño.")
    
    daño_al_jugador = calcular_daño(rival["ataque"], jugador["defensa"], accion_j)
    jugador["vida"] -= daño_al_jugador
    print(f"-> {rival['nombre']} {accion_r} y causa {daño_al_jugador} de daño.")
    
    print(f"Vida restante - {jugador['nombre']}: {max(0, jugador['vida'])} | {rival['nombre']}: {max(0, rival['vida'])}\n")

def iniciar_juego():
    print("--- SELECCIÓN DE PERSONAJE ---")
    for i, p in enumerate(aventureros):
        print(f"{i}. {p['nombre']} (Vida: {p['vida']}, ATK: {p['ataque']}, DEF: {p['defensa']})")
    
    seleccion = int(input("\nElige el número de tu aventurero: "))
    heroe = aventureros[seleccion]
    
    print(f"\nHas elegido al {heroe['nombre']}. ¡Comienza el combate!")
    
    accion_usuario = input("¿Qué quieres hacer? (atacar/defender): ").lower()
    accion_enemigo = random.choice(["atacar", "defender"])
    
    ejecutar_turno(heroe, accion_usuario, enemigo, accion_enemigo)

if __name__ == "__main__":
    iniciar_juego()