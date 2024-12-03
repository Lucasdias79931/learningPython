class NO():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Lista():

    def __init__(self):
       self.ini = None
       
       
    def append(self,element):

        if self.ini == None:
            self.ini = NO(element)
            
           
        else:
            atual = self.ini
           
            while atual.next != None:
                atual = atual.next

            atual.next = NO(element)

    def update(self,element,novo):
        if self.ini is None:
            print("Lista vazia!")
            return

        if self.ini.data == element:
            self.ini = novo
            return
        else:
            atual = self.ini
            while atual is not None and atual.data != element:
                atual = atual.next
            
            if atual.data == element:
                atual.data = novo
                return
        
        print("elemento não encontradao!")

    def delet(self, element):
        if self.ini is None:
            print("Lista vazia!")
            return

        if self.ini.data == element:
            self.ini = self.ini.next
            return
        else:
            atual = self.ini
            anterior = None
            while atual is not None and atual.data != element:
                anterior = atual
                atual = atual.next
            
            if atual is not None and atual.data == element:
                anterior.next = atual.next
                atual = None
                return
        
        print("Elemento não encontrado!")

                    
        
    def imprime(self):
        atual = self.ini
        while atual is not None:
            print(atual.data)
            print("\n")
            atual = atual.next


            

