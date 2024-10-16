#enqueue / append
#dequeue / pop_first
#peek
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def printlist(self):
        current_node = self.first
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.printlist()  

queue.dequeue()
queue.printlist()
