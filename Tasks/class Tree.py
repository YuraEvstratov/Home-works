class Node:
    def __init__(self, data: int):
        self.key = data
        self.right = None
        self.left = None
        self.prev = None
        self.count = 1

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data: int):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if current.key == data:
                current.count += 1
                return
            elif current.key > data:
                if current.left is None:
                    current.prev = current
                    current.left = new_node
                    return
                current = current.left

            else: 
                if current.right is None:
                    current.prev = current
                    current.right = new_node
                    return
                current = current.right

    def delete(self, data: int) -> int:
        current = self.__get_current(data)
        if current.left is None and current.right is None:
            if current.prev is None:
                self.root = None
            else:
                if current.key < current.prev.key:
                    current.prev.left = None
                else:
                    current.prev.right = None
        elif not current.left is None:
            if current.left.right is None:
                if current.key < current.prev.key:
                    current.prev.left = current.left
                else:
                    current.prev.right = current.left
            else:
                if current.key < current.prev.key:
                    current.prev.left = current.left.right
                else:
                    current.prev.right = current.left.right
        

                

        
            
    def find(self, data: int) -> int:
        current = self.root
        while current is not None:
            if current.key == data:
                return current.count
            elif current.key < data:
                current = current.right
            else:
                current = current.left
        return 0

    def __get_current(self, data: int) -> int:
            current = self.root
            while current is not None:
                if current.key == data:
                    return current
                elif current.key < data:
                    current = current.right
                else:
                    current = current.left
            return 0
    
    def print_forward(self, current):
        list = []
        
        
    def print_reversed(self):
        current = self.root
        def f(current):
            if current.left:
                f(current.left)
            print(current.key)
            if current.right:
                return f(current.right)

        return f(current)
    
    def print_LMR(self):
        current = self.root
        def f(current):
                if not current.left is None:
                    f(current.left)
                print(current.key)
                if not current.right is None:
                    return f(current.right)
        
                    
        return f(current)
            





l = Tree()
l.insert(5)
l.insert(2)
l.insert(9)
l.insert(78)
l.print_LMR()
print("")
l.print_forward()
print("")
l.print_reversed()
            
        