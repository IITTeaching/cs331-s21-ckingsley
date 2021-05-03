class MultiQueue:
  
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self, num_queues=3):
        self.num_queues = num_queues
        self.lengths = [0] * num_queues
        self.heads = [None] * num_queues
        self.tails = [None] * num_queues

    def enqueue(self,item):
    ################################################################################
    # BEGIN SOLUTION
    ################################################################################
        idx = 0
        b = False
        for i in range(self.num_queues):
            if not self.heads[i]:
                idx = i
                b = True
                break

        
        if b: #there is a None head
            self.heads[idx] = self.tails[idx] = self.Node(item)

        elif not b: #all heads are filled
            min = 0
            idx2 = 0
            for i in range(self.num_queues):
                count = 1
                h = self.heads[i]
                t = self.tails[i]
                while h != t:
                    h = h.next
                    count += 1
                if i==0:
                    min = count
                else:
                    if count < min:
                        min = count
                        idx2 = i
            
            self.tails[idx2].next = self.Node(item)
                


    ################################################################################
    # END SOLUTION
    ################################################################################

    def dequeue(self):
        assert(self)
    ################################################################################
    # BEGIN SOLUTION
    ################################################################################
        
        max = 0
        idx = 0
        for i in range(self.num_queues):
            if not self.heads[i]:
                break
            else:
                count = 1
                h = self.heads[i]
                t = self.tails[i]
                while h != t:
                    h = h.next
                    count += 1
                if i==0:
                    max = count
                else:
                    if count > max:
                        max = count
                        idx = i
        
        t = self.tails[idx]
        self.tails[idx] = None
        return t
                
        
    ################################################################################
    # END SOLUTION
    ################################################################################


    def __len__(self):
        return sum(self.lengths)

    def __bool__(self):
        return len(self) > 0

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def listrepr(head):
        c = head
        s = []
        while c:
            s.append(str(c.val))
            c = c.next
        return "[" + ",".join(s) + "]"

    def __repr__(self):
        return "\n".join([ MultiQueue.listrepr(self.heads[i]) for i in range(self.num_queues) ])




m = MultiQueue()
for i in range(3):
    m.enqueue(i)
    print(m)

for i in range(2):
    m.dequeue()