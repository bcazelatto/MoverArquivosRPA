import os

class Config:

    # Diretório atual
    diretorio_padrao = os.environ['USERPROFILE']

    # Configs LOG
    caminho_log = f"{diretorio_padrao}/eclipse-workspace/Python/RPA/MoverArquivos_RPA/Log"

    caminho_entrada = f'{diretorio_padrao}/eclipse-workspace/Python/RPA/MoverArquivos_RPA/Entrada'
    caminho_saida = f'{diretorio_padrao}/eclipse-workspace/Python/RPA/MoverArquivos_RPA/Saida'
