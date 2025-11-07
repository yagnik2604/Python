
class Node:
    def __init__(self, data):
        self.data = data # store data
        self.next = None # points to next node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node                    
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end='->')
            curr = curr.next
        print("None")


ll = LinkedList()
ll.append(22)
ll.append(23)
ll.append(24)
ll.display()
