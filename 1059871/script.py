import tkinter as tk
from tkinter import messagebox

# Criar janela principal (oculta)
root = tk.Tk()
root.withdraw()  # esconde a janela principal

# Exibir mensagem de alerta
messagebox.showwarning("Atenção", "Isso é um alerta!")

# Fechar a aplicação
root.destroy()
