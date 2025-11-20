# Treap (Treap is a tree heap combination)
import random
class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None
root = TreapNode(5)
print('Treap created')
