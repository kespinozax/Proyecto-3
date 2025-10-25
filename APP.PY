import tkinter as tk
from tkinter import messagebox
from functools import partial
from tkinter import simpledialog
from tkinter import ttk
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# ---------------- Clase Proceso ----------------
class Proceso:
    contador_pid = 1
    def __init__(self, nombre, llegada, duracion, quantum=None):
        self.pid = Proceso.contador_pid
        Proceso.contador_pid += 1
        self.nombre = nombre
        self.llegada = llegada
        self.duracion = duracion
        self.restante = duracion
        self.quantum = quantum
        self.finalizacion = 0
        self.retorno = 0
        self.espera = 0
        self.inicio = None

# ---------------- Algoritmos ----------------
def fcfs_tick(procesos):
    for p in procesos:
        p.restante = p.duracion
        p.inicio = None
        p.finalizacion = 0
        p.retorno = 0
        p.espera = 0
    tiempo = 0
    historial = []
    cola = []
    current = None
    pendientes = sorted(procesos, key=lambda x: x.llegada)
    while pendientes or cola or current:
        while pendientes and pendientes[0].llegada == tiempo:
            cola.append(pendientes.pop(0))
        if current is None and cola:
            current = cola.pop(0)
            if current.inicio is None:
                current.inicio = tiempo
        for q in cola:
            q.espera += 1
        esperas_con_pos = [(q.nombre, i+1) for i, q in enumerate(cola)]
        en_cpu_nombre = current.nombre if current else None
        historial.append((tiempo, en_cpu_nombre, esperas_con_pos))
        if current:
            current.restante -= 1
            if current.restante == 0:
                current.finalizacion = tiempo + 1
                current.retorno = current.finalizacion - current.llegada
                current = None
        tiempo += 1
    return historial, procesos

# Aquí podrías agregar SJF, SRTF o RR usando la misma estructura de FCFS

def sjf_tick(procesos):
    for p in procesos:
        p.restante = p.duracion
        p.espera = 0
        p.inicio = None
        p.finalizacion = 0
        p.retorno = 0

    tiempo = 0
    historial = []
    cola = []
    current = None
    pendientes = sorted(procesos, key=lambda x: x.llegada)

    while pendientes or cola or current:
        while pendientes and pendientes[0].llegada == tiempo:
            cola.append(pendientes.pop(0))

        if current is None and cola:
            # elegir el proceso más corto
            cola.sort(key=lambda x: x.duracion)
            current = cola.pop(0)
            if current.inicio is None:
                current.inicio = tiempo

        for q in cola:
            q.espera += 1

        esperas_con_pos = [(q.nombre, i+1) for i, q in enumerate(cola)]
        en_cpu_nombre = current.nombre if current else None
        historial.append((tiempo, en_cpu_nombre, esperas_con_pos))

        if current:
            current.restante -= 1
            if current.restante == 0:
                current.finalizacion = tiempo + 1
                current.retorno = current.finalizacion - current.llegada
                current = None

        tiempo += 1

    return historial, procesos
# ------------------------------------------------------
# -----------------------------------------------------

def rr_tick(procesos, quantum):
    for p in procesos:
        p.restante = p.duracion
        p.espera = 0
        p.inicio = None
        p.finalizacion = 0
        p.retorno = 0

    tiempo = 0
    historial = []
    cola = []
    current = None
    q_restante = 0
    pendientes = sorted(procesos, key=lambda x: x.llegada)

    while pendientes or cola or current:
        while pendientes and pendientes[0].llegada == tiempo:
            cola.append(pendientes.pop(0))

        if current is None and cola:
            current = cola.pop(0)
            q_restante = quantum
            if current.inicio is None:
                current.inicio = tiempoimport tkinter as tk
from tkinter import messagebox
from functools import partial
from tkinter import simpledialog
from tkinter import ttk
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# ---------------- Clase Proceso ----------------
class Proceso:
    contador_pid = 1
    def __init__(self, nombre, llegada, duracion, quantum=None):
        self.pid = Proceso.contador_pid
        Proceso.contador_pid += 1
        self.nombre = nombre
        self.llegada = llegada
        self.duracion = duracion
        self.restante = duracion
        self.quantum = quantum
        self.finalizacion = 0
        self.retorno = 0
        self.espera = 0
        self.inicio = None

# ---------------- Algoritmos ----------------
def fcfs_tick(procesos):
    for p in procesos:
        p.restante = p.duracion
        p.inicio = None
        p.finalizacion = 0
        p.retorno = 0
        p.espera = 0
    tiempo = 0
    historial = []
    cola = []
    current = None
    pendientes = sorted(procesos, key=lambda x: x.llegada)
    while pendientes or cola or current:
        while pendientes and pendientes[0].llegada == tiempo:
            cola.append(pendientes.pop(0))
        if current is None and cola:
            current = cola.pop(0)
            if current.inicio is None:
                current.inicio = tiempo
        for q in cola:
            q.espera += 1
        esperas_con_pos = [(q.nombre, i+1) for i, q in enumerate(cola)]
        en_cpu_nombre = current.nombre if current else None
        historial.append((tiempo, en_cpu_nombre, esperas_con_pos))
        if current:
            current.restante -= 1
            if current.restante == 0:
                current.finalizacion = tiempo + 1
                current.retorno = current.finalizacion - current.llegada
                current = None
        tiempo += 1
    return historial, procesos

# Aquí podrías agregar SJF, SRTF o RR usando la misma estructura de FCFS

def sjf_tick(procesos):
    for p in procesos:
        p.restante = p.duracion
        p.espera = 0
        p.inicio = None
        p.finalizacion = 0
        p.retorno = 0

    tiempo = 0
    historial = []
    cola = []
    current = None
    pendientes = sorted(procesos, key=lambda x: x.llegada)

    while pendientes or cola or current:
        while pendientes and pendientes[0].llegada == tiempo:
            cola.append(pendientes.pop(0))

        if current is None and cola:
            # elegir el proceso más corto
            cola.sort(key=lambda x: x.duracion)
            current = cola.pop(0)
            if current.inicio is None:
                current.inicio = tiempo

        for q in cola:
            q.espera += 1

        esperas_con_pos = [(q.nombre, i+1) for i, q in enumerate(cola)]
        en_cpu_nombre = current.nombre if current else None
        historial.append((tiempo, en_cpu_nombre, esperas_con_pos))

        if current:
            current.restante -= 1
            if current.restante == 0:
                current.finalizacion = tiempo + 1
                current.retorno = current.finalizacion - current.llegada
                current = None

        tiempo += 1

    return historial, procesos
# ------------------------------------------------------

def srtf_tick(procesos):
    for p in procesos:
        p.restante = p.duracion
        p.espera = 0
        p.inicio = None
        p.finalizacion = 0
        p.retorno = 0

    tiempo = 0
    historial = []
    pendientes = sorted(procesos, key=lambda x: x.llegada)
    cola = []
    current = None

    while pendientes or cola or current:
        while pendientes and pendientes[0].llegada == tiempo:
            cola.append(pendientes.pop(0))

        # elegir proceso con menor tiempo restante
        if cola or current:
            candidatos = cola[:]
            if current:
                candidatos.append(current)
            candidatos.sort(key=lambda x: x.restante)
            if candidatos[0] != current:
                if current and current != candidatos[0]:
                    cola.append(current)
                current = candidatos[0]
                if current in cola:
                    cola.remove(current)
                if current.inicio is None:
                    current.inicio = tiempo

        for q in cola:
            q.espera += 1

        esperas_con_pos = [(q.nombre, i+1) for i, q in enumerate(cola)]
        en_cpu_nombre = current.nombre if current else None
        historial.append((tiempo, en_cpu_nombre, esperas_con_pos))

        if current:
            current.restante -= 1
            if current.restante == 0:
                current.finalizacion = tiempo + 1
                current.retorno = current.finalizacion - current.llegada
                current = None

        tiempo += 1

    return historial, procesos
# -----------------------------------------------------

def rr_tick(procesos, quantum):
    for p in procesos:
        p.restante = p.duracion
        p.espera = 0
        p.inicio = None
        p.finalizacion = 0
        p.retorno = 0

    tiempo = 0
    historial = []
    cola = []
    current = None
    q_restante = 0
    pendientes = sorted(procesos, key=lambda x: x.llegada)

    while pendientes or cola or current:
        while pendientes and pendientes[0].llegada == tiempo:
            cola.append(pendientes.pop(0))

        if current is None and cola:
            current = cola.pop(0)
            q_restante = quantum
            if current.inicio is None:
                current.inicio = tiempo

        for q in cola:
            q.espera += 1

        esperas_con_pos = [(q.nombre, i+1) for i, q in enumerate(cola)]
        en_cpu_nombre = current.nombre if current else None
        historial.append((tiempo, en_cpu_nombre, esperas_con_pos))

        if current:
            current.restante -= 1
            q_restante -= 1
            if current.restante == 0:
                current.finalizacion = tiempo + 1
                current.retorno = current.finalizacion - current.llegada
                current = None
            elif q_restante == 0:
                cola.append(current)
                current = None

        tiempo += 1

    return historial, procesos

# ---------------- Función de animación ----------------
def animar(procesos, algoritmo="FCFS", quantum=2, intervalo_ms=5000):


    if algoritmo == "FCFS":
        historial, resultados = fcfs_tick(procesos)
    elif algoritmo == "SJF":
        historial, resultados = sjf_tick(procesos)
    elif algoritmo == "SRTF":
        historial, resultados = srtf_tick(procesos)
    elif algoritmo == "ROUND ROBIN":
        historial, resultados = rr_tick(procesos,quantum)
    else:
        
        messagebox.showinfo("Info", f"Algoritmo {algoritmo} no implementado todavía")
        return

    colores = {p.nombre: (random.random(), random.random(), random.random()) for p in procesos}
    procesos_unicos = [p.nombre for p in procesos]
    tiempo_total = historial[-1][0] + 1 if historial else 0

    fig = plt.figure(figsize=(12, 8))
    gs = fig.add_gridspec(3, 1, height_ratios=[2, 1, 1.6])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])

    ax1.set_yticks(range(len(procesos_unicos)))
    ax1.set_yticklabels(procesos_unicos)
    ax1.set_title(f"Diagrama de Gantt - {algoritmo}")
    ax1.set_ylabel("Procesos")
    ax1.set_xlim(0, tiempo_total)
    ax1.grid(axis="x", linestyle="--", alpha=0.6)

    ax2.set_yticks([])
    ax2.set_title("CPU en tiempo real")
    ax2.set_xlabel("Tiempo")
    ax2.set_xlim(0, tiempo_total)
    ax2.grid(axis="x", linestyle="--", alpha=0.6)

    data = {
        "PID": [p.pid for p in resultados],
        "Proceso": [p.nombre for p in resultados],
        "Llegada": [p.llegada for p in resultados],
        "Duración": [p.duracion for p in resultados],
        "Inicio": [p.inicio for p in resultados],
        "Espera": [p.espera for p in resultados],
        "Finalización": [p.finalizacion for p in resultados],
        "Retorno": [p.retorno for p in resultados],
    }
    df = pd.DataFrame(data)
    ax3.axis("off")
    tabla = ax3.table(cellText=df.values, colLabels=df.columns,
                      loc="center", cellLoc="center")
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(9)
    tabla.scale(1.2, 1.2)
    ax3.set_title("Métricas de Procesos", pad=8)

    def update(frame):
        t, en_cpu, esperas = historial[frame]
        for nombre, pos in esperas:
            idx = procesos_unicos.index(nombre)
            ax1.barh(idx, 1, left=t, color="lightgray", edgecolor="black")
            ax1.text(t + 0.5, idx, str(pos), ha="center", va="center", fontsize=8, color="black")
        if en_cpu:
            idx = procesos_unicos.index(en_cpu)
            ax1.barh(idx, 1, left=t, color=colores[en_cpu], edgecolor="black")
            ax2.barh(0, 1, left=t, color=colores[en_cpu], edgecolor="black")
            ax2.text(t + 0.5, 0, en_cpu, ha="center", va="center", fontsize=9, color="white")
        return []

    ani = animation.FuncAnimation(fig, update, frames=len(historial), interval=intervalo_ms, blit=False, repeat=False)
    plt.tight_layout()
    plt.show()

# ---------------- GUI ----------------
class App:
    def __init__(self, root):
        self.root = root
        root.title("Planificador de Procesos")
        self.procesos = []

        # 🔹 Procesos de prueba iniciales
        self.procesos = [
            Proceso("P1", llegada=0, duracion=5),
            Proceso("P2", llegada=2, duracion=3),
            Proceso("P3", llegada=4, duracion=1),
            Proceso("P4", llegada=6, duracion=7),
        ]

        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.agregar_btn = tk.Button(self.frame_botones, text="Agregar Proceso", command=self.agregar_proceso)
        self.agregar_btn.pack(side=tk.LEFT, padx=5)

        self.eliminar_btn = tk.Button(self.frame_botones, text="Eliminar Proceso", command=self.eliminar_proceso)
        self.eliminar_btn.pack(side=tk.LEFT, padx=5)

        # ================= Quantum Entry =================
        self.frame_quantum = tk.Frame(root)
        self.frame_quantum.pack(pady=5)

        tk.Label(self.frame_quantum, text="Quantum :").pack(side=tk.LEFT)

        # Validador para que solo acepte números
        vcmd = (root.register(self.validar_numero), "%P")
        self.quantum_entry = tk.Entry(self.frame_quantum, width=5, validate="key", validatecommand=vcmd)
        self.quantum_entry.insert(0, "2")  # Valor por defecto
        self.quantum_entry.pack(side=tk.LEFT, padx=5)
        

        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10)

        self.lista_label = tk.Label(self.frame_lista, text="Procesos actuales:")
        self.lista_label.pack()
        self.lista_procesos = tk.Listbox(self.frame_lista, width=40)
        self.lista_procesos.pack()

# 🔹 Refrescar inmediatamente para que se muestren los de prueba
        self.actualizar_lista()
            
        self.frame_algoritmos = tk.Frame(root)
        self.frame_algoritmos.pack(pady=10)

        self.fcfs_btn = tk.Button(self.frame_algoritmos, text="FCFS", command=partial(self.ejecutar, "FCFS"))
        self.fcfs_btn.pack(side=tk.LEFT, padx=5)
        self.sjf_btn = tk.Button(self.frame_algoritmos, text="SJF", command=partial(self.ejecutar, "SJF"))
        self.sjf_btn.pack(side=tk.LEFT, padx=5)
        self.rr_btn = tk.Button(self.frame_algoritmos, text="ROUND ROBIN", command=partial(self.ejecutar, "ROUND ROBIN"))
        self.rr_btn.pack(side=tk.LEFT, padx=5)



    # ---------------- Validación de números ----------------
    def validar_numero(self, valor):
        return valor.isdigit() or valor == ""

    def agregar_proceso(self):
        nombre = simpledialog.askstring("Nombre", "Nombre del proceso:")
        llegada = simpledialog.askinteger("Llegada", "Tiempo de llegada:")
        duracion = simpledialog.askinteger("Duración", "Duración del proceso:")
        if nombre and llegada is not None and duracion is not None:
            self.procesos.append(Proceso(nombre, llegada, duracion))
            self.actualizar_lista()

    def eliminar_proceso(self):
        selected = self.lista_procesos.curselection()
        if selected:
            idx = selected[0]
            self.procesos.pop(idx)
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_procesos.delete(0, tk.END)
        for p in self.procesos:
            self.lista_procesos.insert(tk.END, f"{p.nombre} | Llegada: {p.llegada} | Duración: {p.duracion}")

    def ejecutar(self, algoritmo):
        if not self.procesos:
            messagebox.showwarning("Atención", "No hay procesos para ejecutar")
            return
        # Leer quantum desde el Entry
        try:
            quantum = int(self.quantum_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Quantum inválido, usando 2 por defecto")
            quantum = 2
        animar(list(self.procesos), algoritmo=algoritmo, quantum=quantum)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


        for q in cola:
            q.espera += 1

        esperas_con_pos = [(q.nombre, i+1) for i, q in enumerate(cola)]
        en_cpu_nombre = current.nombre if current else None
        historial.append((tiempo, en_cpu_nombre, esperas_con_pos))

        if current:
            current.restante -= 1
            q_restante -= 1
            if current.restante == 0:
                current.finalizacion = tiempo + 1
                current.retorno = current.finalizacion - current.llegada
                current = None
            elif q_restante == 0:
                cola.append(current)
                current = None

        tiempo += 1

    return historial, procesos

# ---------------- Función de animación ----------------
def animar(procesos, algoritmo="FCFS", quantum=2, intervalo_ms=5000):


    if algoritmo == "FCFS":
        historial, resultados = fcfs_tick(procesos)
    elif algoritmo == "SJF":
        historial, resultados = sjf_tick(procesos)
    elif algoritmo == "ROUND ROBIN":
        historial, resultados = rr_tick(procesos,quantum)
    else:
        
        messagebox.showinfo("Info", f"Algoritmo {algoritmo} no implementado todavía")
        return

    colores = {p.nombre: (random.random(), random.random(), random.random()) for p in procesos}
    procesos_unicos = [p.nombre for p in procesos]
    tiempo_total = historial[-1][0] + 1 if historial else 0

    fig = plt.figure(figsize=(12, 8))
    gs = fig.add_gridspec(3, 1, height_ratios=[2, 1, 1.6])
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])

    ax1.set_yticks(range(len(procesos_unicos)))
    ax1.set_yticklabels(procesos_unicos)
    ax1.set_title(f"Diagrama de Gantt - {algoritmo}")
    ax1.set_ylabel("Procesos")
    ax1.set_xlim(0, tiempo_total)
    ax1.grid(axis="x", linestyle="--", alpha=0.6)

    ax2.set_yticks([])
    ax2.set_title("CPU en tiempo real")
    ax2.set_xlabel("Tiempo")
    ax2.set_xlim(0, tiempo_total)
    ax2.grid(axis="x", linestyle="--", alpha=0.6)

    data = {
        "PID": [p.pid for p in resultados],
        "Proceso": [p.nombre for p in resultados],
        "Llegada": [p.llegada for p in resultados],
        "Duración": [p.duracion for p in resultados],
        "Inicio": [p.inicio for p in resultados],
        "Espera": [p.espera for p in resultados],
        "Finalización": [p.finalizacion for p in resultados],
        "Retorno": [p.retorno for p in resultados],
    }
    df = pd.DataFrame(data)
    ax3.axis("off")
    tabla = ax3.table(cellText=df.values, colLabels=df.columns,
                      loc="center", cellLoc="center")
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(9)
    tabla.scale(1.2, 1.2)
    ax3.set_title("Métricas de Procesos", pad=8)

    def update(frame):
        t, en_cpu, esperas = historial[frame]
        for nombre, pos in esperas:
            idx = procesos_unicos.index(nombre)
            ax1.barh(idx, 1, left=t, color="lightgray", edgecolor="black")
            ax1.text(t + 0.5, idx, str(pos), ha="center", va="center", fontsize=8, color="black")
        if en_cpu:
            idx = procesos_unicos.index(en_cpu)
            ax1.barh(idx, 1, left=t, color=colores[en_cpu], edgecolor="black")
            ax2.barh(0, 1, left=t, color=colores[en_cpu], edgecolor="black")
            ax2.text(t + 0.5, 0, en_cpu, ha="center", va="center", fontsize=9, color="white")
        return []

    ani = animation.FuncAnimation(fig, update, frames=len(historial), interval=intervalo_ms, blit=False, repeat=False)
    plt.tight_layout()
    plt.show()

# ---------------- GUI ----------------
class App:
    def __init__(self, root):
        self.root = root
        root.title("Planificador de Procesos")
        self.procesos = []

        # 🔹 Procesos de prueba iniciales
        self.procesos = [
            Proceso("P1", llegada=0, duracion=5),
            Proceso("P2", llegada=2, duracion=3),
            Proceso("P3", llegada=4, duracion=1),
            Proceso("P4", llegada=6, duracion=7),
        ]

        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.agregar_btn = tk.Button(self.frame_botones, text="Agregar Proceso", command=self.agregar_proceso)
        self.agregar_btn.pack(side=tk.LEFT, padx=5)

        self.eliminar_btn = tk.Button(self.frame_botones, text="Eliminar Proceso", command=self.eliminar_proceso)
        self.eliminar_btn.pack(side=tk.LEFT, padx=5)

        # ================= Quantum Entry =================
        self.frame_quantum = tk.Frame(root)
        self.frame_quantum.pack(pady=5)

        tk.Label(self.frame_quantum, text="Quantum :").pack(side=tk.LEFT)

        # Validador para que solo acepte números
        vcmd = (root.register(self.validar_numero), "%P")
        self.quantum_entry = tk.Entry(self.frame_quantum, width=5, validate="key", validatecommand=vcmd)
        self.quantum_entry.insert(0, "2")  # Valor por defecto
        self.quantum_entry.pack(side=tk.LEFT, padx=5)
        

        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10)

        self.lista_label = tk.Label(self.frame_lista, text="Procesos actuales:")
        self.lista_label.pack()
        self.lista_procesos = tk.Listbox(self.frame_lista, width=40)
        self.lista_procesos.pack()

# 🔹 Refrescar inmediatamente para que se muestren los de prueba
        self.actualizar_lista()
            
        self.frame_algoritmos = tk.Frame(root)
        self.frame_algoritmos.pack(pady=10)

        self.fcfs_btn = tk.Button(self.frame_algoritmos, text="FCFS", command=partial(self.ejecutar, "FCFS"))
        self.fcfs_btn.pack(side=tk.LEFT, padx=5)
        self.sjf_btn = tk.Button(self.frame_algoritmos, text="SJF", command=partial(self.ejecutar, "SJF"))
        self.sjf_btn.pack(side=tk.LEFT, padx=5)
        self.srtf_btn = tk.Button(self.frame_algoritmos, text="SRTF", command=partial(self.ejecutar, "SRTF"))
        self.srtf_btn.pack(side=tk.LEFT, padx=5)
        self.rr_btn = tk.Button(self.frame_algoritmos, text="ROUND ROBIN", command=partial(self.ejecutar, "ROUND ROBIN"))
        self.rr_btn.pack(side=tk.LEFT, padx=5)



    # ---------------- Validación de números ----------------
    def validar_numero(self, valor):
        return valor.isdigit() or valor == ""

    def agregar_proceso(self):
        nombre = simpledialog.askstring("Nombre", "Nombre del proceso:")
        llegada = simpledialog.askinteger("Llegada", "Tiempo de llegada:")
        duracion = simpledialog.askinteger("Duración", "Duración del proceso:")
        if nombre and llegada is not None and duracion is not None:
            self.procesos.append(Proceso(nombre, llegada, duracion))
            self.actualizar_lista()

    def eliminar_proceso(self):
        selected = self.lista_procesos.curselection()
        if selected:
            idx = selected[0]
            self.procesos.pop(idx)
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_procesos.delete(0, tk.END)
        for p in self.procesos:
            self.lista_procesos.insert(tk.END, f"{p.nombre} | Llegada: {p.llegada} | Duración: {p.duracion}")

    def ejecutar(self, algoritmo):
        if not self.procesos:
            messagebox.showwarning("Atención", "No hay procesos para ejecutar")
            return
        # Leer quantum desde el Entry
        try:
            quantum = int(self.quantum_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Quantum inválido, usando 2 por defecto")
            quantum = 2
        animar(list(self.procesos), algoritmo=algoritmo, quantum=quantum)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
