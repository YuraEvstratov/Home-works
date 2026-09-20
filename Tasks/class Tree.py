class Node:
    def __init__(self, data: int):
        self.data = data
        self.right = None
        self.left = None
        self.len = 0

class Tree:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.len += 1
            return
        
        current = self.head
        while True:
            if current.data == new_node.data:
                current.len += 1
                break
            if current.data > new_node.data:
                current = current.left
                if current == None:
                    current = new_node
                    current.len += 1
                    break
            if current.data < new_node.data:
                        current = current.right
                        if current == None:
                            current = new_node
                            current.len += 1
                            break

    def find(self, data: int):
        current = self.head
        find_node = Node(data)
        while current.data != find_node.data:
            if current.data > find_node.data:
                 current = current.left
            if current.data < find_node.data:
                 current = current.right
            if current == None:
                 return 0
        return current.len
    def print(self):
        current = self.head
        while current.right:
            print(current.data)
            current = current.right
        current = self.head
        while current.left:
            print(current.data)
            current = current.left
l = Tree()
for i in range(5):
     l.append(i)
l.print()
l.find(4)
        
            
        