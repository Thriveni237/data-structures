# Red Black Tree
class RBNode:
    def __init__(self, val):
        self.val = val
        self.color = 'RED'
        self.left = None
        self.right = None
        self.parent = None
class RBTree:
    def __init__(self):
        self.root = None
    def insert(self, val):
        node = RBNode(val)
        if not self.root:
            self.root = node
            self.root.color = 'BLACK'
        else:
            self._insert_recursive(self.root, node)
rbt = RBTree()
rbt.insert(10)
print('RB Tree created')
