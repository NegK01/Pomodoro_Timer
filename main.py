# from tkinter import *
# (Importa casi todo el modulo de tkinter y nos ahorra poner "tkinter."Label)

import time  # Importa todo aquello relacionado al tiempo
import tkinter as tk  # Tedioso poner "tk."Label, pero nos ayuda a no confundirnos
from tkinter import ttk  # Ttk Nos permite utilizar widgets y estilos mas modernos
from tkinter import PhotoImage  # Importa imagenes
import threading


# ↑ Nos permite ejecutar hilos que realicen tareas simultáneamente
# Ojo, estos hilos son distintos, los usaremos para que no
# se detenga el pomodoro cuando movamos la ventana o minimicemos

class Pomodoro_Timer:

    # Tendremos funciones separadas con el fin de una estructura organizada
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("600x300")
        self.ventana.title("Pomodoro Timer")
        self.ventana.tk.call("wm", "iconphoto", self.ventana, PhotoImage(file="pomodoro_icox32.png"))

        self.s = ttk.Style()
        self.s.configure("TNoteBook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))

        self.tabulador = ttk.Notebook(self.ventana)
        self.tabulador.pack(fill="both", pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabulador, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabulador, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabulador, width=600, height=100)

        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu", 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu", 48))
        self.short_break_timer_label.pack(pady=20)

        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu", 48))
        self.long_break_timer_label.pack(pady=20)

        self.tabulador.add(self.tab1, text="Pomodoro")
        self.tabulador.add(self.tab2, text="Short Break")
        self.tabulador.add(self.tab3, text="Long Break")

        self.grid_layout = ttk.Frame(self.ventana)
        self.grid_layout.pack(pady=10)

        self.iniciar_boton = ttk.Button(self.grid_layout, text="Iniciar", command=self.iniciar_temporizador_hilo)
        self.iniciar_boton.grid(row=0, column=0)

        self.saltar_boton = ttk.Button(self.grid_layout, text="Saltar", command=self.saltar_temporizador)
        self.saltar_boton.grid(row=0, column=1)

        self.reiniciar_boton = ttk.Button(self.grid_layout, text="Reiniciar", command=self.reiniciar_temporizador)
        self.reiniciar_boton.grid(row=0, column=2)

        self.pomodoro_contador_label = ttk.Label(self.grid_layout, text="Pomodoros: 0", font=("Ubuntu", 16))
        self.pomodoro_contador_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.pomodoros = 0
        self.skipped = False
        self.stopped = False
        self.running = False

        self.ventana.mainloop()

    def iniciar_temporizador_hilo(self):
        if not self.running:
            t = threading.Thread(target=self.iniciar_temporizador)
            t.start()
            self.running = True

    def iniciar_temporizador(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabulador.index(self.tabulador.select()) + 1

        if timer_id == 1:
            full_seconds = 60 * 25
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pomodoro_timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")
                self.ventana.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_contador_label.config(text=f"Pomodoros: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabulador.select(2)
                else:
                    self.tabulador.select(1)
                self.iniciar_temporizador()

        elif timer_id == 2:
            full_seconds = 60 * 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.short_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.ventana.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabulador.select(0)
                self.iniciar_temporizador()

        elif timer_id == 3:
            full_seconds = 60 * 15
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.long_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.ventana.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabulador.select(0)
                self.iniciar_temporizador()
        else:
            print("Invalid Timer id")

    def reiniciar_temporizador(self):
        self.stopped = True
        self.skipped = False
        self.pomodoros = 0
        self.pomodoro_timer_label.config(text="25:00")
        self.short_break_timer_label.config(text="05:00")
        self.long_break_timer_label.config(text="15:00")
        self.pomodoro_contador_label.config(text="Pomodoros: 0")
        self.running = False

    def saltar_temporizador(self):
        current_tab = self.tabulador.index(self.tabulador.select())
        if current_tab == 0:
            self.pomodoro_timer_label.config(text="25:00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text="05:00")
        elif current_tab == 2:
            self.long_break_timer_label.config(text="15:00")

        self.stopped = True
        self.skipped = True


Pomodoro_Timer()
