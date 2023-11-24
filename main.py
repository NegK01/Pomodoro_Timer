# from tkinter import *
# (Importa casi todo el modulo de tkinter y nos ahorra poner "tkinter."Label)


import tkinter as tk # Tedioso poner "tk."Label, pero nos ayuda a no confundirnos
from tkinter import ttk # Ttk Nos permite utilizar widgets mas modernos
from tkinter import PhotoImage # Importa imagenes
from time import * # Importa todo aquello relacionado al tiempo
from threading import * # Nos permite ejecutar hilos que realicen tareas simultaneamente
                      # ↑ Ojo, estos hilos son distintos, los usaremos para que no
                      # se detenga el pomodoro cuando movemos la ventana u otra funcion

class Pomodoro_Timer:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("600x300")
        self.ventana.title("Pomodoro Timer")
        self.ventana.tk.call("wm", "iconphoto", self.ventana._w, PhotoImage(file="pomodoro_icox32.png"))




        self.ventana.mainloop()


Pomodoro_Timer()
