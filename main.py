# from tkinter import *
# (Importa casi todo el modulo de tkinter y nos ahorra poner "tkinter."Label)


import tkinter as tk # Tedioso poner "tk."Label, pero nos ayuda a no confundirnos
from tkinter import ttk # Ttk Nos permite utilizar widgets y estilos mas modernos
from tkinter import PhotoImage # Importa imagenes
from time import * # Importa todo aquello relacionado al tiempo
from threading import * # Nos permite ejecutar hilos que realicen tareas simultaneamente
                      # ↑ Ojo, estos hilos son distintos, los usaremos para que no
                      # se detenga el pomodoro cuando movemos la ventana u otra funcion

class Pomodoro_Timer:

# Tendremos funciones separadas con el fin de una estructura organizada
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("600x300")
        self.ventana.title("Pomodoro Timer")
        self.ventana.tk.call("wm", "iconphoto", self.ventana._w, PhotoImage(file="pomodoro_icox32.png"))

        self.s = ttk.Style()
        self.s.configure("TNoteBook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))

        self.tabulador = ttk.Notebook(self.ventana)
        self.tabulador.pack(fill="both", pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabulador, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabulador, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabulador, width=600, height=100)

        self.tabulador.add(self.tab1, text="Pomodoro")
        self.tabulador.add(self.tab2, text="Short Break")
        self.tabulador.add(self.tab3, text="Long Break")




        self.ventana.mainloop()


    def iniciar_temporizador_hilo(self):
        pass

    def iniciar_temporizador(self):
        pass

    def reinciar_temporizador(self ):
        pass

    def saltar_temporizador(self):
        pass

        self.ventana.mainloop()
Pomodoro_Timer()
