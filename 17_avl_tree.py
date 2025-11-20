# AVL Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
def insert(node, val):
    if not node:
        return Node(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    node.height = 1 + max(height(node.left), height(node.right))
    return node
def height(node):
    return node.height if node else 0
tree = None
tree = insert(tree, 10)
tree = insert(tree, 20)
print('AVL Tree created')
