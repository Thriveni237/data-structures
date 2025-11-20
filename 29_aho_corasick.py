# Aho-Corasick Algorithm
class ACNode:
    def __init__(self):
        self.go = {}
        self.fail = None
        self.val = 0
root = ACNode()
print('Aho-Corasick created')
