class binaryTree:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None


    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = binaryTree(value)
        else:
            newNode = binaryTree(value)
            newNode.left_child = self.left_child
            self.left_child = newNode

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = binaryTree(value)
        else:
            new_node = binaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

try:
    a_node = binaryTree('a')
    a_node.insert_left('b')
    a_node.insert_right('c')

    b_node = a_node.left_child
    b_node.insert_right('d')

    c_node = a_node.right_child
    c_node.insert_left('e')
    c_node.insert_right('f')

    d_node = b_node.right_child
    e_node = c_node.left_child
    f_node = c_node.right_child

    print(a_node.value) # a
    print(b_node.value) # b
    print(c_node.value) # c
    print(d_node.value) # d
    print(e_node.value) # e
    print(f_node.value) # f
except AttributeError as e:
    print(f"Erro de atributo: {e}")

except ValueError as e:
    print(f"Erro de valor: {e}")

except Exception as e:  
    print(f"Ocorreu um erro: {e}")