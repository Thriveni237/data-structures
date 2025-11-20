# Skip List
import random
class SkipNode:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)
head = SkipNode(None, 3)
print('Skip List created')
