# Persistent Segment Tree
class PersistentSegTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.versions = []
    def build(self):
        self.versions.append(self.arr[:])
    def update(self, idx, val):
        new_version = self.arr[:]
        new_version[idx] = val
        self.arr = new_version
        self.versions.append(new_version)
pst = PersistentSegTree([1, 2, 3, 4])
pst.build()
print('Persistent Segment Tree created')
