class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None
class List:       
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        
    def append(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        # current = self.head
        # while current.next:
        #     current = current.next
        # current.next = new_node
        # new_node.prev = current

        self.size += 1

    def appstart(self, data: int):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1
    
    def addindex(self, data: int, index: int):
        new_node = Node(data)

        current = self.head
        counter = 0
        while counter != index:
            current = current.next
            counter += 1
        value = current.prev
        current.prev = new_node
        new_node.next = current
        new_node.prev = value

        self.size += 1

    def pop(self, data: int):
        del_node = Node(data)
        current = self.head
        while current != del_node:
            value = current
            current = current.next
        value.next = current
        self.size -= 1
        return current

    def print(self):
        current = self.head
        while current.next:
            print(current.data)
            current = current.next
        
l = List()
for i in range(6):
    l.append(i)
l.pop(2)
l.print()

# g = List()
# for i in range(5):
#     g.appstart(i)
# g.print()
