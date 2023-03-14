
from times import *
from partida import *
from rodada import *

class Rodada:
    def __init__(self, rodadas, classificacao, times) -> None:
        self.times = times #Objeto time
        self.rodadas = rodadas
        self.classificacao = classificacao
    pass
    #SET
    def setTime1(self,times):
        self.times = times
    def setTime1(self,rodadas):
        self.rodadas = rodadas
    def setTime1(self,classificacao):
        self.classificacao = classificacao

    #GET
    def getTime1(self):
        return self.times
    def getTime1(self):
        return self.rodadas
    def getTime1(self):
        return self.classificacao

