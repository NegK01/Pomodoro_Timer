# from tkinter import *
# (Importa casi todo el modulo de tkinter y nos ahorra poner "tkinter."Label)
Import tkinter as tk # Tedioso poner "tk."Label, pero nos ayuda a no confundirnos

from tkinter import PhotoImage # Importa imagenes
from time import * # Importa todo aquello relacionado al tiempo
from threading import * # Nos permite ejecutar hilos que realicen tareas simultaneamente
                      # ↑ Ojo, estos hilos son distintos, los usaremos para que no
                      # se detenga el pomodoro cuando movemos la ventana u otra funcion

class Pomodoro_Timer:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.mainloop()
a
Pomodoro_Timer()
