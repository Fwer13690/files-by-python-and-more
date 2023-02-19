import random

def cara_o_cruz():
    opciones = ["cara", "cruz"]
    intentos = 0
    while intentos < 3:
        intentos += 1
        jugador = input("Elige cara o cruz (o presiona Enter para salir): ").lower()
        if jugador == "":
            print("Saliendo del juego...")
            break
        elif jugador not in opciones:
            print("Opción no válida. Intenta de nuevo.")
        else:
            computadora = random.choice(opciones)
            print(f"CAYO: {computadora}.")
            if jugador == computadora:
                print("YOU WIN")
            else:
                print("YOU LOSE")
    print("GAME OVER")

cara_o_cruz()
