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
    
    def insert_index(self, data: int, index: int):
        if index > self.size or index < 0:
            raise IndexError(f"Index {index} out of range [0, {self.size}]")
        
        if index == 0:
            self.appstart(data)
            return
        
        if index == self.size:
            self.append(data)
            return
        
        new_node = Node(data)
        current = self.__get_node(index)

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node

        self.size += 1

    def __get_node(self, index: int) -> Node:
        if index >= self.size or index < 0:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    

    def removestart(self):
        current = self.head
        self.head = current.next
        self.size -= 1
        return current


    def pop(self):
        current = self.tail
        self.tail = current.prev
        self.size -= 1
        return current
    

    def removeindex(self, index: int) -> Node:
        if index > self.size or index < 0:
            raise IndexError(f"Index {index} out of range [0, {self.size}]")
        
        if index == 0:
            self.removestart()
            return
        
        if index == self.size:
            self.pop()
            return
        
        current = self.__get_node(index)
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return current


    def print(self):
        current = self.head
        while current.next:
            print(current.data)
            current = current.next
        
l = List()
for i in range(6):
    l.insert_index(i, i)
l.print()
e = l.remove_index(2)
l.print()
print(e.data)
