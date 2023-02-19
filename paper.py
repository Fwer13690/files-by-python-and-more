import random

def piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    intentos = 0
    while intentos < 3:
        intentos += 1
        jugador = input("Elige piedra, papel o tijeras (o presiona Enter para salir): ").lower()
        if jugador == "":
            print("Saliendo del juego...")
            break
        elif jugador not in opciones:
            print("Opción no válida. Intenta de nuevo.")
        else:
            computadora = random.choice(opciones)
            print(f"PC: {computadora}.")
            if jugador == computadora:
                print("Empate.")
            elif jugador == "piedra":
                if computadora == "papel":
                    print("Perdiste.")
                else:
                    print("Ganaste.")
            elif jugador == "papel":
                if computadora == "tijeras":
                    print("Perdiste.")
                else:
                    print("Ganaste.")
            elif jugador == "tijeras":
                if computadora == "piedra":
                    print("Perdiste.")
                else:
                    print("Ganaste.")
    print("GAME OVER")

piedra_papel_tijeras()
