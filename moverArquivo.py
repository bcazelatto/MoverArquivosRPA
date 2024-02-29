from settings import Config
from log import Logging
import os

class MoveFiles:
   
    def mover(arquivo, extensao):
        try:
            Logging.execute('INFO', f'INICIANDO MOVIMENTACAO DO ARQUIVO [{arquivo}.{extensao}]'.upper())
            if not os.path.exists(Config.caminho_entrada):
                Logging.execute('WARMING', 'PASTA DE ENTRADA NAO EXISTE')
            else:
                if not os.path.exists(f'{Config.caminho_entrada}/{arquivo}.{extensao}'):
                    Logging.execute('WARMING', 'ARQUIVO DE ENTRADA NAO EXISTE')
                else:
                    if not os.path.exists(Config.caminho_saida):
                        os.makedirs(Config.caminho_saida)
                        Logging.execute('INFO', 'CRIADO PASTA DE SAIDA PARA MOVIMENTACAO DO ARQUIVO')
                    os.rename(f'{Config.caminho_entrada}/{arquivo}.{extensao}', f'{Config.caminho_saida}/{arquivo}.{extensao}')
                    Logging.execute('INFO', f'EXECUTADO MOVIMENTACAO COM SUCESSO DA PASTA {Config.caminho_entrada} PARA A PASTA {Config.caminho_saida}'.replace('\\', '/'))
                    return True
        except Exception as e:
            Logging.execute('ERROR', f'NAO FOI POSSIVEL MOVER O ARQUIVO - {e}')
            return False

        

