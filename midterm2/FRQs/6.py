class Heap:
    def __init__(self):
        self.data = []

    @staticmethod
    def _parent(idx):
        return (idx-1)//2

    @staticmethod
    def _left(idx):
        return idx*2+1

    @staticmethod
    def _right(idx):
        return idx*2+2

    ################################################################################
    # BEGIN SOLUTION
    ################################################################################
    def delete(self, val): # delete val from the heap
        assert(len(self.data) > 0)
        replace = self.pop()
        if not replace == val:
            for i in range(len(self.data)):
                x = self.data[i]
                if x == val:
                    self.data[i] = replace

            self.heapify()
                

    ################################################################################
    # END SOLUTION
    ################################################################################

    def heapify(self, idx=0):
        while True:
            l = Heap._left(idx)
            r = Heap._right(idx)
            maxidx = idx
            if l < len(self) and self.data[l] > self.data[idx]:
                maxidx = l
            if r < len(self) and self.data[r] > self.data[maxidx]:
                maxidx = r
            if maxidx != idx:
                self.data[idx], self.data[maxidx] = self.data[maxidx], self.data[idx]
                idx = maxidx
            else:
                break

    def add(self, x):
        self.data.append(x)
        i = len(self.data) - 1
        p = Heap._parent(i)
        while i > 0 and self.data[p] < self.data[i]:
            self.data[p], self.data[i] = self.data[i], self.data[p]
            i = p
            p = Heap._parent(i)

    def peek(self):
        return self.data[0]

    def pop(self):
        ret = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]
        self.heapify()
        return ret

    def __iter__(self):
        return self.data.__iter__()

    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)
  

