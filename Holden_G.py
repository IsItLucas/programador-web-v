import ctypes
import threading


def alerta(msg, titulo="Alerta"):
    ctypes.windll.user32.MessageBoxW(0, msg, titulo, 0x40 | 0)


threading.Thread(target=alerta, args=("Hello, Holden. You said my virus is boring, huh?\nI'm gonna make you regret it.", "Alert!")).start()
