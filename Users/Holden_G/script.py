def message_box(msg, title):
	ctypes.windll.user32.MessageBoxW(0, msg, title, 0x10)


message_box("This is a test error message.", "Test")
