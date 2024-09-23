class NPC:
    def __init__(self,nome,time,forca,municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
    
    def info(self):
        print("nome....:" + self.nome)
        print("time....:" + str(self.time))
        print("forca...:" + str(self.forca))
        print("munição.: " + str(self.municao))
        print("vivo...:" + ("sim" if self.vivo else "não "))
        print("energia:" + str(self.energia))
        print("-----------------------------------------")