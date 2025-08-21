import tkinter as tk
from tkinter import messagebox
import threading

def mostrar_alerta():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Título", "Rodando no main thread!")
    root.destroy()

if __name__ == "__main__":
    # Executa direto no main thread (funciona)
    mostrar_alerta()
