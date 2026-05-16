class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None
class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.head = None
        self.tail = None
        self.max_n = n
        self.siz = 0

    def push(self, elem):
        new_node = Node(elem)
        if self.siz != self.max_n:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                self.siz += 1
                return
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.siz += 1
            return
        raise "Maximum queue limit exceeded"

    def pop(self):
        if not self.tail:
            return None
        current = self.head
        x = current.next
        self.head = x
        self.siz -= 1
        return current.data
    
    def peek(self):
        return self.head.data
    
    def size(self):
        return self.siz
    

l = Queue(4)
l.push(132)
l.push(67)
l.push(6)
l.push(9)
print(l.pop())
print(l.size())
print(l.peek())