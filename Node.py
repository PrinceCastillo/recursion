class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last.next = new_node

    def print_precursion(self, node):
        if node is Node:
            return
        print(node.data)
        self.print_precursion(node.next)

    def start_recursion_traversal(self):
        self.print_precursion(self.head)

if  __name__ == "__main__"




