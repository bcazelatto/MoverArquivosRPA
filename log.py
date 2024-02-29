import os
from settings import Config
from datetime import datetime

class Logging:

    def execute(status, mensagem):
        # Obtendo a data e hora atual
        data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_atual = datetime.now().strftime("%Y%m%d")

        if not os.path.exists(Config.caminho_log):
            os.makedirs(Config.caminho_log)
        
        caminho_arquivo_log = os.path.join(Config.caminho_log, f'{data_atual}_LOGTECNICO.txt')

        with open (caminho_arquivo_log, 'a') as arquivo:
            #Escrevendo log
            arquivo.write(f'{data_hora_atual}: {status} - {mensagem}\n')

