from preguntas_respuestas import preguntas_respuestas

print("SOY UN BOT YOJUU! ¿En qué puedo ayudarte?")

while True:
    # Leemos la pregunta del usuario
    pregunta = input("Tú: ")

    # Buscamos la respuesta correspondiente en el diccionario
    respuesta = preguntas_respuestas.get(pregunta)

    # Si la respuesta existe, la mostramos en pantalla
    if respuesta:
        print("Chatbot: ", respuesta)
    else:
        print("Chatbot: Lo siento, no tengo la respuesta a esa pregunta.")
