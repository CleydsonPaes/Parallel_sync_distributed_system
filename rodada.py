
from times import *
from partida import *

class Rodada:
    def __init__(self, partidas) -> None:
        self.partidas = partidas #Objeto time
        self.resultados = []
    pass
    #SET
    def setTime1(self,partidas):
        self.partidas = partidas
    def setTime1(self,resultados):
        self.resultados = resultados

    #GET
    def getTime1(self):
        return self.partidas
    def getTime1(self):
        return self.resultados

