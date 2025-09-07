# chatbot_simple.py

# Base de conocimiento inicial (diccionario clave:respuesta)
base_conocimiento = {
    "hola": "Hola, ¿cómo estás?",
    "como estas": "Estoy bien, gracias. ¿Y tú?",
    "de que te gustaria hablar": "Podemos hablar de sistemas expertos o de lo que quieras."
}

print("ChatCPT")
print("Escribe 'salir' para terminar.\n")

while True:
    entrada = input("Tú: ").lower().strip()

    if entrada == "salir":
        print("Chatbot: ¡Hasta luego!")
        break

    # Buscar en base de conocimiento
    if entrada in base_conocimiento:
        print("Chatbot:", base_conocimiento[entrada])
    else:
        print("Chatbot: No sé cómo responder eso. ¿Qué debería contestar?")
        nueva_respuesta = input("Tú (define la respuesta): ")
        base_conocimiento[entrada] = nueva_respuesta
        print("Chatbot: ¡Gracias! Ahora lo recordaré.")
