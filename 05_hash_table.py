# Hash Table Implementation (using dictionary for simplicity)

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Generate hash for a key"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert key-value pair into hash table"""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def search(self, key):
        """Search for a value by key"""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """Delete a key-value pair"""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        return False
    
    def display(self):
        """Display all key-value pairs"""
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f'Index {i}: {bucket}')

# Test the Hash Table
if __name__ == '__main__':
    ht = HashTable()
    ht.insert('name', 'Alice')
    ht.insert('age', 25)
    ht.insert('city', 'NYC')
    ht.insert('email', 'alice@example.com')
    
    print('Hash Table Contents:')
    ht.display()
    
    print('Search name:', ht.search('name'))
    print('Search age:', ht.search('age'))
    
    ht.delete('age')
    print('After deleting age:')
    ht.display()
