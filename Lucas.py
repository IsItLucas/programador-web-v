import ctypes
import threading


def alerta(msg, titulo="Alerta"):
    ctypes.windll.user32.MessageBoxW(0, msg, titulo, 0x40 | 0)


threading.Thread(target=alerta, args=("Mensagem paralela!", "Aviso")).start()
