from src.Models import Acesso
from queue import Queue

class AcessoService:
    def __init__(self, queueAcessos = None):
        if queueAcessos:
            self.__fila_acessos = queueAcessos
        else:
            self.__fila_acessos = Queue()