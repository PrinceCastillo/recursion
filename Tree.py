class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#InOrder
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

#PreOrder
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


#PostOrder
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

#SwapOrder
def swaporder_traversal(root):
    if root:
        root.left, root.right = root.right, root.left
        swaporder_traversal(root.left)
        swaporder_traversal(root.right)

root = Treenode(1)
root.left = Treenode(2)
root.right = Treenode(3)
root.left.right = Treenode(5)
root.left.left = Treenode(4)
root.right.left = Treenode(6)
root.right.right = Treenode(7)

print("In-Order Traversal")
inorder_traversal(root)
print("\nPre-Order Traversal")
preorder_traversal(root)
print("\nPost-Order Traversal")
postorder_traversal(root)

print("\n\nSwapping Subtrees...")
swaporder_traversal(root)
print("\nInorder Traversal After Swap:")
inorder_traversal(root)
print("\nPreOrder Traversal After Swap:")
preorder_traversal(root)
print("\nPostOrder Traversal After Swap")
postorder_traversal(root)