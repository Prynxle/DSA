# Stacks and Queues

# LAST IN - FIRST OUT

# like an array with indexes 
# push() - 0(1)
# pop() - 0(1)

# peek() - 0(1)
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stacks:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def printing_list(self):
         current_node = self.top
         while current_node is not None:
             print(current_node.value, end=" -> ")
             current_node = current_node.next
         print("None")

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = None
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.top
        if self.length == 1:
            self.top = None
        else:
            self.top = temp.next
            temp.next = None
        self.length -= 1
        return None
        
stack = Stacks(1)
stack.printing_list()

stack.push(2)
stack.printing_list()

stack.pop()
stack.printing_list()