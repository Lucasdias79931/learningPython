from npc import NPC

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome,time,self.forca,self.municao)


