import os

# Nome do arquivo
nome_arquivo = "teste.txt"

# Abre o arquivo em modo escrita ("w") - cria se não existir
with open(nome_arquivo, "w") as f:
    f.write("Conteúdo inicial do arquivo.\n")
