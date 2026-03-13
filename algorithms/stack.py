class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        new_node = Node(data)
        
        new_node.next = self.top
        
        self.top = new_node
        self._size += 1

    def is_empty(self):
        return not self._size

    def pop(self):
        if self.top is None:
            raise IndexError("Empty stack")
        
        popped_node = self.top

        self.top = popped_node.next
        self._size -= 1

        return popped_node.data



    def peek(self):
        if self.top is None:
            raise IndexError("Empty stack")
        
        return self.top.data

    
    def size(self):
        return self._size
    


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(5)
stack.push(1)
print(stack.pop())
print(stack.peek())
print(stack.size())
print(stack.is_empty())