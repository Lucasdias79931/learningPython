class Data:
    def __init__(self, book):
        self.book = book

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.base = None
        self.top = None
   
    def bsort(self, ordem):
        if self.base is None or self.top is None:
            return 
        
        current = self.base

        while(current != self.top):
            next = current.next
            while next != None:
                if ordem == 1:
                    if current.data.book > next.data.book:
                        aux = current.data
                        current.data = next.data
                        next.data = aux
                else:
                    if current.data.book < next.data.book:
                        aux = current.data
                        current.data = next.data
                        next.data = aux
                next = next.next
            current = current.next

    def is_empty(self):
        return self.base is None

    def create_data(self, book):
        return Data(book)

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.base = new_node
            self.top = new_node
        else:
            self.top.next = new_node
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return None

        book = self.top.data.book

        if self.top == self.base:
            self.top = None
            self.base = None
        else:
            current = self.base
            while current.next != self.top:
                current = current.next
            current.next = None
            self.top = current

        return book

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data.book

    def size(self):
        if self.is_empty():
            return 0
        tam = 0
        current = self.base
        while current is not None:
            tam += 1
            current = current.next
        return tam

    def clear(self):
        while not self.is_empty():
            self.pop()

    def search(self, item):
        if self.is_empty():
            return -1

        pos = -self.size() + 1
        current = self.base
        while current is not None:
            if current.data.book == item:
                return pos
            pos += 1
            current = current.next

        return -1

    def copy_stack(self):
        new_stack = Stack()
        current = self.base
        while current is not None:
            new_stack.push(self.create_data(current.data.book))
            current = current.next
        return new_stack

    def reverse(self):
        if self.base is None or self.base == self.top:
            return

        current = self.base
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.base = previous
    def merge_stack(self, stack_two):
        if self.is_empty() or stack_two.is_empty():
            print("\nUma das listas ou as duas são nulas")
            return None

        new_stack = Stack()
        current_stack_origin = self.base
        while current_stack_origin is not None:
            new_stack.push(self.create_data(current_stack_origin.data.book))
            current_stack_origin = current_stack_origin.next

        current_stack_origin = stack_two.base
        while current_stack_origin is not None:
            new_stack.push(self.create_data(current_stack_origin.data.book))
            current_stack_origin = current_stack_origin.next

        return new_stack

    def iterate(self, index):
        if self.is_empty() or index < 0 or index >= self.size():
            return None

        current = self.base
        for _ in range(index):
            current = current.next
        return current

    def print_stack(self):
        if self.is_empty():
            print("\nStack vazia!")
            return

        current = self.base
        while current is not None:
            print(f"\n{current.data.book}")
            current = current.next


if __name__ == "__main__":
    stack = Stack()

    stack.push(stack.create_data("sandman"))
    stack.push(stack.create_data("ana"))
    stack.push(stack.create_data("paulo"))

    print("\ninterando a partir da base até o top")
    for i in range(stack.size()):
        current = stack.iterate(i)
        print(f"\nNode {i + 1}, Book: {current.data.book}")
    stack.bsort(1)

    print("\nstack ordenada")
    for i in range(stack.size()):
        current = stack.iterate(i)
        print(f"\nNode {i + 1}, Book: {current.data.book}")
