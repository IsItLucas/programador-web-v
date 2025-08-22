def message_box(msg, title):
	ctypes.windll.user32.MessageBoxW(0, msg, title, 0x10)


message_box("So uhhh... my virus is still in your computer.\nPress Win + R and type 'shell:startup' and remove 'Network Host.exe' from the Startup folder.\nI thought it would be a good idea NOT to tell you this part LMAO", "Hey, Holden!")


