import ctypes

def alerta(msg, titulo="Alerta"):
    ctypes.windll.user32.MessageBoxW(0, msg, titulo, 0x40 | 0)

# Pode chamar dentro de qualquer thread
alerta("Isso funciona dentro da thread!", "Aviso")
