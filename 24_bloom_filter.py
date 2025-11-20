# Bloom Filter
class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.filter = [False] * size
    def _hash(self, item, seed):
        return (hash(item) + seed) % self.size
    def add(self, item):
        for i in range(3):
            idx = self._hash(item, i)
            self.filter[idx] = True
    def contains(self, item):
        for i in range(3):
            idx = self._hash(item, i)
            if not self.filter[idx]:
                return False
        return True
bf = BloomFilter(100)
print('Bloom Filter created')
