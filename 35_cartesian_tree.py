# Cartesian Tree
class CartNode:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.left = None
        self.right = None
root = CartNode(5, 0)
print('Cartesian Tree created')
