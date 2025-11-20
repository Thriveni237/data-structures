# Fibonacci Heap
class FibNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None
        self.mark = False
fib_heap_root = FibNode(1)
print('Fibonacci Heap created')
