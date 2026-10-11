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
                    new_node.prev = current
                    current.left = new_node
                    return
                current = current.left

            else: 
                if current.right is None:
                    new_node.prev = current
                    current.right = new_node
                    return
                current = current.right

    def delete(self, data: int) -> bool:
        current = self._get_node(data)
        if current is None:
            return False
        if current.count > 1:
            current.count -= 1
            return True
        if current.left is None and current.right is None:
            self._transplant(current, None)
        elif current.left is not None or current.right is not None:
            value = current.left if current.left is not None else current.right
            self._transplant(current, value)
        else:
            node = current.right
            while node.left is not None:
                node = node.left
            current.key = node.key
            current.count = node.count
            self._transplant(node, node.right)

                   

    def _transplant(self, u, v):
        if u.prev is None:
            self.root = v
        elif u is u.prev.left:
            u.prev.left = v
        else:
            u.prev.right = v
        if v is not None:
            v.prev = u.prev

            
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

    def _get_node(self, data: int) -> Node:
            current = self.root
            while current is not None:
                if current.key == data:
                    return current
                elif current.key < data:
                    current = current.right
                else:
                    current = current.left
            return None
    
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
l.delete(9)
# print("")
# l.print_forward()
# print("")
# l.print_reversed()

l.print_LMR()          
        