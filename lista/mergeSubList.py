class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class List:
    def __init__(self, data = None):
        if data:
            self.head = Node(data)
        else:
            self.head = None

    def push(self, data):
        newNode = Node(data)
        
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode


lista = List(List(2))

print(lista.head.data.head.data)