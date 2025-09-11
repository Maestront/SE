# chatbot_persistente.py
import json
import os

# Nombre del archivo donde guardaremos la base
archivo = "base_conocimiento.json"

if os.path.exists(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        base_conocimiento = json.load(f)
else:
    # Base inicial
    base_conocimiento = {
        "hola": "Hola, ¿cómo estás?",
        "como estas": "Estoy bien, gracias. ¿Y tú?",
        "de que te gustaria hablar": "Podemos hablar de sistemas expertos o de lo que quieras."
    }

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
