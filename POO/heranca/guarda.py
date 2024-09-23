from npc import NPC



class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome,time,self.forca,self.municao)


        