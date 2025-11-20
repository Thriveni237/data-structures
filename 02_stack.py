# Stack Implementation

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Return the top item without removing it"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the size of the stack"""
        return len(self.items)
    
    def display(self):
        """Display all items in the stack"""
        print('Stack (top to bottom):', self.items[::-1])

# Test the Stack
if __name__ == '__main__':
    stack = Stack()
    print('Is empty:', stack.is_empty())
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    
    print('Stack size:', stack.size())
    stack.display()
    
    print('Peek:', stack.peek())
    print('Pop:', stack.pop())
    stack.display()
    
    print('Is empty:', stack.is_empty())
