# Van Emde Boas Tree
class VEBTree:
    def __init__(self, u):
        self.u = u
        if u <= 2:
            self.A = [False] * u
            return
        self.min = None
        self.max = None
veb = VEBTree(16)
print('Van Emde Boas Tree created')
