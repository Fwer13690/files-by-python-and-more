import chess
import random

board = chess.Board()

while not board.is_game_over():
    if board.turn == chess.WHITE:
        # Jugada del usuario
        move = input("Ingrese su jugada: ")
        try:
            board.push_san(move)
        except ValueError:
            print("Movimiento inválido")
            continue
    else:
        # Jugada de la PC
        move = random.choice(list(board.legal_moves))
        board.push(move)
        print("La PC ha jugado: ", move)

    print(board)
