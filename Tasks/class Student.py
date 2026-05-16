class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None
class List:       
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

        self.size += 1

    def appstart(self, data: int):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        current = new_node
        current.next = self.head
        self.head = current
        self.size += 1
    
    def print(self):
        current = self.head
        while current.next:
            print(current.data)
            current = current.next
        
l = List()
for i in range(5):
    l.append(i)
l.print()

l = List()
for i in range(5):
    l.appstart(i)
l.print()
