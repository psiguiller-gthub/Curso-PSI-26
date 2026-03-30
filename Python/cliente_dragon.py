import socket
import threading
import sys

IP_EC2 = "98.84.102.78"
PUERTO = 5000
jugando = True 

try:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((IP_EC2, PUERTO))
except Exception as e:
    print(f"Error: No se pudo conectar: {e}")
    sys.exit()

def recibir_datos():
    global jugando
    # El hilo de escucha se detiene si la bandera es False
    while jugando:
        try:
            msg = cliente.recv(1024).decode()
            if not msg:
                jugando = False
                break
            
            partes = msg.split("|")
            if partes[0] == "JEFE_GOLPE":
                print(f"\n[!] El Dragon Jefe ataca: -{partes[1]} HP. Tu vida: {partes[2]}")
            elif partes[0] == "PLAYER_GOLPE":
                print(f"\n[*] Has golpeado al Dragon Jefe. Vida del Jefe: {partes[2]}")
            elif msg == "VICTORIA":
                print("\n\n--- VICTORIA: EL DRAGON JEFE HA SIDO DERROTADO ---")
                jugando = False
            elif msg == "DERROTA":
                print("\n\n--- DERROTA: Has caido en combate ---")
                jugando = False
            
            if jugando:
                print("Escribe 'a' para atacar >> ", end="", flush=True)
        except:
            jugando = False
            break

# Iniciar hilo de recepcion
threading.Thread(target=recibir_datos, daemon=True).start()

print("--- DESAFIO DEL DRAGON JEFE ---")
print("Escribe 'a' y pulsa Enter para atacar. Escribe 'salir' para terminar.\n")

# Bucle principal controlado por la bandera
while jugando:
    try:
        comando = input(">> ").lower()
        if not jugando: 
            break 
        
        if comando == 'a':
            cliente.send(b"ATACAR")
        elif comando == 'salir':
            cliente.send(b"SALIR")
            jugando = False
    except (EOFError, KeyboardInterrupt, BrokenPipeError):
        jugando = False

print("\nConexion cerrada.")
cliente.close()