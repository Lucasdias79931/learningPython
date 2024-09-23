from npc import NPC



class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome,time,self.forca,self.municao)
        
    def inf(self):
        super().info()
              
    


        