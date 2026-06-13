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
    

    def remove_start(self) -> Node:
        if self.head == None:
            raise IndexError("Remove from empty list")
        
        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = current.next
            self.head.prev = None
        
        current.next = None
        self.size -= 1
        return current


    def pop(self) -> Node:
        if self.tail == None:
            raise IndexError("Remove from empty list")
        
        current = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return current
        
        self.tail = current.prev
        self.tail.next = None
        current.prev = None
        self.size -= 1
        return current
    

    def remove_index(self, index: int) -> Node:
        if index > self.size or index < 0:
            raise IndexError(f"Index {index} out of range [0, {self.size}]")
        
        if index == 0:
            return self.remove_start()
        
        if index == self.size:
            return self.pop()
        
        current = self.__get_node(index)
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return current


    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        
l = List()
for i in range(6):
    l.insert_index(i, i)
print(l.remove_index(2).data)
print(l.remove_index(5).data)
l.print()

