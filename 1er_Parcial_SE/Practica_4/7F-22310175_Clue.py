import tkinter as tk
from tkinter import messagebox, ttk
import random

# ---------- Casos DOOM ----------
casos = [
    {
        "culpable": "Marine",
        "arma": "Escopeta",
        "locacion": "Base Espacial",
        "descripciones": {
            "personajes": {
                "Marine": "Marine estaba patrullando la Base Espacial y parecía nervioso.",
                "Imp": "Imp se esconde cerca de los conductos de ventilación.",
                "Cacodemon": "Cacodemon flotaba en silencio, ajeno a todo.",
                "Revenant": "Revenant entrenaba en el pasillo de armas.",
                "Cyberdemon": "Cyberdemon descansaba en la torre, indiferente."
            },
            "armas": {
                "Escopeta": "La Escopeta tiene huellas recientes y está lista.",
                "Lanzacohetes": "El Lanzacohetes parece limpio y sin uso.",
                "Chainsaw": "El Chainsaw está sobre la mesa, intacto.",
                "Pistola de Plasma": "La Pistola de Plasma brilla, pero sin uso reciente.",
                "BFG 9000": "El BFG 9000 reposa, sin signos de actividad."
            },
            "locaciones": {
                "Base Espacial": "Hay señales de lucha en los pasillos de la Base Espacial.",
                "Laboratorio Secreto": "El laboratorio está intacto, sin rastros.",
                "Nivel del Infierno": "Todo tranquilo, sin alteraciones.",
                "Sala de Armas": "Armamento guardado sin uso reciente.",
                "Torre de Control": "Los monitores muestran actividad normal."
            }
        }
    },
    {
        "culpable": "Imp",
        "arma": "Chainsaw",
        "locacion": "Nivel del Infierno",
        "descripciones": {
            "personajes": {
                "Imp": "Imp fue visto merodeando por el Nivel del Infierno con algo extraño.",
                "Marine": "Marine patrullaba, sin notar nada.",
                "Cacodemon": "Cacodemon dormía, ignorando los sucesos.",
                "Revenant": "Revenant practicaba en otra zona.",
                "Cyberdemon": "Cyberdemon descansaba, distante."
            },
            "armas": {
                "Chainsaw": "El Chainsaw tiene restos recientes de uso.",
                "Escopeta": "La Escopeta está limpia y sin rastros.",
                "Lanzacohetes": "El Lanzacohetes parece intacto.",
                "Pistola de Plasma": "Pistola de Plasma sin uso reciente.",
                "BFG 9000": "BFG 9000 sin actividad."
            },
            "locaciones": {
                "Nivel del Infierno": "Se oyen gritos y marcas de lucha en el suelo.",
                "Base Espacial": "Todo en orden, sin alteraciones.",
                "Laboratorio Secreto": "El laboratorio está normal.",
                "Sala de Armas": "Sin uso reciente de armas.",
                "Torre de Control": "Monitores funcionan normalmente."
            }
        }
    },
    {
        "culpable": "Revenant",
        "arma": "Lanzacohetes",
        "locacion": "Sala de Armas",
        "descripciones": {
            "personajes": {
                "Revenant": "Revenant estaba entrenando con el Lanzacohetes en la Sala de Armas.",
                "Marine": "Marine patrullaba, sin percatarse.",
                "Imp": "Imp se escondía en los rincones.",
                "Cacodemon": "Cacodemon dormía.",
                "Cyberdemon": "Cyberdemon vigilaba la torre, indiferente."
            },
            "armas": {
                "Lanzacohetes": "El Lanzacohetes muestra signos recientes de uso.",
                "Escopeta": "La Escopeta sin rastros.",
                "Chainsaw": "Chainsaw intacto.",
                "Pistola de Plasma": "Pistola de Plasma limpia.",
                "BFG 9000": "BFG 9000 sin uso."
            },
            "locaciones": {
                "Sala de Armas": "Hay indicios de actividad reciente en la Sala de Armas.",
                "Base Espacial": "Todo normal.",
                "Laboratorio Secreto": "Sin alteraciones.",
                "Nivel del Infierno": "Silencio absoluto.",
                "Torre de Control": "Monitores normales."
            }
        }
    },
    {
        "culpable": "Cacodemon",
        "arma": "Pistola de Plasma",
        "locacion": "Laboratorio Secreto",
        "descripciones": {
            "personajes": {
                "Cacodemon": "Cacodemon flotaba por el laboratorio con mirada sospechosa.",
                "Marine": "Marine patrullaba en otra zona.",
                "Imp": "Imp se escondía.",
                "Revenant": "Revenant practicaba en la Sala de Armas.",
                "Cyberdemon": "Cyberdemon vigilaba desde la torre."
            },
            "armas": {
                "Pistola de Plasma": "La Pistola de Plasma brilla con actividad reciente.",
                "Escopeta": "Escopeta intacta.",
                "Lanzacohetes": "Lanzacohetes limpio.",
                "Chainsaw": "Chainsaw sin uso.",
                "BFG 9000": "BFG 9000 intacto."
            },
            "locaciones": {
                "Laboratorio Secreto": "Frascos derramados y signos de caos en el laboratorio.",
                "Base Espacial": "Todo normal.",
                "Nivel del Infierno": "Silencio absoluto.",
                "Sala de Armas": "Sin rastros.",
                "Torre de Control": "Todo en orden."
            }
        }
    },
    {
        "culpable": "Cyberdemon",
        "arma": "BFG 9000",
        "locacion": "Torre de Control",
        "descripciones": {
            "personajes": {
                "Cyberdemon": "Cyberdemon estaba en la Torre de Control, manipulando los monitores con intención.",
                "Marine": "Marine patrullaba sin notar nada.",
                "Imp": "Imp escondido en los pasillos.",
                "Revenant": "Revenant entrenando.",
                "Cacodemon": "Cacodemon dormía."
            },
            "armas": {
                "BFG 9000": "El BFG 9000 está cargado y listo, con huellas recientes.",
                "Escopeta": "Escopeta limpia.",
                "Lanzacohetes": "Lanzacohetes sin uso.",
                "Chainsaw": "Chainsaw intacto.",
                "Pistola de Plasma": "Pistola de Plasma limpia"
            },
            "locaciones": {
                "Torre de Control": "Monitores alterados y signos de actividad reciente en la Torre.",
                "Base Espacial": "Todo en orden.",
                "Laboratorio Secreto": "Sin cambios.",
                "Nivel del Infierno": "Silencio total.",
                "Sala de Armas": "Sin alteraciones."
            }
        }
    }
]

# ---------- Clase principal ----------
class ClueDoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Clue DOOM")
        self.root.geometry("900x650")
        self.root.configure(bg="#111111")  # Fondo oscuro estilo DOOM

        self.seleccion_caso = random.choice(casos)

        # Fuentes y colores
        self.fuente_titulo = ("Courier New", 28, "bold")
        self.fuente_normal = ("Courier New", 14, "bold")
        self.color_texto = "#ffff99"
        self.color_boton1 = "#ff3300"
        self.color_boton2 = "#ffcc00"

        # Título
        self.titulo = tk.Label(root, text="CLUE DOOM", font=self.fuente_titulo, bg="#111111", fg="#ff3300")
        self.titulo.pack(pady=15)

        # Frame selección
        self.frame_seleccion = tk.Frame(root, bg="#111111")
        self.frame_seleccion.pack(pady=10)

        # Listas de investigación
        self.personajes = list(self.seleccion_caso["descripciones"]["personajes"].keys())
        self.armas = list(self.seleccion_caso["descripciones"]["armas"].keys())
        self.locaciones = list(self.seleccion_caso["descripciones"]["locaciones"].keys())

        # Combobox personajes
        tk.Label(self.frame_seleccion, text="Personajes:", font=self.fuente_normal, bg="#111111", fg="#ffcc00").grid(row=0, column=0, padx=5, pady=5)
        self.combo_pers = ttk.Combobox(self.frame_seleccion, values=self.personajes, font=self.fuente_normal, width=25)
        self.combo_pers.grid(row=0, column=1, padx=5, pady=5)

        # Combobox armas
        tk.Label(self.frame_seleccion, text="Armas:", font=self.fuente_normal, bg="#111111", fg="#ffcc00").grid(row=1, column=0, padx=5, pady=5)
        self.combo_armas = ttk.Combobox(self.frame_seleccion, values=self.armas, font=self.fuente_normal, width=25)
        self.combo_armas.grid(row=1, column=1, padx=5, pady=5)

        # Combobox locaciones
        tk.Label(self.frame_seleccion, text="Locaciones:", font=self.fuente_normal, bg="#111111", fg="#ffcc00").grid(row=2, column=0, padx=5, pady=5)
        self.combo_loc = ttk.Combobox(self.frame_seleccion, values=self.locaciones, font=self.fuente_normal, width=25)
        self.combo_loc.grid(row=2, column=1, padx=5, pady=5)

        # Frame descripciones
        self.frame_desc = tk.Frame(root, bg="#222222", bd=4, relief="ridge")
        self.frame_desc.pack(pady=20, fill="both", expand=False)
        self.label_desc = tk.Label(self.frame_desc, text="Investiga para obtener descripciones...", font=self.fuente_normal, bg="#222222", fg="#ffff99", justify="left", wraplength=850)
        self.label_desc.pack(padx=10, pady=10)

        # Botones
        self.frame_botones = tk.Frame(root, bg="#111111")
        self.frame_botones.pack(pady=10)
        self.boton_acusar = tk.Button(self.frame_botones, text="Acusar", font=self.fuente_normal, width=18, bg=self.color_boton1, fg="#ffff99", command=self.acusar)
        self.boton_acusar.grid(row=0, column=0, padx=15)
        self.boton_prueba = tk.Button(self.frame_botones, text="Ver Respuesta (Prueba)", font=self.fuente_normal, width=22, bg=self.color_boton2, fg="#111111", command=self.mostrar_respuesta)
        self.boton_prueba.grid(row=0, column=1, padx=15)

        # Animación pulsante
        self.animar_luz_botones()

        # Eventos de selección
        self.combo_pers.bind("<<ComboboxSelected>>", self.actualizar_desc)
        self.combo_armas.bind("<<ComboboxSelected>>", self.actualizar_desc)
        self.combo_loc.bind("<<ComboboxSelected>>", self.actualizar_desc)

    def actualizar_desc(self, event=None):
        texto = ""
        pers = self.combo_pers.get()
        arma = self.combo_armas.get()
        loc = self.combo_loc.get()
        if pers:
            texto += f"{self.seleccion_caso['descripciones']['personajes'][pers]}\n"
        if arma:
            texto += f"{self.seleccion_caso['descripciones']['armas'][arma]}\n"
        if loc:
            texto += f"{self.seleccion_caso['descripciones']['locaciones'][loc]}\n"
        if not texto:
            texto = "Investiga para obtener descripciones..."
        self.label_desc.config(text=texto)

    def acusar(self):
        pers = self.combo_pers.get()
        arma = self.combo_armas.get()
        loc = self.combo_loc.get()
        if pers == self.seleccion_caso["culpable"] and arma == self.seleccion_caso["arma"] and loc == self.seleccion_caso["locacion"]:
            messagebox.showinfo("¡Correcto!", f"¡Has resuelto el caso! El culpable era {pers} con {arma} en {loc}.")
        else:
            messagebox.showerror("Incorrecto", f"No has acertado. Intenta de nuevo.")
        self.reiniciar()

    def mostrar_respuesta(self):
        c = self.seleccion_caso
        messagebox.showinfo("Respuesta", f"Culpable: {c['culpable']}\nArma: {c['arma']}\nLocación: {c['locacion']}")

    def reiniciar(self):
        caso_anterior = self.seleccion_caso
        while True:
            nuevo_caso = random.choice(casos)
            if nuevo_caso != caso_anterior:
                break
        self.seleccion_caso = nuevo_caso

        # Reiniciar combobox
        self.combo_pers.set("")
        self.combo_armas.set("")
        self.combo_loc.set("")
        self.label_desc.config(text="Investiga para obtener descripciones...")

        # Mezclar las listas para que las respuestas no aparezcan arriba
        self.personajes = list(self.seleccion_caso["descripciones"]["personajes"].keys())
        random.shuffle(self.personajes)
        self.armas = list(self.seleccion_caso["descripciones"]["armas"].keys())
        random.shuffle(self.armas)
        self.locaciones = list(self.seleccion_caso["descripciones"]["locaciones"].keys())
        random.shuffle(self.locaciones)

        self.combo_pers.config(values=self.personajes)
        self.combo_armas.config(values=self.armas)
        self.combo_loc.config(values=self.locaciones)


    def animar_luz_botones(self):
        self.pulsante = getattr(self, "pulsante", True)
        color1_boton = "#ff3300" if self.pulsante else "#aa0000"
        color2_boton = "#ffcc00" if self.pulsante else "#ffaa00"
        color_texto = "#ffff99" if self.pulsante else "#ffffff"

        self.boton_acusar.config(bg=color1_boton, fg=color_texto)
        self.boton_prueba.config(bg=color2_boton, fg="#111111")

        style = ttk.Style()
        style.theme_use('default')
        style.configure("TCombobox",
                        fieldbackground="#111111",
                        background="#222222" if self.pulsante else "#333333",
                        foreground="#ffff99",
                        font=("Courier New", 14, "bold"))

        self.pulsante = not self.pulsante
        self.root.after(600, self.animar_luz_botones)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClueDoom(root)
    root.mainloop()
