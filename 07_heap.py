# Heap Implementation (Min Heap)
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        """Add a value to the heap"""
        heapq.heappush(self.heap, value)
    
    def pop(self):
        """Remove and return the smallest element"""
        if self.heap:
            return heapq.heappop(self.heap)
        return None
    
    def peek(self):
        """Return the smallest element without removing it"""
        if self.heap:
            return self.heap[0]
        return None
    
    def size(self):
        """Return the size of the heap"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if the heap is empty"""
        return len(self.heap) == 0
    
    def display(self):
        """Display the heap"""
        print('Heap:', self.heap)

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        """Add a value to the max heap (negate for max-heap behavior)"""
        heapq.heappush(self.heap, -value)
    
    def pop(self):
        """Remove and return the largest element"""
        if self.heap:
            return -heapq.heappop(self.heap)
        return None
    
    def peek(self):
        """Return the largest element without removing it"""
        if self.heap:
            return -self.heap[0]
        return None

# Test the Heap
if __name__ == '__main__':
    min_heap = MinHeap()
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        min_heap.push(val)
    
    print('Min Heap:')
    min_heap.display()
    print('Peek (min):', min_heap.peek())
    print('Pop (min):', min_heap.pop())
    min_heap.display()
    
    max_heap = MaxHeap()
    for val in values:
        max_heap.push(val)
    
    print('\nMax Heap:')
    print('Peek (max):', max_heap.peek())
    print('Pop (max):', max_heap.pop())
    print('Peek (max) after pop:', max_heap.peek())
