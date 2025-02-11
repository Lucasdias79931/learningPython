class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Lista():

    def __init__(self, element = None):
        if not element:
            self.ini = None
            self.end = None
            self.size = 0
        else:
            self.ini = Node(element)
            self.end = self.ini
            self.size = 1
       
       
       
    def append(self,element):
        newNode = Node(element)

        if self.size == 0:
            self.ini = newNode
            self.end = self.ini
        else:
            newNode.prev = self.end
            self.end.next = newNode
            self.end = newNode
        
        self.size += 1
    
    def search(self, index):
        if index > self.size or index < self.size * -1:
            raise ValueError(e)
            return
        if index == 0 or index == (self.size) * -1:
            return self.ini.data
        
        if index == self.size - 1 or index == -1:
            return self.end.data

        if index > 0:
            if index < (self.size -1) // 2:
                current = self.ini.next
                currentIndex = 1
                while(currentIndex != index):
                    current = current.next
                    currentIndex += 1
                return current.data 
            else:
                current = self.end.prev
                currentIndex = self.size - 1
                while(currentIndex != index):
                    current = current.prev
                    currentIndex -= 1
                return current.data 
        else:
            if index >= (self.size * - 1 ) // 2:
                ...

