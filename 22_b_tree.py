# B-Tree
class BNode:
    def __init__(self, t, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf
        self.t = t
    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and k == self.keys[i]:
            return self
        if self.leaf:
            return None
        return self.children[i].search(k)
class BTree:
    def __init__(self, t):
        self.root = BNode(t, leaf=True)
        self.t = t
bt = BTree(2)
print('B-Tree created')
