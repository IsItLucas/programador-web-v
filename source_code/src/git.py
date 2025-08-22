import requests
import base64
import json


OK = 200
OK_CREATED = 201
ERR_NOT_FOUND = 404


TOKEN = "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"

REPO_NOME = "IsItLucas/programador-web-v"
REPO_BRANCH = "main"


def ler_arquivo(caminho):
	url = f"https://api.github.com/repos/{REPO_NOME}/contents/{caminho}?ref={REPO_BRANCH}"

	request = requests.get(url, headers = get_headers(), verify = False)

	if request.status_code == OK:
		conteudo_codificado = request.json()["content"]
		conteudo = base64.b64decode(conteudo_codificado).decode()
		return conteudo
	
	elif request.status_code == ERR_NOT_FOUND:
		print("Arquivo não encontrado: " + caminho)
		return ""

	else:
		raise Exception(f"Erro ao acessar arquivo: {request.status_code}, {request.text}")


def criar_arquivo(caminho, conteudo, sobrescrever):
	conteudo_codificado = base64.b64encode(conteudo.encode()).decode()
	sha = get_sha(caminho)

	data = {
		"message": "Criado / atualizado " + caminho,
		"content": conteudo_codificado,
		"branch": REPO_BRANCH
	}

	if sha:
		data["sha"] = sha

		if not sobrescrever:
			return

	url = f"https://api.github.com/repos/{REPO_NOME}/contents/{caminho}"

	request = requests.put(url, headers = get_headers(), data = json.dumps(data), verify = False)

	if request.status_code in [OK, OK_CREATED]:
		acao = "atualizado" if sha else "criado"
		print(f"Arquivo {acao} com sucesso: {caminho}")
	
	else:
		raise Exception(f"Error trying to create/update file: {request.status_code}, {request.text}")


def deletar_arquivo(caminho):
    sha = get_sha(caminho)
    if not sha:
        print("Arquivo não encontrado: " + caminho)
        return

    url = f"https://api.github.com/repos/{REPO_NOME}/contents/{caminho}"
    data = {
        "message": "Deletado " + caminho,
        "sha": sha,
        "branch": REPO_BRANCH
    }

    request = requests.delete(url, headers = get_headers(), json = data, verify = False)
    if request.status_code == OK:
        print(f"Arquivo deletado com sucesso: {caminho}")
    else:
        raise Exception(f"Erro ao deletar arquivo: {request.status_code}, {request.text}")


def get_sha(caminho):
	url = f"https://api.github.com/repos/{REPO_NOME}/contents/{caminho}?ref={REPO_BRANCH}"
	
	request = requests.get(url, headers = get_headers(), verify = False)

	if request.status_code == OK:
		return request.json()["sha"]
	
	elif request.status_code == ERR_NOT_FOUND:
		return None
	
	else:
		raise Exception(f"Erro ao acessar GitHub: {request.status_code}, {request.text}")


def get_headers():
	return {
		"Authorization": f"token {TOKEN}",
		"Accept": "application/vnd.github.v3+json"
	}