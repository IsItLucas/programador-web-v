import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # esconde a janela principal

messagebox.showinfo("Título", "Isso é um alerta!")
