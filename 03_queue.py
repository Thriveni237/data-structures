# Queue Implementation
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to the rear of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item"""
        if not self.is_empty():
            return self.items.popleft()
        return None
    
    def front(self):
        """Return the front item without removing it"""
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the size of the queue"""
        return len(self.items)
    
    def display(self):
        """Display all items in the queue"""
        print('Queue (front to rear):', list(self.items))

# Test the Queue
if __name__ == '__main__':
    queue = Queue()
    print('Is empty:', queue.is_empty())
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    
    print('Queue size:', queue.size())
    queue.display()
    
    print('Front:', queue.front())
    print('Dequeue:', queue.dequeue())
    queue.display()
    
    print('Is empty:', queue.is_empty())
