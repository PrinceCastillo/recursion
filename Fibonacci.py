def fibonacci(n):
    if n <= 0:
        return "invalid output"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


class Node:
    def __int__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __int__(self):
        self.head = None

    def print_recursion(self, node):
        if node is None:
            return
        print(node.data)
        self.print_recursion(node.next)


if _name_ == "_main_":
    print(fibonacci(10))

    list = LinkedList
    list.print_recursion(Node)